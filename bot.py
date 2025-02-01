from ctypes import *
from PIL import Image
import numpy as np
import win32ui
import time
import pyautogui
import re

windows = pyautogui.getAllWindows()
for window in windows:
    if re.search("Mozilla Firefox", window.title) is not None:
        title = window.title
        break

gdi= windll.LoadLibrary("c:\\Windows\\system32\\gdi32.dll")

w = win32ui.FindWindow(None, title)

size = 'expert'
shift = 0
right = 2
down = 1
match size:
    case 'expert':
        # j_range = range(175 + down * 16, 192 + down * 16)
        j_range = range(175 + down * 16 + 3, 175 + down * 16 + 4)
        i_range = range(711 + right * 16 + 9, 711 + right * 16 + 10)
        # i_range = range(711 + right * 16, 728 + right * 16)
    # case 'expert':
    #     j_range = range(175, 431)
    #     i_range = range(711, 1191)
    case _:
        j_range = range(1)
        i_range = range(1)



pixels = []
for j in j_range:
    row = []
    for i in i_range:
        dc = w.GetWindowDC()
        pixel = dc.GetPixel(i, j)
        print(pixel)
        bit_string = ("{:0{width}b}".format(pixel, width=24))
        rgb_pixel = (int(bit_string[16:24], 2), int(bit_string[8:16], 2), int(bit_string[:8], 2))
        row.append(rgb_pixel)

        dc.DeleteDC()

    pixels.append(row)
    
pixels = pixels
array = np.array(pixels, dtype=np.uint8)

new_image = Image.fromarray(array)
new_image.save('new.png')

one = 16711680
two = 31488
three = 255
four = 8060928
five = 123
six = 8092416
seven = 0
eight = 8092539

wall = 12434877

##################### FOR PIXEL READOUT
# j_range = range(175 + down * 16 + 3, 175 + down * 16 + 4)
# i_range = range(711 + right * 16 + 9, 711 + right * 16 + 10)