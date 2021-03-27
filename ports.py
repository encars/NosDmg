from typing import List
from psutil import process_iter, AccessDenied, Process


def get_processes(substring: str) -> List[Process]:
    processes = []
    for process in process_iter():
        try:
            if substring in process.name():
                processes.append(process)
        except AccessDenied as err:
            pass
    return processes


def get_nostale_packet_logger_ports() -> List[int]:
    processes = get_processes("NostaleClientX.exe")
    ports = []
    for process in processes:
        for connection in process.connections():
            if connection.laddr and connection.laddr.ip == "127.0.0.1":
                ports.append(connection.laddr.port)
    return ports


# print(get_nostale_packet_logger_ports())