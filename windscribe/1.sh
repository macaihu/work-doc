iptables -t nat -N windscribe
iptables -t nat -A POSTROUTING -j windscribe
iptables -t nat -A windscribe -o tun0 -j MASQUERADE
