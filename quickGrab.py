"""

All coordinates assume a screen resolution of 1920x1080, and Opera
no Bookmarks Toolbar enabled, running in a Win8 PC.
URL = http://goo.gl/6v7nM6
x_pad = 462
y_pad = 68
Play area =  x_pad+1, y_pad+1, 901, 727
"""

from PIL import ImageGrab as IG
import pyautogui as pa
import os
import time

def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    screenGrab()

if __name__ == '__main__':
    main()

