import socket
from ports import get_nostale_packet_logger_ports
import psutil
import win32process
from dataframe import Player, process_entry
from utils import inject


TCP_IP = '127.0.0.1'
TCP_PORT = get_nostale_packet_logger_ports()[0]
BUFFER_SIZE = 2048

inject()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

while True:
    try:
        data = s.recv(BUFFER_SIZE).decode("utf-8")
    except UnicodeDecodeError:
        pass
    cleanData = data.split("\r")
    for entry in cleanData:
        process_entry(entry)

s.close()
