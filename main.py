import socket
from ports import getPacketLoggerPorts
import psutil
import win32process
from dataframe import Player, processEntry, displayStats
from utils import inject
import time


inject()
time.sleep(3)

TCP_IP = '127.0.0.1'
TCP_PORT = getPacketLoggerPorts()[0]
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

displayStats()

while True:
    try:
        data = s.recv(BUFFER_SIZE).decode("utf-8")
    except UnicodeDecodeError:
        pass
    cleanData = data.split("\r")
    for entry in cleanData:
        processEntry(entry)

s.close()