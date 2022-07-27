import time
import ctypes
import cv2
import pydirectinput as p
import pyautogui
import numpy
from sys import argv
from ctypes import wintypes
from .windows import WindowManager
import Unexpected.images as images
#Documentazione
#https://wiki.nexusmods.com/index.php/DirectX_Scancodes_And_How_To_Use_Them
#https://pynput.readthedocs.io/en/latest/mouse.html
#https://stackoverflow.com/questions/1181464/controlling-mouse-with-python

time.sleep(2)

#VARIABILI
yesbuttonimg = "images/YesButton.png"
exitbutton = "images/ExitButton.png"
iconbutton = "images/IconButton.png"
time.sleep(3)
HANDLER = WindowManager()

ALPHABET = {
    "1": 2,
    "2": 3,
    "3": 4,
    "[SPACEBAR]": 57,
    "A": 30,
    "B": 0x42,
    "C": 0x43,
    "D": 32,
    "E": 0x45,
    "F": 0x46,
    "G": 0x47,
    "H": 0x48,
    "I": 0x49,
    "J": 0x4A,
    "K": 0x4B,
    "L": 0x4C,
    "M": 0x4D,
    "N": 0x4E,
    "O": 0x4F,
    "P": 0x50,
    "Q": 0x51,
    "R": 0x52,
    "S": 30,
    "T": 0x54,
    "U": 0x55,
    "V": 0x56,
    "W": 17,
    "X": 0x58,
    "Y": 0x59,
    "Z": 0x5A,
    " ": 0x20,
    "/": 0xBF,
    ",": 51,
    ".": 0xBE,
    ";": 0xBA,
    "[ENTER]": 28,
    "[ESC]": 1
}

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


# Funzioni

def MoveTo(x,y):
    ctypes.windll.user32.SetCursorPos(x,y)

def PressMouse(time_down = 0):
    #HANDLER.focusROBLOX()
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    time.sleep(time_down)
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up

def PressKey(key):
    #HANDLER.focusROBLOX()
    hexKeyCode = ALPHABET[key]
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(key):
    hexKeyCode = ALPHABET[key]
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def Hotkey(hexKeyCode,time_down):
    PressKey(hexKeyCode)
    time.sleep(time_down)
    ReleaseKey(hexKeyCode)

def LocateImage():
    try:
        Yes_Position = gui.locateCenterOnScreen(yesbuttonimg, grayscale=False, confidence=0.65)
        print(f"Yes Button Find at location x={Yes_Position[0]} y={Yes_Position[1]}")
        p.moveTo(Yes_Position[0], Yes_Position[1])
        p.moveRel(0, 5)
        p.mouseDown()
        time.sleep(0.25)
        p.mouseUp()
    except:
        print('No YesButton.png Image Found')
        time.sleep(0.5)


