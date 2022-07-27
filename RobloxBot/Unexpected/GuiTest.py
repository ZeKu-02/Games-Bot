import pyautogui
import win32api
import win32con
from pyautogui import *
import cv2
import pyautogui as gui
import time
import keyboard
import numpy
import random
import pywin
#from .keybinds import Hotkey

Key_Pressed = False
start = True
time.sleep(2)

#images
yesbuttonimg = "images/YesButton.png"
exitbutton = "images/ExitButton.png"
iconbutton = "images/IconButton.png"
print(gui.size())
#gui.moveTo(100,100)
#gui.click(100,100, 1 ,3, button= "left")


time.sleep(3)
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while start == True :
 #gui.keyDown('e')
 if keyboard.is_pressed("q") and Key_Pressed == False:
   Key_Pressed = True
   time.sleep(0.2)
 if keyboard.is_pressed("q") and Key_Pressed == True:
    Key_Pressed = False
    print("Stop")
    time.sleep(0.2)
 if Key_Pressed == True:
   print(gui.position())

   try:
       Yes_Position = gui.locateCenterOnScreen(yesbuttonimg, grayscale=False, confidence=0.65)
       print(f"Yes Button Find at location x={Yes_Position[0]} y={Yes_Position[1]}")
       gui.moveTo(Yes_Position[0], Yes_Position[1], 0.8)
       click(555,501)
       time.sleep(0.1)
       gui.click(555,501)
       time.sleep(0.5)
   except:
       print('No Image Found')
       time.sleep(0.5)




