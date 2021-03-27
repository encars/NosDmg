from injector import Injector
import psutil


PROCESS_NAME = 'NostaleClientX.exe'


def get_packet_logger_path(nostale_pid):
    process = psutil.Process(nostale_pid)
    return os.path.dirname(process.exe()) + '/PacketLogger.dll'


def get_pid():
    for proc in psutil.process_iter():
        try:
            if PROCESS_NAME in proc.name():
                pid = proc.pid
        except:
            print('Permission Error.')
    return pid


def inject():
    injector = Injector()

    pid = get_pid()
    path_dll = r'C:\Program Files (x86)\Nostale_DE\PacketLogger.dll'

    injector.load_from_pid(pid)
    injector.inject_dll(path_dll)
    injector.unload()