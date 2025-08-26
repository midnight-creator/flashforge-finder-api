# Multicasting Traffic, Docker, & UDP Discovery
Docker containers will need to be exposed to external traffic to pickup multicast traffic.

From my brief research, setting up a macvlan networking appears to be the best but it only works on Linux

This folder contains the rough draft to for a Docker container that supports the device's UDP discovery mechanism.

The bash scripts are to setup and teardown the networking on the host computer's side to get the container to be able to communicate with external traffic.