import threading
from launcher import launch
from gui import runGui


def main():
    threading.Thread(target=launch).start()
    runGui()


if __name__ == '__main__':
    main()