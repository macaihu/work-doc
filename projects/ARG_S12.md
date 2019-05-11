
#### 2019.05.10
**刘云** 代理商反馈他们他们工具使用的是C#.net,调用C/C++动态库的可能存在的风险还需要赵金评估下。
**吴曦**发出的工作任务 其中snmp和tr069的支持所有节点比较费时，bridge模式和bcp有困难。<hide>
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