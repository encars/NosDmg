from injector import Injector
import psutil
import os
from typing import List
from psutil import process_iter, AccessDenied, Process
import settings


def getProcesses(substring: str) -> List[Process]:
    processes = []
    for process in process_iter():
        try:
            if substring in process.name():
                processes.append(process)
        except AccessDenied as err:
            pass
    return processes


def getPacketLoggerPorts() -> List[int]:
    processes = getProcesses(settings.PROCESS_NAME)
    ports = []
    for process in processes:
        for connection in process.connections():
            if connection.laddr and connection.laddr.ip == "127.0.0.1":
                ports.append(connection.laddr.port)
    return ports


def getPacketLoggerPath(pid):
    process = psutil.Process(pid)
    return os.path.dirname(process.exe()) + '/PacketLogger.dll'


def getPid():
    for proc in psutil.process_iter():
        try:
            if settings.PROCESS_NAME in proc.name():
                pid = proc.pid
        except:
            pass
    return pid


def inject():
    injector = Injector()

    pid = getPid()
    path_dll = getPacketLoggerPath(pid)

    injector.load_from_pid(pid)
    injector.inject_dll(path_dll)
    injector.unload()