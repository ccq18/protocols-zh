#!/usr/bin/env python3
"""
Batch translate English RFC stubs under rfcs-zh/ to Chinese using OpenAI Chat API.
Requires: export OPENAI_API_KEY=<your_key>
Usage: python3 scripts/translate_rfcs_zh.py
"""
import os
import sys
import time
import re
import argparse
from pathlib import Path
from typing import List

try:
    import openai
except ImportError:
    sys.exit('Please install openai (pip install openai)')

OPENAI_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_KEY:
    sys.exit('Please set OPENAI_API_KEY environment variable')

openai.api_key = OPENAI_KEY
openai.api_base= os.getenv('OPENAI_BASE_URL')
SRC_ROOT = Path('rfcs-zh')

def translate_chunk(text: str) -> str:
    """
    Use OpenAI API to translate a text chunk, with retry on transient errors.
    """
    from openai.error import APIError, RateLimitError, Timeout, ServiceUnavailableError
    import json
    max_retries = 5
    for attempt in range(1, max_retries + 1):
        try:
            resp = openai.ChatCompletion.create(
                model='gpt-4.1-nano',
                messages=[
                    {'role': 'system', 'content': '你是一个专业翻译助手，请将用户提供的英文翻译成流畅的中文。'},
                    {'role': 'user', 'content': f'请将下面的英文翻译成中文：\n```\n{text}\n```'}
                ],
                temperature=0,
            )
            return resp.choices[0].message.content.strip()
        except (APIError, RateLimitError, Timeout, ServiceUnavailableError, json.JSONDecodeError) as e:
            if attempt < max_retries:
                wait = attempt * 2
                print(f"[Warning] translate_chunk attempt {attempt}/{max_retries} failed: {e}. Retrying in {wait}s...")
                time.sleep(wait)
                continue
            else:
                print(f"[Error] translate_chunk failed after {max_retries} attempts: {e}")
                raise
 
def split_text(text: str, max_words: int = 1000) -> List[str]:
    """
    Split text into chunks of at most max_words, preserving paragraphs when possible.
    """
    paragraphs = text.split('\n\n')
    chunks: List[str] = []
    current = ''
    current_words = 0
    for p in paragraphs:
        p_words = len(p.split())
        if current:
            candidate = current + '\n\n' + p
            candidate_words = current_words + p_words
        else:
            candidate = p
            candidate_words = p_words
        if candidate_words <= max_words:
            current = candidate
            current_words = candidate_words
        else:
            if current:
                chunks.append(current)
            if p_words <= max_words:
                current = p
                current_words = p_words
            else:
                # paragraph too long, split by words
                words = p.split()
                for i in range(0, len(words), max_words):
                    chunks.append(' '.join(words[i:i+max_words]))
                current = ''
                current_words = 0
    if current:
        chunks.append(current)
    return chunks

def process_file(path: Path, max_words: int, delay: float):
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    # find first blank line after header
    idx = 0
    for i, line in enumerate(lines):
        if line.strip() == '':
            idx = i
            break
    header = '\n'.join(lines[:idx+1])
    eng = '\n'.join(lines[idx+1:]).strip()
    if not eng:
        print(f'No English content in {path}, skipping.')
        return
    # skip if already contains Chinese (i.e., already translated)
    if re.search(r'[\u4e00-\u9fff]', eng):
        print(f'Skipping {path} (already translated).')
        return
    # split English content into chunks
    parts = split_text(eng, max_words)
    total_parts = len(parts)
    if total_parts > 1:
        print(f'  Split into {total_parts} chunks for translation.')
    zh_parts = []
    # translate each chunk with progress
    for idx, part in enumerate(parts, start=1):
        print(f'    [{idx}/{total_parts}] Translating chunk {idx}/{total_parts}...')
        zh = translate_chunk(part)
        zh_parts.append(zh)
        time.sleep(delay)
    zh_full = '\n\n'.join(zh_parts)
    # assemble final
    out = '\n'.join([header, zh_full])
    path.write_text(out, encoding='utf-8')

def main():
    parser = argparse.ArgumentParser(description='Batch translate RFC stubs under rfcs-zh/')
    parser.add_argument('--max-words', type=int, default=2000,
                        help='max words per translation chunk (default: 2000)')
    parser.add_argument('--delay', type=float, default=0.1,
                        help='seconds to wait between chunks (default: 0.1s)')
    args = parser.parse_args()
    # gather files to process
    files = list(sorted(SRC_ROOT.rglob('rfc*.txt')))
    total = len(files)
    print(f'Found {total} files to translate.')
    # process each file with progress
    for idx, path in enumerate(files, start=1):
        print(f'[{idx}/{total}] Processing {path}')
        try:
            process_file(path, args.max_words, args.delay)
        except Exception as e:
            print(f'[Error] Failed to process {path}: {e}')
    print('All files processed.')

if __name__ == '__main__':
    main()