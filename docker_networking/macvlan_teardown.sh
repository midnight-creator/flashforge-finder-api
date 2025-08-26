#!/bin/sh
sudo ip route del 192.168.1.248/29 dev macvlan-shim 
sudo ip link set macvlan-shim down 
sudo ip addr del 192.168.1.249/24 dev macvlan-shim 
sudo ip link del macvlan-shim link enp3s0 type macvlan mode bridge