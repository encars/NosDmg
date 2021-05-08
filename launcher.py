import time
import socket
from utils import inject, getPacketLoggerPorts
from dataframe import processData
import settings


def launch():
    inject()
    time.sleep(3)
    
    TCP_IP = '127.0.0.1'
    TCP_PORT = getPacketLoggerPorts()[0]
    BUFFER_SIZE = 2048

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    while settings.RUNNING:
        data = s.recv(BUFFER_SIZE).decode(encoding='utf-8', errors='replace')
        cleanData = data.split("\r")
        for entry in cleanData:
            try:
                processData(entry)
            except:
                print(f'Error processing the following data: {entry}')


def exitProgram():
    settings.RUNNING = False