import threading
from launcher import launch
from gui import runGui


def main():
    infoThread = threading.Thread(target=launch).start()
    runGui()


if __name__ == '__main__':
    main()

#test