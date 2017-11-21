# [GM8136_3DNR_User_Guide_V1.1.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_3DNR_User_Guide_V1.1.pdf)

3dnr: 3d降噪

使用ft3nr200.ko这个模块, 源码在arm-linux-3.3.\module\中, 可以编译了. 由于各个模块联系看起来非常紧密, 貌似不容易把它单独卸载掉.

这个ko在target/lib/modules目录中, 加载这个模块后:

``` 
#cat /proc/thdnr200/dma/param   
 === DMA Parameter ===  
 [00]WC_WAIT_VALUE (0x0~0xffff) : 0x0  
 [01]RC_WAIT_VALUE (0x0~0xffff) : 0x0  
```
不知道这些值的含义.

可以使用:```insmod ft3dnr200.ko max_minors=16``` 进行参数指定加载. 有个这样的说明:  
> For example, users need the driver to provide one channel of 2M resolution, one channel of VGA resolution,
and one channel of CIF resolution:  
> insmod ft3dnr200.ko res_cfg="2M/1,VGA/1,CIF/1"  

实际上参考板中使用的命令是:  
```
/sbin/insmod /lib/modules/ft3dnr200.ko src_yc_swap=1 dst_yc_swap=1 ref_yc_swap=1
```
显然这里没有设置什么resolution之类的东西, 那么文档里面继续说:  
> If this parameter is not specified, the default value will be extracted from the middleware configuration file,
“gmlib.cfg”, under the [ENCODE_DIDN] section.

这个gmlib.cfg文件, 在参考板上, 存在于/mnt/mtd目录中, 可以修改, 其中 [ENCODE_DIDN] 内容是这样的:
> [ENCODE_DIDN]          
> ; CONFIG1 = resolution_keywords/channels/total_fps/ddr_channel, ...   
> CONFIG1 = 2M/1/30/0  

把这里的30改为25, rtspd跑的仍然是30.   



# [GM8136_AES_DES_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_AES_DES_User_Guide_V1.0.pdf)

AES: The Advanced Encryption Standard (AES)  
DES: Data Encryption Standard (DES)  
这不是数据加密么, 和摄像头有什么关系?
>The AES-DES cipher coprocessor provides an efficient hardware implementation of the DES/Triple-DES/AES algorithm for the high-performance encryption and decryption, which can be applied to various applications

这样看起来, 这个cpu提供硬件的DES/AES算法, 估计是这两种算法比较耗cpu, 干脆来个硬件来处理? 不过参考板上貌似没有这个ko呢.

可以编译通过啦:
/tmp # insmod aes_des.ko
Register AES/DES...OK
/tmp # ls /dev/security  -l
crw-rw----    1 root     root       10,  57 Jan  2 22:16 /dev/security

例子程序就以后再搞吧.






```
├── GM8136_Audio_System_Programming_Guide.pdf
├── GM8136_Capture_User_Guide_V1.0.pdf
├── GM8136_Flash_User_Guide_V1.0.pdf
├── GM8136_Frammap_User_Guide_V1.0.pdf
├── GM8136_GM2D_User_Guide_V1.0.pdf
├── GM8136_GM8136S_EVB_User_Guide_V1.0.pdf
├── GM8136_GMAC_User_Guide_V1.0.pdf
├── GM8136_GPIO_User_Guide_V1.0.pdf
├── GM8136_H264_Encoder_User_Guide_V1.0.pdf
├── GM8136_Hardware_Design_User_Guide_v0.1.pdf
├── GM8136_IRDA_User_Guide_V1.0.pdf
├── GM8136 ISP Tuning Tool User Guide_v1.2.pdf
├── GM8136_IVS_User_Guide_V1.0.pdf
├── GM8136_LCD_User_Guide_V1.0.pdf
├── GM8136 Linux User Guide_V1.1.pdf
├── GM8136_Motion_Detection_Programming_Guide_V1.0.pdf
├── GM8136_OSG_User_Guide_V1.0.pdf
├── GM8136_Quick_Start_V1.1.pdf
├── GM8136_RTC_User_Guide_V1.0.pdf
├── GM8136_SAR_ADC_User_Guide_V1.0.pdf
├── GM8136_scaler_User_Guide_v1.0.pdf
├── GM8136_SD_Card_User_Guide_V1.0.pdf
├── GM8136S_GM8135_Product_Brief_V1.0.pdf
├── GM8136S_GM8135S_Data_Sheet_V0.3.pdf
├── GM8136S_GM8135S_Data_Sheet_V0.8.pdf
├── GM8136S_GM8135S_Data_Sheet_V0.9.pdf
├── GM8136_SPI_User_Guide_V1.0.pdf
├── GM8136 U-BOOT User Guide_v1.3.pdf
├── GM8136_USB_OTG_User_Guide_V1.1.pdf
├── GM8136_Watchdog_User_Guide_V1.0.pdf
├── GMLIBv2_IPcam_Sample_Code_V0.3.chm
├── GMLIBv2_Programming_Guide _V1.2.pdf
├── H264_Rate_Control_User_Guide_V1.0.pdf
├── H264中文规范.pdf
├── hemu
│   ├── 中移物联网“和目”视频监控技术规范1.0_20170810.docx
│   ├── 和目云平台接入文档2017.pdf
│   └── 和目智能摄像头技术规范书Build0914_0912（含测试方案）.docx
├── How to reduce the power consumption (GM8136S_35S)_ENG.pdf
├── How to reduce the power consumption (GM8136S_35S).pdf
├── http接入协议.pdf
├── onenet
│   └── OneNet云.pdf
├── ONVIF2.0协议珍藏版.docx
├── onvif_client_demo_src.bz2
├── ONVIF_Device_TestTool_v.14.06.zip
├── other_ic
│   └── BL-7601MU2 Product Specification V3.（70002052） .pdf
├── OV9712 Rev1D  Conversion support data (for PCN, 9-10-2013).pdf
├── RTSP_Over_HTTP.pdf
├── w25q128fv datasheet.pdf
├── 中移TCP透传.pdf
└── 电路原理图.pdf
```
3 directories, 52 files
