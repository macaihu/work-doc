
# 电梯程序在pc上进行升级
sshpass -p keep0It3 scp  -P 8357 images/elevator/elevator_v1.00.zip root@192.168.0.2:/tmp/
sshpass -p keep0It3 ssh root@192.168.0.2 -p 8357 "/etc/init.d/rc.update /tmp/elevator_v1.00.zip"
sshpass -p keep0It3 ssh root@192.168.0.2 -p 8357 "reboot"


# tz8135命令升级:

mount -t nfs 192.168.0.50:/opt/work/ /mnt/nfs --nolock

mount -t nfs 192.168.19.199:/opt/work/ /mnt/nfs --nolock

奥远电梯:
cd /mnt/nfs/gm8136s/images/elevator/
ps | grep rc.onenet | grep -v grep | awk '{print $1}' | xargs kill -9
killall tzvideo
flashcp -v rootfs-cpio_master.squashfs.img /dev/mtd2
flashcp -v uImage /dev/mtd1



tz8135
cd /mnt/nfs/gm8136s/images/tz8135/
flashcp -v rootfs-cpio_master.squashfs.img /dev/mtd2
flashcp -v uImage /dev/mtd1
flashcp -v u-boot.bin /dev/mtd0




# tz8138 sd卡升级命令:

kernel:
mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 uImage
sf probe 0; sf erase 0x60000 ${filesize}; sf write 0x2000000 0x60000 ${filesize};

文件系统:
mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 rootfs-cpio_master.squashfs.img
sf probe 0; sf erase 0x260000 ${filesize}; sf write 0x2000000 0x260000 ${filesize};


全部flash
mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 tz8135.bin
sf probe 0; sf erase 0x0 ${filesize}; sf write 0x2000000 0x0 ${filesize};

mw.b 0x2000000 0xFF 0x800000　;fatload mmc 0 0x02000000 elevator.bin
sf probe 0; sf erase 0x0 ${filesize}; sf write 0x2000000 0x0 ${filesize};




# 从串口使用uboot升级

1. 先配置本机器IP，和server IP。

setenv ipaddr 192.168.19.33 ;setenv serverip 192.168.19.199

2. 更新内核

mw.b 0x2000000 0xFF 0x800000;tftpboot 0x02000000 uImage_8136; sf probe 0; sf erase 0x60000 0x2a0000; sf write 0x2000000 0x60000 0x2a0000;

3. 更新文件系统

mw.b 0x2000000 0xFF 0x800000; tftpboot 0x02000000 rootfs-cpio_master.squashfs.img;sf probe 0; sf erase 0x300000 0x200000; sf write 0x2000000 0x300000 0x200000;

4. 更新user分区

mw.b 0x2000000 0xFF 0x800000;tftpboot 0x02000000 GM8135_2MP.SPI.jffs2.img; sf probe 0; sf erase 0xe00000 0x100000; sf write 0x2000000 0xe00000 0x100000;

或者 
1. 更新全部
mw.b 0x2000000 0xFF 0x800000;tftpboot 0x02000000 tz8135.bin; sf probe 0; sf erase 0x0 ${filesize}; sf write 0x2000000 0x0 ${filesize};
