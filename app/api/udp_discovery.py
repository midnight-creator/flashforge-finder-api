import socket
import time
import struct

class UDP_discovery:
    """FlashForge Printers announces itself when sent a discovery message is sent to IP 225.0.0.9 on Port 19000"""
    def __init__(self, dest_ip: str = "225.0.0.9", dest_port: int = 19000, discovery_message: str = b'c0a8014346500000'):
        self.dest_ip = dest_ip
        self.dest_port = 19000
        self.discovery_message = discovery_message
        self.devices = {}

    def scan_devices(self, timeout: int = 5):
        # Create a UDP socket
        UDP_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        UDP_socket.settimeout(timeout)
        # Limit the TTL 1 so the packet remains on the local network
        UDP_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, struct.pack('b', 1))
        
        # Bind to every IP on the destination port
        UDP_socket.bind(('0.0.0.0', self.dest_port))

        # Send the message to the multicast group
        UDP_socket.sendto(self.discovery_message, (self.dest_ip, 19000))
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                data, addr = UDP_socket.recvfrom(len(self.discovery_message))
                self.devices[addr] = data.decode('utf-8')
            except TimeoutError as e:
                continue
            
    
    def get_devices(self):
        return self.devices
    
    def get_device_ips(self):
        return self.devices.keys()
    
    def get_device_names(self):
        return self.devices.values()
    
    def clear_devices(self):
        self.devices = {}
