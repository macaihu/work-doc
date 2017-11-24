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


# [GM8136_Audio_System_Programming_Guide.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_Audio_System_Programming_Guide.pdf)

声音系统有4部分工作:
1. i2s pmu 设置
2. 音频解码器寄存器设置
3. 旁路功能(bypass function ???)和/proc信息
4. 音频驱动编程.

在sdk源码中, 目录是module/front_end

有两个ko, fe_common.ko 前端(front end)核心, 包括ssp pmu设置. decoder.ko, 解码器核心, 包括视频音频寄存器设置.

module/front_end这个目录里面的文件看起来很多的样子.

编译这个目录中会出现好多个ko, 包括fe_common.ko和decoder.ko, 不过在卡片机上lsmod看起来没有加载decoder.ko.
卡片机/proc目录中没有adda320这个目录, 不过有个比较像的, adda308, 

	cat /proc/adda308/SPV 
	SPV should be between 0 ~ 3(0db ~ 1.5db)
	current SPV = 0

文档继续讲到audio_drv.ko这个, front_end编译出来的ko中, 不包含这个ko. 卡片机中存在, 并已经加载.

加载的方式和文档中一样:

    insmod audio_drv.ko audio_ssp_num=0,1 audio_ssp_chan=1,1 bit_clock=400000,400000 sample_rate=8000,8000 audio_out_enable=1,0


# [GM8136_Capture_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_Capture_User_Guide_V1.0.pdf)

FTVCAP300从不同的图像接口捕获图像, 从AMBA AXI输出到内存中. 提供两个视频输入接口, 一个支持ITU-R BT.656, BT.1120, and BT.601格式, 另外一个只支持isp数据格式(这些格式是啥?). 两个通道都可以输出4个resolution. OSD可以在输出视频中增加任何文字. 掩码功能可以增加水印和log. 运动检查功能适用于监视系统.

支持图形裁剪功能. 每个通道有源裁剪和目标裁剪. 可以通过中间件进行设置.

FTVCAP300支持拉伸功能.

FTVCAP300每个通道支持8个掩码窗口, 支持16个可编程的调色板颜色. 

FTVCAP300每个通道支持8个osd窗口, osd字体是12x18.

FTVCAP300运行检查支持128x128个区域. 支持以下参数的设置:

Parameter      | Description
---------------|-------------
alpha          | Control the updated speed of the MD model, if the luminance variance of background is significant, users should select bigger value for alpha. 
tb             | Decide if this MB belongs to the background or foreground, small value of tb with sensitive MD 
sigma          | Control the noise tolerance ability of the MD model, large value with strong noise tolerance ability 
alpha accuracy | Control the update speed of the MD weight, alpha accuracy with large value increases the update speed of the MD weight which can increase the model update speed when the background is changed. The value of the alpha accuracy is formulated as A * 8191, users can choose the suitable value for variable A.
tg             | Decide if this MB belongs to the background or foreground, the value of tg must be the same as tb.

FTVCAP300的源码在module/vcap300中, 编译完也是大量的ko在其中. 编译出来的ko都以 vcap300开头, 卡片机上的三个都在目录中:

    [root@GM]# ls vcap* -l
    -rw-r--r--    1 root     root          6508 Oct 15 20:24 vcap0.ko
    -rw-r--r--    1 root     root        362716 Oct 15 20:24 vcap300_common.ko
    -rw-r--r--    1 root     root         12444 Oct 15 20:24 vcap300_isp.ko

下面的大量篇幅是各种ko的参数说明, 先跳过不看吧.

	#cat /proc/vcap300/version
	Version: 0.3.12

```
[root@GM]# cat /proc/vcap300/vcap0/ability
HW_Version         : 20140311
HW_Revision        : 000
VI_Count           : 1
Cascade_Count      : 1
Mask_Win_Count     : 8
OSD_Win_Count      : 8
Mark_Win_Count     : 4
Scaler_Count       : 4
Scaler_Ability_UP  : Yes Yes Yes No 
Scaler_Ability_DOWN: Yes Yes Yes No 
FCS_Support        : Yes
Denoise_Support    : Yes
Sharpness_Support  : Yes
VI_MD_Win_X_Num    : 0 127 
MD_IMG_SRC         : TC_Out
TC_X_Align         : 2
OSD_Border_Pixel   : 2
OSD_Frame_Mode     : Yes
OSD_Edge_Smooth    : Yes
OSD_Color_Scheme   : Yes
Real_Time_CH       : Yes
```

在使用rtspd和vlc看视频的情况下:
```
[root@GM]# cat /proc/vcap300/vcap0/status
Dev      VI#        CH#        P0     P1     P2     P3
--------------------------------------------------------
(START )
         0(IDLE  )  0(IDLE  )  IDLE   IDLE   IDLE   IDLE  
                    1(IDLE  )  IDLE   IDLE   IDLE   IDLE  
                    2(IDLE  )  IDLE   IDLE   IDLE   IDLE  
                    3(IDLE  )  IDLE   IDLE   IDLE   IDLE  
         1(START )  0(START )  START  START  IDLE   IDLE


[root@GM]# cat /proc/vcap300/vcap0/vg_info
|VCH#  VCAP_CH#  #Split  #Path  VI_Mode  FD_Start    Resolution  VLOS  FPS_C  FPS_M  Interface  
|-----------------------------------------------------------------------------------------------
 0     4         0       4      0        0x10000400  1280x720    No    25     25     isp  


[root@GM]# cat /proc/vcap300/input_module/table
|VI#    Name             Type       Interface      Resolution    FPS_C   FPS_M   XCAP#
|=======================================================================================
1      isp              isp        isp            1280x720      25      25      ISP  


```

然后又是一堆驱动的节点说明...


# [GM8136_Flash_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_Flash_User_Guide_V1.0.pdf)

gm8136有4个跳针, spi boot还是nand boot, spi 或spi-nand , spi 3/4字节模式, 固件升级模式, 当跳到固件升级模式的时候, 可以从pc上使用usb口进行升级.

如果要修改flash的分区信息, 应该要改这个文件:linux-3.3-fa/drivers/mtd/devices/spi_flash.c

```
search "partition_check" string, and set these definition direcly at this API function.
For example:
partitions[0].name = "abc";
partitions[0].offset = 0x140000;
partitions[0].size = 0x200000;
```

对于jff2的文件, 可以修改里面的内容:

```
# losetup /dev/loop0 xxx.jffs2.img
# modprobe block2mtd block2mtd=/dev/loop0
# modprobe mtdblock
# mount -t jffs2 -o ro /dev/mtdblock0 mnt
```

不过我们从来不去编辑里面的内容, 从来都是编译的方式使用mkfs.jff2这个工具做出来.

# [GM8136_Frammap_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_Frammap_User_Guide_V1.0.pdf)

当内核模块需要申请内存时, 一般用alloc_pages或者kmalloc, 这样做有两个问题, 一个是著名的内存碎片问题, 一个是内核的内存申请上限问题. 另外, ddr的带宽也是一个重要的限制因素, 比如两个ip使用同样的ddr通道时(为啥会有这样的情况?)

FRAMMAP 有如下功能.....

在卡片机中, 只是简单的加载了模块:
/sbin/insmod /lib/modules/frammap.ko

```
[root@GM]# cat /proc/frammap/ddr_info 
----------------------------------------------------------------
ddr name: frammap0 
base: 0x3000000 
end: 0x43b2000 
size: 0x13b2000 bytes
memory allocated: 0x13b2000 bytes 
memory free: 0x0 bytes 
max available slice: 0x0 bytes
memory allocate count: 24 
clear address: 0x43b2000 
dirty pages: 5042 
clear pages: 0 
size alignment: 0x1000 
```

frammap源码module/frammp中, 编译出frammap.ko, 只有1个c文件.


# [GM8136_GM2D_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_GM2D_User_Guide_V1.0.pdf)

2D computer Graphics accelerator Engine 图像加速引擎.

感觉可以不要, 摄像头设备一般情况是没有显示设备的. 不过卡片机中加载了这个模块.

源码在module/ft2dge目录中, 编译出ft2dge.ko

# [GM8136_GM8136S_EVB_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_GM8136S_EVB_User_Guide_V1.0.pdf)

参考板指南

跳针的含义:
Pin                                             |  No. Signal Name
------------------------------------------------|----------------------
JP0 (Internal pull-low)/JP1 (Internal pull-low) | PLL1 setting
JP6                                             | Firmware update mode
JP7 (Internal pull-low)                         | SPI / parallel NAND flash selection 
JP8 (Internal pull-up)                          |  Power on Heat(这个是啥?)
P19 (Internal pull-low)                         | SPI flash 3/4-byte mode selection

看起来还有一个串口, j10:UART1/RS485

要使用参考板, 必须连接串口, 号称应该使用3.3v的, 但是没有任何数据, 找个1.8v的反而可以.

    # ifconfig eth0 xxx.xxx.xxx.xxx (for example: 192.168.68.105)
    # cd /mnt/mtd
    # ./rtspd

pc端运行vlc, 打开媒体|打开网络串流.... 输入:

    rtsp://192.168.19.55/live/ch00_0

就可以看见啦, 如果要使用tcp方式, 需要点击"显示更多选项中", 在"编辑选项"的输入框中,增加" :rtsp-tcp", 注意注意注意, 要加空格.

写了可以通过usb口进行升级, 不过还没有试过.

# [GM8136_GMAC_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_GMAC_User_Guide_V1.0.pdf)

驱动文件位置:
drivers/net/Ethernet/faraday/ftgmac100.c Main program of the GMAC driver
drivers/net/Ethernet/faraday/ftgmac100.h Header file of the GMAC driver

驱动的选项

     │ │[*]   Faraday devices                                                      │ │  
     │ │     <*>     Faraday FTGMAC100 support                                     │ │  
     │ │     [*]       Enable GMAC 0                                               │ │  
     │ │     [*]         Less queue number                                         │ │  

可以使用hw指令指定mac

    # ifconfig eth0 hw ether 00:11:22:33:44:55
    # ifconfig eth0 192.168.121.139


# [GM8136_GPIO_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_GPIO_User_Guide_V1.0.pdf)

增加这个选项:

    | Symbol: GPIO_FTGPIO010 [=y]                                                             │  
    │ Type  : tristate                                                                        │  
    │ Prompt: FTGPIO010 GPIO support                                                          │  
    │   Defined at drivers/gpio/Kconfig:88                                                    │  
    │   Depends on: GPIOLIB [=y] && (ARCH_GM [=y] || ARCH_GM_DUO [=n] || ARCH_GM_SMP [=n])    │  
    │   Location:                                                                             │  
    │     -> Device Drivers                                                                   │  
    │       -> GPIO Support (GPIOLIB [=y])                                                    │   

这样表示已经有了驱动:

    [root@GM]# ls /sys/devices/platform/ftgpio010.0
    driver     gpio       modalias   subsystem  uevent

打开用户空间gpio控制:

    │ CONFIG_GPIO_SYSFS:                                                                      │  
    │                                                                                         │  
    │ Say Y here to add a sysfs interface for GPIOs.                                          │  
    │                                                                                         │  
    │ This is mostly useful to work around omissions in a system's                            │  
    │ kernel support.  Those are common in custom and semicustom                              │  
    │ hardware assembled using standard kernels with a minimum of                             │  
    │ custom patches.  In those cases, userspace code may import                              │  
    │ a given GPIO from the kernel, if no kernel driver requested it.                         │  
    │                                                                                         │  
    │ Kernel drivers may also request that a particular GPIO be                               │  
    │ exported to userspace; this can be useful when debugging.                               │  
    │                                                                                         │  
    │ Symbol: GPIO_SYSFS [=y]                                                                 │  
    │ Type  : boolean                                                                         │  
    │ Prompt: /sys/class/gpio/... (sysfs interface)                                           │  
    │   Defined at drivers/gpio/Kconfig:51                                                    │  
    │   Depends on: GPIOLIB [=y] && SYSFS [=y] && EXPERIMENTAL [=y]                           │  
    │   Location:                                                                             │  
    │     -> Device Drivers                                                                   │  
    │       -> GPIO Support (GPIOLIB [=y])                                                    │  
    │   Selected by: MACH_MIOA701 [=n] && ARCH_PXA [=n] && !ARCH_PXA_V7 [=n]                  │  

可以使用通用的方式来控制:

    [root@GM]#  ls /sys/class/gpio/
    export      gpiochip0   gpiochip32  unexport


# [GM8136_H264_Encoder_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_H264_Encoder_User_Guide_V1.0.pdf)

高性能的h264编码器......favc_enc.ko, 源码的位置有点像ftmcp300, 或者是ftmcp280?

vg_boot.sh中, 按照不同的frontend来设置h264e_max_width.

卡片机和开发板的版本看起来还有一点点区别:


    [root@GM]# cat /proc/videograph/h264e/info
    FAVC Encoder v2.0.3.1, built @ Sep 27 2016 13:59:14 (GM8136)
    module parameter
    ====================   ======
    h264e_max_width        1280
    h264e_max_height       720

    /mnt/mtd # cat /proc/videograph/h264e/info
    FAVC Encoder v2.0.2, built @ Aug 26 2016 14:20:38 (GM8136)
    module parameter
    ====================   ======
    h264e_max_width        1920
    h264e_max_height       1088

在开发板上, 一开始没有数据, 不知道是不是运行了rtspd后出现了:

    /mnt/mtd # cat /proc/videograph/h264e/chn_info
     chn    resolution   buf.type  gop   mode         fps         bitrate    max.br    init.q  min.q  max.q  qp
    =====  ============  ========  ===  ======  ===============  =========  =========  ======  =====  =====  ==
       0    1920x1088      1080P    60    CBR       900/30          8192       8192      25      20     51   27
       1     640x 480      VGA      60    CBR       900/30           512        512      25      20     51   34

在卡片机上的信息

    [root@GM]# cat /proc/videograph/h264e/chn_info
     chn    resolution   buf.type  gop   mode         fps         bitrate    max.br    init.q  min.q  max.q  qp
    =====  ============  ========  ===  ======  ===============  =========  =========  ======  =====  =====  ==
       0    1280x 720      720P     60    CBR       625/25          8192       8192      25      20     51   20
       1     640x 480      VGA      60    CBR       625/25           512        512      25      20     51   23

还有不少节点, 还完全不了解其中的含义.

# [GM8136_Hardware_Design_User_Guide_v0.1.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_Hardware_Design_User_Guide_v0.1.pdf)

硬件设计文档. 先略过.

# [GM8136_IRDA_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_IRDA_User_Guide_V1.0.pdf)

irda.ko这个文件在卡片机和开发板上都没有出现.

# [GM8136 ISP Tuning Tool User Guide_v1.2.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136 ISP Tuning Tool User Guide_v1.2.pdf)

这个看起来好复杂的样子, 调色?

# [GM8136_IVS_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_IVS_User_Guide_V1.0.pdf)


# [GM8136_LCD_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_LCD_User_Guide_V1.0.pdf)
# [GM8136 Linux User Guide_V1.1.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136 Linux User Guide_V1.1.pdf)
# [GM8136_Motion_Detection_Programming_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_Motion_Detection_Programming_Guide_V1.0.pdf)
# [GM8136_OSG_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_OSG_User_Guide_V1.0.pdf)
# [GM8136_Quick_Start_V1.1.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_Quick_Start_V1.1.pdf)
# [GM8136_RTC_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_RTC_User_Guide_V1.0.pdf)
# [GM8136_SAR_ADC_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_SAR_ADC_User_Guide_V1.0.pdf)
# [GM8136_scaler_User_Guide_v1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_scaler_User_Guide_v1.0.pdf)
# [GM8136_SD_Card_User_Guide_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136_SD_Card_User_Guide_V1.0.pdf)
# [GM8136S_GM8135_Product_Brief_V1.0.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136S_GM8135_Product_Brief_V1.0.pdf)
# [GM8136S_GM8135S_Data_Sheet_V0.3.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136S_GM8135S_Data_Sheet_V0.3.pdf)
# [GM8136S_GM8135S_Data_Sheet_V0.8.pdf](ftp://192.168.1.123/gm8136s/docs/GM8136S_GM8135S_Data_Sheet_V0.8.pdf)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)
# [](ftp://192.168.1.123/gm8136s/docs/)



```
├── 
├── 
├── 
├── 
├── 
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
