#Modules
import pydirectinput as p   #https://github.com/learncodebygaming/pydirectinput                      #https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input
import ctypes
import pyautogui
import time
import numpy
from api.keybinds import PressKey , ReleaseKey , MoveTo , Hotkey ,PressMouse ,LocateImage

time.sleep(5)

while (True):
    """
    p.moveTo(56,417)
    time.sleep(0.25)
    p.moveRel(0,5)
    p.mouseDown()
    time.sleep(0.25)
    p.mouseUp()
    """
    LocateImage()
    #PressKey(0x11)
    #time.sleep(1)
    #ReleaseKey(0x11)
    #time.sleep(1)11
    print(pyautogui.position())
    p.keyDown("w")
    time.sleep(2)
    p.keyUp("w")
    #Hotkey("W",1)
    #time.sleep(1)
    #MoveTo(1249,17)
    Hotkey("[SPACEBAR]",0.35)
    time.sleep(1)
