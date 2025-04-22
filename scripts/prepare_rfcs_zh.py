#!/usr/bin/env python3
"""
Script to generate Chinese translation stubs for RFC files listed in 常用RFC文档整理.md.
Scans the summary markdown for RFC numbers and ranges, locates the corresponding English RFC .txt files,
and creates stub Chinese translation files under the rfcs-zh directory, preserving the RFCs sub-directory.
"""
import os
import re

SUMMARY = '常用RFC文档整理.md'
SRC_ROOT = 'rfcs'
DST_ROOT = 'rfcs-zh'

def find_rfc_numbers(text):
    nums = set()
    # match single or ranges: RFC 7230 or RFC 7230-7235
    for m in re.finditer(r'RFC\s*(\d+)(?:-(\d+))?', text):
        start = int(m.group(1))
        end = int(m.group(2)) if m.group(2) else start
        for n in range(start, end+1):
            nums.add(n)
    return sorted(nums)

def locate_src(rfc_no):
    # determine subdir: groups of 500
    idx = (rfc_no - 1) // 500
    lo = idx*500 + 1
    hi = (idx+1)*500
    sub = f'RFCs{lo:04d}-{hi:04d}'
    fname = f'rfc{rfc_no}.txt'
    path = os.path.join(SRC_ROOT, sub, fname)
    if os.path.isfile(path):
        return sub, fname, path
    return None, None, None

def main():
    # Read summary
    with open(SUMMARY, 'r', encoding='utf-8') as f:
        text = f.read()
    # Extract RFC numbers
    nums = find_rfc_numbers(text)
    # Generate stubs
    for n in nums:
        sub, fname, src = locate_src(n)
        if not src:
            print(f'WARNING: RFC {n} source not found')
            continue
        dst_dir = os.path.join(DST_ROOT, sub)
        os.makedirs(dst_dir, exist_ok=True)
        dst = os.path.join(dst_dir, fname)
        if os.path.exists(dst):
            continue
        with open(dst, 'w', encoding='utf-8') as out, open(src, 'r', encoding='utf-8', errors='ignore') as inp:
            out.write(f'# RFC {n} 中文翻译 (stub)\n')
            out.write(f'# 原文文件: ../{SRC_ROOT}/{sub}/{fname}\n')
            out.write('# TODO: 在此处用中文替换下面的英文原文内容\n\n')
            # 将英文原文内容复制到此处，便于翻译
            for line in inp:
                out.write(line)
    print('Stub translation files generated under', DST_ROOT)

if __name__ == '__main__':
    main()