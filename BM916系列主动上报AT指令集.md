# BroadMobi BM916 系列主动上报AT指令

## 1 系统模式变化指示：^MODE
^MODE:<sys_mode>

参数
<sys_mode>
0  无服务
2  CDMA模式
3  GSM/GPRS模式
4  HDR模式
5  WCDMA模式
8  CDMA HDR混合模式
9  LTE模式

## 2、SIM卡状态变化指示
+SIM:Removed、+SIM: Inserted
## 3、来电提示RING
## 4、电话接通提示CONNECT
## 5、呼叫挂断上报信息指令+DISC
+DISC:<id>,<idr>,<mode>,<cause>,<number>,<num_type>,[<alpha_text>];

参数
<id>链路Id

<idr>呼叫方向
0 发起的呼叫
1 呼入的呼叫

<mode>呼叫类型
0 语音
1 CS Data
2 PS Data
3 SMS

<cause code>挂断原因，具体<cause code>参考协议GSM 04.08和表21

<number>呼叫号码
<num_type>号码类型
<alpha_text>号码在电话本中的text字符串

##  6、新短信状态报告到达指示：+CDSI或+CDS
该指令是非请求指令，显示有一个新的短信状态报告，并指示存储位置
当cnmi的<ds>为2时，采用+CDSI上报，上报形式为：
+CDSI:<mem>,<index>
当cnmi的<ds>为1时，采用+CDS上报，上报形式为：
+CDS: <fo>,<mr>,<ra>,<tora>,<scts>,<dt>,<st>
<scts>Timestamp
<dt>discharge_time
<st>:tp_status

参数
<mem>
"SM"  UIM
"ME"  NV

<index>十进制整数，表示短信状态报告在存储中的位置，即索引值

##  7、短信存储介质满上报指令：^SMMEMFULL
^SMMEMFULL: <mem_type>

当机卡一体机短信满时的提示
^SMMEMFULL: MEM
当机卡分离机短信满时的提示
^SMMEMFULL: SM

## 8、短信到达指示：+CMTI
新短信提示
+CMTI: <mem>,<index>

参数
<mem>"SM"  UIM
"ME"  NV

<index>在存储中的位置，即索引值

## 9、新短信直接上报指示：+CMT
在某些情况下，新短信会用+CMT直接上报。比如当QCNMI参数mt=2，mode=2。具体请参考 8.3 AT$QCNMI。
+CMT：<oa>,,<scts>,[<tooa>,<fo>,<pid>,<dcs>,<sca>,<tosca>,<length>,]<msg>

## 10 连接成功指示命令：MIPACCEPT
+ MIPACCEPT: <server_id>,<client_id>,<client_ip>,<client_port>

仅TCP连接时提供上报功能
参数：
<server_id>表示需要建立server的ID号，取值：1-4
< client_id >  client的ID号(1-3)  每个server最大支持3个client
<client_ip>   client的IP地址
<port>   client的端口号

## 11 TCP接收数据上报：MIPRTCP
+ MIPRTCP: <server_id>,<number>,<data>

TCP接收数据时的上报
参数：
<server_id>表示需要建立server的ID号，取值1-4
<number>取值：0-1460  本次接收的字符个数
<data>本次接收的数据内容，字符型，长度为<number>

## 12 UDP接收数据上报：MIPRUDP
+ MIPRUDP: <server_id>,<ip>,<port>,<data>

UDP接收数据时的上报
参数：
<server_id>取值：0   连接ID
<ip>server的ip地址
<port>取值：0-65535server侧的端口号
<data>本次接收的数据内容，字符型，长度为<number>

## 13 SERVER接收数据上报：MIPSERVER
+ MIPRUDP: <server_id>,<client_id>,<data_len>,<data>

SERVER接收数据时的上报
参数：
<server_id>表示需要建立server的ID号，取值：1-4
<client_id>  client的ID号(1-3)  每个server最大支持3个client
<data_len>收到的数据长度
<data>本次接收的数据内容，字符型，长度为<number>

## 14 TCP链接断开提示
+MIPSTATUS: TCP <socket_id > DISCONNECT

## 15 server TCP链接断开提示
+MIPSERVER DISCONNECT <server_id > <socket_id>

## 16 HTTP服务器交互内容主动上报：+HTTPREAD
+HTTPREAD：data_len, content

## 17 TTS播报以及播报结束主动上报：+BMTTS：END
+BMTTS：END 语音播报结束

AT+BMCMD=BMTTS,0，"1234567"OK
+ BMTTS: END 
注：AT+BMCMD=BMTTS ,<coding>,"string"
coding：0 -- 英文字符
coding：6-- UTF-8

##  18上位机主动下发升级命令 :^FTPST
^FTPST：上报升级状态

AT+BMCMD=UPGRADE, <path>,<type> 开始升级备份分区
参数：<path> 模块升级包路径
      <type> 升级包类型 1-全量 2-差分
执行 AT+BMCMD=UPGRADE 命令升级此新版本,模块返回 OK。
主动上报^FTPST:50 后开始升级备份分区 
若升级成功，上报 ^FTPST: 60，升级失败，上报 ^FTPST: 80

上报状态描述： -1 无效状态，未执行过升级操作 
10 空闲状态 
42 升级包完整性校验失败 
45 升级包完整性校验成功 
50 收到升级命令，模块进入升级状态 
60 升级备份分区完成 
80 升级失败 
90 升级成功



