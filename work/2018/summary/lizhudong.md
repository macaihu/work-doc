M60	移植测试sipalg。
	解决库尔德机型外放声音小，回声底噪大问题。
FON	增加EAP功能。
	分析rtl驱动、授权程序、eap协议、radius协议，验证解决连接不稳定容易掉线问题。
	梳理hotspotd内存使用，解决容易崩溃问题，并使用父子进程监控彻底解决崩溃后马上复位问题。
	监控4G网络变化，修复wifi复位丢失路由网关和加密方式问题。
P21K	移植libosip和siproxd到zte平台，并编写对应nv参数转换工具。
	打开SPI框架并实现slic驱动。
	修改原版ccapp电话程序各种问题，增加digit_map，三方通话，会议，前转，回环等功能。
	修正tr069远程升级问题。
GPON	分析数据库、中间层、网页各层框架和修改方式，使我们可以实现3BB的新增功能。
	加入tr069必测项目。
	DDNS增加yaddns和other功能。
	实现IPv6的ACL和Filter功能。
	扩展网络服务端增加网页通过本地磁盘保存和恢复系统配置功能。
	定位内存泄漏点。
	5G wifi增加自动信道范围限制。

