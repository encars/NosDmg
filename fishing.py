import time
import random
import pyautogui
import threading

def fish(data):
    if(int(data[5]) == 30 or int(data[5]) == 31):
        time.sleep(random.uniform(0.75, 2))
        pyautogui.press('e')
        time.sleep(random.uniform(5, 7))
        pyautogui.press('q')


def start_fish(data):
    fishingThread = threading.Thread(target=fish, args=[data]).start()