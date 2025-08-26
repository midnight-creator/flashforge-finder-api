#!/bin/sh
# Setup the shim routing so the host can see the new containers via IP
sudo ip link add macvlan-shim link enp3s0 type macvlan mode bridge
sudo ip addr add 192.168.1.249/24 dev macvlan-shim
sudo ip link set macvlan-shim up
sudo ip route add 192.168.1.248/29 dev macvlan-shim