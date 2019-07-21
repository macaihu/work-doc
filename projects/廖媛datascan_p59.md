
#### 2019.07.19
**喻潇**  皮晓聪使用的机器在深圳也会出现过一段时间不能使用的情况。
#### 2019.07.16
**皮晓聪**  解决了MC7455模块一些bug，发现一些新bug这周需要修复。（预估3天）
#### 2019.07.11
**皮晓聪**  修复使用BM816,BM817C,MC7455模块时网页上无法配置PIN码问题  
4G拨号会断开，程序没有重新去拨号和获取地址。
#### 2019.07.10
**皮晓聪**  mc7455看起来只有一个串口可以发送at。
#### 2019.07.09
**赵金**  imei只能写一次。
**Vince Lai**  查詢不到pin和puk可輸入剩餘次數，我會請教原廠是否有支持 請試試看AT+CPINR
**皮晓聪**  P59更新版本为V4.1.16。           Sierra wireless 的MC7455模块测试。<hide>  
- apps/dialtool2:MC7455模块查询PIN和PUK剩余输入次数  (PiXiaocong)
- 修复使用MC7455模块时WEB页面PIN码配置失败或无响应问题  (PiXiaocong)
- 修复WEB页面设置频带响应慢或有时不响应问题  (PiXiaocong)
</hide>
#### 2019.07.08
**皮晓聪**  P59更新版本为V4.1.15。Sierra wireless 的MC7455模块测试。<hide>
- apps/dialtool2:修复MC7455模块有时获取IMSI失败造成无法注册网络问题 (PiXiaocong)
- apps/dialtool2:修复使用MC7455模块时未查询当前已锁定判断信息 (PiXiaocong)
- cmdlib: 上传一个单独调试cmdlib的c文件（如果cmdlib接口有问题，可以直接用此文件使用gdb进行单步调试） (renyinshan)
- document: 上传一份P5x GDB调试的文档说明 (renyinshan)
- gdb: Add installgdbserver directory to .gitignore (renyinshan)
- Modem Log： 底层脚本增加启动判断（支持直接编译到系统和临时上传） (renyinshan)
- cmdlib: 增加bmlogproxy是否运行的判断，如果是临时上传的，则需要增加/tmp/bmlogproxy的判断（底层接口判断比较严谨） (renyinshan)
- web[Modem Log]: 解决开启log提示失败的错误。（响应太快，cgi还没收到判断结果） (renyinshan)
- Modem Log： 增加抓取宽翼模块log的底层脚本，供网页调用。（至此，此功能在管理页面和普通页面都可正常工作） (renyinshan)
- web [Modem Log]: 普通页面增加抓取模块log的功能 (renyinshan)
- cmdlib: 增加抓取宽翼模块log的代理程序"bmlogproxy"是否运行的判断。 (renyinshan)
- apps/switchwan:修复WAN模式为doublewiredlte模式时由于有些LTE模块网络接口不为usb0没有删除多出默认路由而无法上网问题 (PiXiaocong)
- P59:修复WAN模式切换到singlewan模式时由于有些LTE模块网络接口不为usb0造成无法添加默认路由问题 (PiXiaocong)
- apps/dialtool2:输出当前LTE模块网络接口名称到/tmp/.system_info_static文件 (PiXiaocong)
- 修复使用BM816模块(网络接口为wwan0)WEB页面不显示4G网口信息问题 (PiXiaocong)
- apps/dialtool2:增加P59(TZ7.823.317板型)支持BM816模块处理 (PiXiaocong)
- 添加BM816模块驱动 (PiXiaocong)
- bmlogproxy: Fix a build error. (renyinshan)
- .gitignore: 增加build_dir到.gitignore文件中 (renyinshan)
- bmlogproxy: 增加宽翼模块的抓包工具bmlogproxy. 并更新一个比较通用的Makefile，以后新增加的app可以以此来参考 (renyinshan)
- compile.mk: 增加一个编译app所需的mk文件 (renyinshan)
</hide>

#### 2019.07.05
**喻潇**  PIN菜单编辑PIN然后点OK，和锁频菜单点Set Bands；这两个菜单没反应；
#### 2019.07.02
**皮晓聪**  tzgap_P59_4.1.14.zip版本 Sierra wireless 的MC7455模块支持已添加请测试。<hide>
- P59:Release P59 V4.1.14  <PiXiaocong>
- apps/dialtool2:MC7455模块暂不启用GPS,以修复启用GPS后MC7455模块初始化失败问题  (PiXiaocong)
- apps/dialtool2:修复不能配置MC7455模块工作在3G网络和4G模式时无法获取信号强度问题 (PiXiaocong)
- P53: 内核支持MC74xx模块 <CONFIG_4G_MODULE_MC74xx=m>  (renyinshan)
- version: 解决version文件中os参数为空的bug.  (renyinshan)
- P59: 解决新拉的仓，直接编译6 or 8 报错的问题，需要一个mkimage工具，原来是从boot代码中生成的（只用此工具，其他不用） (renyinshan)
</hide>
#### 2019.07.01
**Vince Lai**  AT!SELRAT=? 可搜尋模塊支持的設置 AT!SELRAT=00    範例:該指令設置為AUTO
#### 2019.06.26
**皮晓聪**  插入SIM后发相关的AT指令无法拨号获取网络地址。
Vince Lai  使用AT命令操作可以但未來原廠不提供技術支持
#### 2019.06.25
Vince Lai（Nexcomm）eth2/eth3即為模塊枚舉出來的網絡接口,是正確可用的。
#### 2019.06.21
**王松勇**  来公司。原来是代理西门子模块的。  
Sierra Wireless 模块在欧美还有非常大的市场。有cat12的版本。价格能比移远贵1倍。  
映翰通等有采用Sierra Wireless的模块，产线在深圳。  
金雅拓原来收购了西门子的模块。
**廖媛**  模块发给皮晓聪。
#### 2019.06.17
**王松勇**  发出at命令集，linux驱动，编程指南等。样品模块需要购买。
**廖媛**  认证费再和Kevin谈。
#### 2019.06.16
**王松勇**  发了EM7455與MC7455的规格书。7455 基于mdm9230. lte  3GPP Release 11 UMTS • 3GPP Release 9
#### 2019.06.14
**Kevin Arnold** Datascan agrees to pay the $5000.00 USD NRE charge for integrating the MC7455 into your router. 
#### 2019.06.13
**Kevin Arnold**  shooting for a $135 price point for the EM7455
**廖媛**  Sierra Wireless 报价80美金。
#### 2019.06.10
**Kevin Arnold**  不需要千兆口。
#### 2019.06.06
**Kevin Arnold**  想用Sierra Wireless MC 7455
#### 2019.05.21
**廖媛**  Kevin没有正式确认使用sierra wireless。
#### 2019.05.21
**廖媛** 已签ucloudlink的nda。
#### 2019.05.20
**廖媛**  发出询问邮件，问kevin的选择。
#### 2019.05.16
**郑欧？** ucloudlink公司的人过来，它们主要是提供mifi的租赁公司，和实际上许多的运营商谈好了资费，自己有一套“云sim”系统，根据落地不同，自动换成当地运营商运营。它们的品牌是“漫游超人”。他们提供的模块并是ap测的usb接口和我们通讯, 不提供软件接口，无法查询到上网状体，信号强度等信息。无法向我们报价，因为已经给kevin报价。  
**廖媛**  发出邮件，p59无模块报价70$
#### 2019.05.14
**廖媛**  约ucloudlink的人周四来公司。
#### 2019.05.13
**Kevin Arnold** ucloudlink会直接给他们报价，可能会使用sierra wireless，便宜一些。
#### 2019.05.08
**廖媛**  ucloudlink的模块没有做att的认证。
#### 2019.05.07
**Kevin Arnold**  仍然希望考虑sierra wireless 和ucloudlink.  
#### 2019.05.06
**廖媛**    Sierra wireless module is good ,but very expensive .  we donn't suggest it .

