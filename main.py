
import pyautogui
import random
import PySimpleGUI as sg
from time import sleep
import subprocess

'''

import os
import sys
#print (os.path.dirname(sys.executable))

sg.theme("DarkBlack")
layout = [
    [sg.Button("RUN THAT", key="run")]
]

window = sg.Window("BING POINT FARMER", layout,size=(500, 50))
#pyautogui.moveTo(1300,60)

firstTime = True

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "run":
        if (firstTime):
            firstTime = False
            subprocess.call(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
            with pyautogui.hold('win'):
                pyautogui.press('up')
            pyautogui.moveTo(1300,65)
            sleep(0.2)
            pyautogui.click()
            with pyautogui.hold('ctrl'):
                pyautogui.press('a')
            pyautogui.press('backspace')


        list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        new = ""
        for i in range (40):
            sleep(0.1)
            new = new + list[random.randint(0,len(list)-1)]
            pyautogui.write(new)
            pyautogui.press("enter")
            pyautogui.click()

        new = "bing "
        
        for i in range (4):
            sleep(0.1)
            new = new + list[random.randint(0,len(list)-1)]
            pyautogui.write(new)
            pyautogui.press("enter")
            pyautogui.click()

        with pyautogui.hold('ctrl'):
            pyautogui.press('a')
            
        pyautogui.write("
        https://rewards.bing.com")
        pyautogui.press("enter")
    break
'''

firstTime = True
if (firstTime):
    firstTime = False
    subprocess.call(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])
    with pyautogui.hold('win'):
        pyautogui.press('up')
    pyautogui.moveTo(1300,65)
    sleep(0.2)
    pyautogui.click()
    with pyautogui.hold('ctrl'):
        pyautogui.press('a')
    pyautogui.press('backspace')

    list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    new = ""
    for i in range (30):
        sleep(6)
        new = new + list[random.randint(0,len(list)-1)]
        pyautogui.write(new)
        pyautogui.press("enter")
        pyautogui.click()
'''
    new = "bing "
    for i in range (4):
        sleep(0.1)
        new = new + list[random.randint(0,len(list)-1)]
        pyautogui.write(new)
        pyautogui.press("enter")
        pyautogui.click()

    with pyautogui.hold('ctrl'):
        pyautogui.press('a')
    pyautogui.write("https://rewards.bing.com")
    pyautogui.press("enter")
'''
