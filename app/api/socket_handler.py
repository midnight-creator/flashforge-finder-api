import socket
import time
import struct

BUFFER_SIZE = 1024
TIMEOUT_SECONDS = 5

def send_and_receive(printer_address: dict, message_data: str):
    """Sends and receives data"""

    printer_socket = socket.socket()
    printer_socket.settimeout(TIMEOUT_SECONDS)
    printer_socket.connect((printer_address['ip'], printer_address['port']))
    printer_socket.send(message_data.encode())
    data = printer_socket.recv(BUFFER_SIZE)
    printer_socket.close()

    return data.decode()

def send_data(printer_address: dict, filepath: str):
    printer_socket = socket.socket()
    printer_socket.settimeout(TIMEOUT_SECONDS)
    printer_socket.connect((printer_address['ip'], printer_address['port']))
    
    with open(filepath, 'rb') as f:
        while True:
            chunk = f.read(2)  # Read 2 bytes at a time
            printer_socket.send(chunk)
            status = printer_socket.recv(BUFFER_SIZE)
            if not chunk:
                break  # End of file
    printer_socket.close()