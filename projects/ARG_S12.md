
#### 2019.05.20
**刘云**  发了个测试DLL库给代理商验证，发现他的64位系统调用我们的32位DLL库有报错，建议客户自己上网找下设置方法。应该是c#中的设置问题。
#### 2019.05.13
**刘云** 产测工具的API C++动态库已通知赵金开始做。下午晚些时候收到运营商正式邮件确认1.05版本可用于第一批供货。
#### 2019.05.12
**刘云** 今天去运营商测试，现场解决他们测试发现的问题，吴曦，向杰在国内支持<hide>
1，解决他们手上那台设备升级1.04程序后admin账户下还是会显示升级程序和配置菜单的问题，有个user_hide属性项最后的配置删掉了，我手里的那台机器因为之前升级过带此配置项的配置所以隐藏了，重新做了个新配置解决。
2，解决ACS服务器打开WAN口HTTP访问后，HTTP不能正常访问的问题，之前的做法是打开后还需要配置白名单IP访问，这边无此要求，修改为打开后直接访问即可。
3，隐藏admin账户下的访问控制菜单，只在Root账户下可见。
4，修改CellId上报形式,改为小区ID和基站ID分别上报。
明天测试计划：
明天运营商计划细测下DMZ和端口转发功能，看看代理商那边是否能约上直接过去蹲着。
WIFI测试：
另外，今天和宽兆的设备对比测试了下WIFI，在他那个环境下测试了近距离（1-2m）和中距离(12-13m,),近距离我们的数据没问题，中距离，最大速率和宽兆差不多都能达到8,9M，但是我们最小值低到零点几M，宽兆的最小也到两点几M，平均速度测下来宽兆有5M多，我们的只有2M多。同样的信道下测试了都在信道1和信道6，两者测试环境都是一样的，唯一不同的就是不是同一时间一起测试，但是连着的时间换了先后顺序测试了几次测试，结果平均速率确实是比宽兆的差。
</hide>
#### 2019.05.10
**刘云** 代理商反馈他们他们工具使用的是C#.net,调用C/C++动态库的可能存在的风险还需要赵金评估下。
**吴曦** 发出的工作任务 其中snmp和tr069的支持所有节点比较费时，bridge模式和bcp有困难。<hide>
工作任务|计划完成时间|人员
-------|---------|----
注网模式添加FDD优先|2019-05-11|吴曦，向杰
多个不同界面和功能需求的程序和配置|待定，等具体需求明确|向杰，占永平
SNMP MIB文件节点名称又mci改为MOBINNET，流量统计和速率等单位由b改为B|2019-05-10|余辉
配置控制去掉usb功能|2019-05-13|吴曦
默认修改为网口抓包模式|2019-05-13|吴曦
Idle mode 确认是否支持|2019-05-15|余小虎
Change timing value standard 3gpp to 1 minutes,some timer are 12 hours,12 min or 54 min，需要与原厂确认|2019-05-20|余小虎，吴曦
SNMP支持所有客户要求节点|2019-05-22|余辉，汪光华
手动搜网，搜索出周边所有基站信息|2019-05-25|吴曦，向杰
Bridge mode（必须支持，L2TP的BCP功能需要用到）|2019-05-22|汪光华，吴曦
VPN添加PPTP和L2TP的BCP功能|2019-05-30|汪光华，吴曦
tr069所有节点，具体对照表格|2019-05-30|向杰，余辉，吴曦，汪光华
提供wifi修改了WPA2漏洞的证明材料|2019-05-15|余小虎，吴曦
提供菲律宾除网页扫描工具的其他安全测试软件|2019-05-30|占永平
V3调试新的switch和slic驱动|1900-01-00|吴曦
V3E调试slic驱动|1900-01-00|汪光华
V3E添加LAN/WAN切换，支持PPPOE功能等|1900-01-00|余辉，吴曦
V3E去射频nv的网页升级，目前中兴微还在开发阶段|1900-01-00|吴曦，汪光华
菲律宾LT90、P25M，巴基斯坦P21K，兰卡S10，尼日利亚S10等其他小需求|1900-01-00|全体
</hide>
#### 2019.05.09
**刘云** PCB的layout和原理图先发给代理商了，源代码处理下再交付（跟进度）。
#### 2019.05.04
**刘云** 今天去运营商那边测试TR069和SNMP，TR069目前优先级最高，需要及时修改的地方已邮件反馈给周湘里，SNMP测试的时间少，暂时发现的问题已反馈给光华。<font color=red>可能不是需要l2tp v3。</font><hide>

Actually the requirement is to allow the L2 traffic coming from CPE LAN interface to be passed to a system that resides in Core network like BRAS. Also, BRAS should send L2 traffic to other network like Customer HQ. we did the test with KZtech AM3100V that you can check the attached file about instruction CPE configuration, I can prepare a sample of AM3100V for your test but need to officially email.
 
A more complete description that:
What we need from layer2 L2TP in CPE is the functionality called BCP (Bridging Control Protocol). This function allows L2 frames generated from devices connected to CPE LAN to be transported over L2TP tunnel transparently. So, the broadcast domain will be extended from CPE LAN side to WAN side over L2TP tunnel and HQ.
 
 
    1.         About Bridge We just do it L2 traffic coming from CPE LAN interface.
    2.         Reduce the Max time of retry connection’s institution (Reduce connection time)
    3.         LTE reconnect issue effect on L2TP re-establish (if for any reason CPE drops and back to the network, there would be no worry whether L2TP BCP can establish)
    4.         Provide MTU size button for L2TP layer2 BCP because some banks have software with difference MTU sizes for connection 
</hide>