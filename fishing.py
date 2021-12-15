import time
import random
import pyautogui
import threading
import settings


def fish(data):
    if settings.FISHING:
        if int(data[4]) == settings.USER_ID:
            if int(data[5]) == 30 or int(data[5]) == 31:
                time.sleep(random.uniform(0.75, 2))
                pyautogui.press('e')
                time.sleep(random.uniform(5, 7))
                pyautogui.press('q')


def start_fish(data):
    threading.Thread(target=fish, args=[data]).start()