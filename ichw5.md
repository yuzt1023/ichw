问题1.北京大学某单位的某台机器IP地址为162.105.80.160, 子网掩码为255.255.255.192，
1) 该单位的网络号(网络+子网)是多少？
答：10100010.01101001.01010000.10000000
2) 该单位理论上可容纳多少主机？
答：1024
3) 北大可以有多少个这样的子网(假定北大全部是162.105网段)？
答：64
问题2.解释TCP协议建立连接为什么设计为三步握手（3-way handshake）？
答：信道是不可靠的，但是我们要建立可靠的连接发送可靠的数据，也就是数据传输是需要可靠的。在这个时候三次握手是一个理论上的最小值，并不是说是tcp协议要求的，而是为了满足在不可靠的信道上传输可靠的数据所要求的。
问题3.有哪些恶意软件, 如何防范恶意软件？
答：计算机病毒，蠕虫，木马，间谍软件，广告软件，zombie
防范：
安装杀毒软件/安全防护软件, 及时打补丁
使用防火墙, 禁止外部计算机通过网络访问本机
不随便下载运行可执行程序
不打开未知的邮件附件
U 盘 通常带毒, 打开前要先查毒
不随便暴露自己的 email、生日、手机等重要信息
不以 Administrator 权限操作计算机
