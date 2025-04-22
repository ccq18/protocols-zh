# 常用RFC文档整理

RFC（Request for Comments）是互联网工程任务组（IETF）发布的一系列备忘录，描述了互联网相关技术的规范和协议。以下是一些常用的RFC文档，按应用领域分类整理。

> 注：带有 🇨🇳 标记的RFC已有中文翻译版本（正在进行中）。可查看[RFC中文翻译项目](rfcs-zh/README.md)和[翻译进度](rfcs-zh/翻译进度.md)了解更多信息。

## 网络基础协议

### IP协议
- [**RFC 791**](rfcs-zh/RFCs0501-1000/rfc791.txt) - 互联网协议（IPv4）
- [**RFC 2460**](rfcs-zh/RFCs2001-2500/rfc2460.txt) - 互联网协议第6版（IPv6）规范
- [**RFC 8200**](rfcs-zh/RFCs8001-8500/rfc8200.txt) - 互联网协议第6版（IPv6）规范（RFC 2460的更新版）

### TCP/IP
- [**RFC 793**](rfcs-zh/RFCs0501-1000/rfc793.txt) - 传输控制协议（TCP） 
- [**RFC 768**](rfcs-zh/RFCs0501-1000/rfc768.txt) - 用户数据报协议（UDP）
- [**RFC 1122**](rfcs-zh/RFCs1001-1500/rfc1122.txt) - 互联网主机要求 - 通信层
- [**RFC 1123**](rfcs-zh/RFCs1001-1500/rfc1123.txt) - 互联网主机要求 - 应用和支持

### 路由协议
- [**RFC 2328**](rfcs-zh/RFCs2001-2500/rfc2328.txt) - OSPF版本2
- [**RFC 4271**](rfcs-zh/RFCs4001-4500/rfc4271.txt) - 边界网关协议4（BGP-4）
- [**RFC 2453**](rfcs-zh/RFCs2001-2500/rfc2453.txt) - RIP版本2

## 应用层协议

### HTTP
- [**RFC 1945**](rfcs-zh/RFCs1501-2000/rfc1945.txt) - HTTP/1.0
- [**RFC 2616**](rfcs-zh/RFCs2501-3000/rfc2616.txt) - HTTP/1.1 
- [**RFC 7230**](rfcs-zh/RFCs7001-7500/rfc7230.txt) - HTTP/1.1（RFC 2616的更新版）
- [**RFC 7231**](rfcs-zh/RFCs7001-7500/rfc7231.txt) - HTTP/1.1（RFC 2616的更新版）
- [**RFC 7232**](rfcs-zh/RFCs7001-7500/rfc7232.txt) - HTTP/1.1（RFC 2616的更新版）
- [**RFC 7233**](rfcs-zh/RFCs7001-7500/rfc7233.txt) - HTTP/1.1（RFC 2616的更新版）
- [**RFC 7234**](rfcs-zh/RFCs7001-7500/rfc7234.txt) - HTTP/1.1（RFC 2616的更新版）
- [**RFC 7235**](rfcs-zh/RFCs7001-7500/rfc7235.txt) - HTTP/1.1（RFC 2616的更新版）
- [**RFC 7540**](rfcs-zh/RFCs7501-8000/rfc7540.txt) - HTTP/2
- [**RFC 9114**](rfcs-zh/RFCs9001-9500/rfc9114.txt) - HTTP/3

### 电子邮件
- [**RFC 5321**](rfcs-zh/RFCs5001-5500/rfc5321.txt) - 简单邮件传输协议（SMTP）
- [**RFC 5322**](rfcs-zh/RFCs5001-5500/rfc5322.txt) - 互联网消息格式
- [**RFC 1939**](rfcs-zh/RFCs1501-2000/rfc1939.txt) - 邮局协议版本3（POP3）
- [**RFC 3501**](rfcs-zh/RFCs3501-4000/rfc3501.txt) - 互联网消息访问协议（IMAP）

### DNS
- [**RFC 1034**](rfcs-zh/RFCs1001-1500/rfc1034.txt) - 域名 - 概念和设施
- [**RFC 1035**](rfcs-zh/RFCs1001-1500/rfc1035.txt) - 域名 - 实现和规范
- [**RFC 6891**](rfcs-zh/RFCs6501-7000/rfc6891.txt) - DNS扩展机制（EDNS(0)）

### FTP
- [**RFC 959**](rfcs-zh/RFCs0501-1000/rfc959.txt) - 文件传输协议（FTP）
- [**RFC 2228**](rfcs-zh/RFCs2001-2500/rfc2228.txt) - FTP安全扩展
- [**RFC 4217**](rfcs-zh/RFCs4001-4500/rfc4217.txt) - 使用TLS的FTP安全

## 安全协议

### TLS/SSL
- [**RFC 5246**](rfcs-zh/RFCs5001-5500/rfc5246.txt) - 传输层安全协议（TLS）1.2版
- [**RFC 8446**](rfcs-zh/RFCs8001-8500/rfc8446.txt) - 传输层安全协议（TLS）1.3版 

### 加密与认证
- [**RFC 2104**](rfcs-zh/RFCs2001-2500/rfc2104.txt) - HMAC：用于消息认证的密钥散列
- [**RFC 3447**](rfcs-zh/RFCs3001-3500/rfc3447.txt) - PKCS #1：RSA加密规范版本2.1
- [**RFC 5280**](rfcs-zh/RFCs5001-5500/rfc5280.txt) - X.509公钥基础设施证书和CRL简介

### 网络安全
- [**RFC 2401**](rfcs-zh/RFCs2001-2500/rfc2401.txt) - IP安全体系结构
- [**RFC 4301**](rfcs-zh/RFCs4001-4500/rfc4301.txt) - IP安全体系结构（RFC 2401的更新版）
- [**RFC 4302**](rfcs-zh/RFCs4001-4500/rfc4302.txt) - IP认证头
- [**RFC 4303**](rfcs-zh/RFCs4001-4500/rfc4303.txt) - IP封装安全有效载荷（ESP）

## Web技术

### REST
- [**RFC 7231**](rfcs-zh/RFCs7001-7500/rfc7231.txt) - HTTP/1.1：语义和内容

### JSON
- [**RFC 7159**](rfcs-zh/RFCs7001-7500/rfc7159.txt) - JavaScript对象表示法（JSON）
- [**RFC 8259**](rfcs-zh/RFCs8001-8500/rfc8259.txt) - JavaScript对象表示法（JSON）（RFC 7159的更新版）

### WebSocket
- [**RFC 6455**](rfcs-zh/RFCs6001-6500/rfc6455.txt) - WebSocket协议

## 互联网标准与最佳实践

### IPv6过渡
- [**RFC 4213**](rfcs-zh/RFCs4001-4500/rfc4213.txt) - 从IPv4到IPv6的基本过渡机制

### 网络管理
- [**RFC 3411**](rfcs-zh/RFCs3001-3500/rfc3411.txt) - 简单网络管理协议（SNMP）v3
- [**RFC 3412**](rfcs-zh/RFCs3001-3500/rfc3412.txt) - 简单网络管理协议（SNMP）v3
- [**RFC 3413**](rfcs-zh/RFCs3001-3500/rfc3413.txt) - 简单网络管理协议（SNMP）v3
- [**RFC 3414**](rfcs-zh/RFCs3001-3500/rfc3414.txt) - 简单网络管理协议（SNMP）v3
- [**RFC 3415**](rfcs-zh/RFCs3001-3500/rfc3415.txt) - 简单网络管理协议（SNMP）v3
- [**RFC 3416**](rfcs-zh/RFCs3001-3500/rfc3416.txt) - 简单网络管理协议（SNMP）v3
- [**RFC 3417**](rfcs-zh/RFCs3001-3500/rfc3417.txt) - 简单网络管理协议（SNMP）v3
- [**RFC 3418**](rfcs-zh/RFCs3001-3500/rfc3418.txt) - 简单网络管理协议（SNMP）v3

### 邮件安全
- [**RFC 5751**](rfcs-zh/RFCs5501-6000/rfc5751.txt) - 安全MIME（S/MIME）版本3.2
- [**RFC 4408**](rfcs-zh/RFCs4001-4500/rfc4408.txt) - 发件人策略框架（SPF）
- [**RFC 6376**](rfcs-zh/RFCs6001-6500/rfc6376.txt) - DomainKeys标识邮件签名（DKIM）

## 其他重要RFC

### DHCP
- [**RFC 2131**](rfcs-zh/RFCs2001-2500/rfc2131.txt) - 动态主机配置协议
- [**RFC 3315**](rfcs-zh/RFCs3001-3500/rfc3315.txt) - IPv6的动态主机配置协议（DHCPv6）

### NTP
- [**RFC 5905**](rfcs-zh/RFCs5501-6000/rfc5905.txt) - 网络时间协议版本4

### OAuth
- [**RFC 6749**](rfcs-zh/RFCs6501-7000/rfc6749.txt) - OAuth 2.0授权框架
- [**RFC 6750**](rfcs-zh/RFCs6501-7000/rfc6750.txt) - OAuth 2.0授权框架：Bearer Token使用

### WebDAV
- [**RFC 4918**](rfcs-zh/RFCs4501-5000/rfc4918.txt) - HTTP扩展：分布式创作和版本控制（WebDAV）

## 注意事项

- RFC文档会随着技术的发展不断更新，有些早期的RFC可能已被更新或废弃
- 最新的RFC文档可以在IETF官方网站（https://www.ietf.org/standards/rfcs/）查阅
- 在使用任何协议或标准时，建议查阅其最新版本的RFC文档
- 如果你希望阅读中文版本的RFC，请查看我们的[RFC中文翻译项目](rfcs-zh/README.md)及[翻译进度](rfcs-zh/翻译进度.md) 