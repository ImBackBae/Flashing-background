import ctypes
import time
from ctypes.wintypes import RGB
from ctypes import byref, c_int

BLACK = RGB(0, 0, 0)
WHITE = RGB(255, 255, 255)
ctypes.windll.user32.SystemParametersInfoA(20, 0, "image.jpg" , 0)
while True:
    ctypes.windll.user32.SetSysColors(1, byref(c_int(1)), byref(c_int(BLACK)))
    time.sleep(1)
    ctypes.windll.user32.SetSysColors(1, byref(c_int(1)), byref(c_int(WHITE)))
    time.sleep(1)
