#!/bin/sh

## Value=0 -> Output to syslog, Value=1 -> Output to log file.
# TZ_LOG_OUTPUT_FLAG=0
set -x

PKG_NAME=$(basename $0)
LOG_FILE=/tmp/${PKG_NAME}.log
PID_FILE=/var/run/${PKG_NAME}.pid

# Output the log to log file.
log()
{
    time="$(cat /proc/uptime)"
    if [ "${TZ_LOG_OUTPUT_FLAG}" = "1" ]; then
        echo "[   ${time}] [rootfs] $0: $@" >> ${LOG_FILE}
    else
        logger -t "$0: " -s $@ > /dev/null 2>&1
    fi
}

default_conf()
{
    name=l2tpv3
    protocol=ip
    local_tun_id=100
    peer_tun_id=200
    local_ip=192.168.19.199
    peer_ip=192.168.1.77
    local_session_id=101
    peer_session_id=102
    mtu=1476
    local_port=5000
    peer_port=6000
    local_tun_ip=10.6.6.1/24
    peer_tun_ip=10.6.6.2/24
    default_gw_enable=0
    bridge_enable=0
}


setup_tun_ip()
{
    ip l2tp add tunnel tunnel_id ${local_tun_id} peer_tunnel_id ${peer_tun_id} encap ip local ${local_ip} remote ${peer_ip} 2>/dev/null
    ip l2tp add session tunnel_id ${local_tun_id} session_id ${local_session_id} peer_session_id ${peer_session_id} 2>/dev/null
    ip link set l2tpeth0 up mtu ${mtu} 2>/dev/null
    ip addr add ${local_tun_ip} dev l2tpeth0 2>/dev/null

    log "l2tpv3 ip protocol tunnel setup successful."
}

setup_tun_udp()
{
    ip l2tp add tunnel tunnel_id ${local_tun_id} peer_tunnel_id ${peer_tun_id} udp_sport ${local_port} udp_dport ${peer_port} encap udp local ${local_ip} remote ${peer_ip} 2>/dev/null
    ip l2tp add session tunnel_id ${local_tun_id} session_id ${local_session_id} peer_session_id ${peer_session_id} 2>/dev/null
    ip link set l2tpeth0 up mtu ${mtu} 2>/dev/null
    ip addr add ${local_tun_ip} dev l2tpeth0 2>/dev/null

    log "l2tpv3 udp protocol tunnel setup successful."
}

add_default_route()
{
    cur_def_route=$(ip route |grep default |grep -v metric)
    pre_route="${cur_def_route} metric 10"
    peer_tun_ip=$(echo $peer_tun_ip |sed 's/\/.*//g')

    [ "${default_gw_enable}" = "1" ] && {

        if [ "${cur_def_route}" != "" ]; then
            ip route replace ${pre_route} 2>/dev/null
            ip route change default via ${peer_tun_ip} dev l2tpeth0 2>/dev/null
        else
            ip route add default via ${peer_tun_ip} dev l2tpeth0 2>/dev/null
        fi    
    }
}

del_default_route()
{
    cur_def_route=$(ip route |grep default |grep l2tpeth0)
    [ "${default_gw_enable}" = "1" -a "${cur_def_route}" != "" ] && {
        ip route del ${cur_def_route} 2>/dev/null
    }
}

setup_bridge()
{
    [ "${bridge_enable}" = "1" ] && {
        brctl addif br0 l2tpeth0 2>/dev/null
    }
}

start_service()
{
    case ${protocol} in
        ip)
            setup_tun_ip
            ;;

        udp)
            setup_tun_udp
            ;;
    esac

    add_default_route
    setup_bridge
}

stop_service()
{
    ip l2tp del tunnel tunnel_id ${local_tun_id} session_id ${local_session_id} 2>/dev/null
    ip l2tp del tunnel tunnel_id ${local_tun_id} 2>/dev/null
    del_default_route
}

restart_service()
{
    stop_service
    start_service
}

query_status()
{
    ip l2tp show tunnel 2>/dev/null
    ip l2tp show session 2>/dev/null
}

default_conf

case $1 in
    start)
        start_service
        ;;
    stop)
        stop_service
        ;;
    restart)
        restart_service
        ;;
    status)
        query_status
        ;;
    *)
        echo -e "\n$0 start | stop | restart | status \n"
        ;;
esac
