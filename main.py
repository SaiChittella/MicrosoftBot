import webbrowser as web
import time
import random as rand
import math
from pynput.keyboard import Key, Controller
import pyautogui as pyau


website = 'https://www.bing.com'
edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

web.register('edge', None, web.BackgroundBrowser(edge_path))

keyboard = Controller()

time.sleep(2)

# For the Web
# 34


def runWeb(times):
    time.sleep(0.5)
    pyau.hotkey('ctrl', 't')
    time.sleep(0.3)
    for i in range(0, times):
        number1 = math.floor(rand.random() * 1520)
        number2 = math.floor(rand.random() * 2800)
        time_to_sleep = math.floor(rand.random() * 1.5) + 1
        time.sleep(1)
        for char in ('' + str(number1) + '*' + str(number2)):
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.11)

        pyau.hotkey('enter')
        time.sleep(time_to_sleep)
        pyau.hotkey('ctrl', 'w')
        pyau.hotkey('ctrl', 't')
        time.sleep(0.8)

# # For Mobile


def mobile(times):
    # 20
    for i in range(times):
        if i == 0:
            x, y = pyau.locateCenterOnScreen('search.png', confidence=0.4)
            pyau.moveTo(x, y, 0.2)
            pyau.click()
            time.sleep(0.5)
        else:
            time.sleep(1)
            pyau.scroll(200)
            x, y = pyau.locateCenterOnScreen('logo.png', confidence=0.4)
            pyau.moveTo(x, y, 0.2)
            pyau.click()
            time.sleep(0.5)

        number1 = math.floor(rand.random() * 1520)
        number2 = math.floor(rand.random() * 2800)
        time_to_sleep = math.floor(rand.random() * 1.5) + 1

        for char in ('' + str(number1) + '*' + str(number2)):
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.15)

        pyau.hotkey('enter')
        time.sleep(time_to_sleep)


def randActivities():
    pass


def runEverything(web):
    if web:
        runWeb(34)

    pyau.hotkey('ctrl', 'shift', 'i')
    time.sleep(1.5)
    pyau.hotkey('ctrl', 'shift', 'm')
    time.sleep(1.5)
    pyau.click()

    mobile(20)

    pyau.hotkey('ctrl', 't')
    time.sleep(1)
    randActivities()


# runEverything(False)

# Switch Accounts


def switchAccount():
    x, y = pyau.locateCenterOnScreen('settings_button.png', confidence=0.9)
    pyau.moveTo(x, y, 0.2)
    pyau.click()
    time.sleep(1)

    x, y = pyau.locateCenterOnScreen('profiles.png', confidence=0.8)
    pyau.moveTo(x, y, 0.3)
    pyau.click()
    time.sleep(0.5)

    x, y = pyau.locateCenterOnScreen('your_profile.png', confidence=0.8)
    pyau.moveTo(x, y, 0.2)
    time.sleep(1)
    pyau.click()
    pyau.scroll(-200)

    time.sleep(1)

    x, y = pyau.locateCenterOnScreen('personal2_account.png', confidence=0.95)
    pyau.moveTo(x, y, 0.3)

    x, y = pyau.locateCenterOnScreen('switch2_button.png', confidence=0.9)
    pyau.moveTo(x, y, 0.2)
    pyau.click()


# 11
# runWeb(34)
# pyau.hotkey('ctrl', 'shift', 'i')
# time.sleep(0.7)
# pyau.hotkey('ctrl', 'shift', 'm')
# time.sleep(1.5)
# pyau.click()
# mobile(20)
# randActivities()

switchAccount()
runEverything(True)
