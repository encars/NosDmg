from injector import Injector
import psutil
import os


PROCESS_NAME = 'NostaleClientX.exe'


def getPacketLoggerPath(nostale_pid):
    process = psutil.Process(nostale_pid)
    return os.path.dirname(process.exe()) + '/PacketLogger.dll'


def getPid():
    for proc in psutil.process_iter():
        try:
            if PROCESS_NAME in proc.name():
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
