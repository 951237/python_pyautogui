from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re


pa.FAILSAFE = True

#윈도우 창찾기
def findWindowAndPosition(title):
    all = pa.getWindows()
    for i in all:
        if title in i:
            r_window = i
        else:
            continue
    pa.getWindow(r_window).set_foreground()
    result = pa.getWindow(r_window).get_position()
    return result

#윈도우창 위치 찾기
def getPosition(p_win):
    pa.getWindow(p_win).set_foreground()
    result = pa.getWindow(p_win).get_position()
    return result


def waitWindow(p_x, p_y, p_r, p_g, p_b):
    i = 1
    while True:
        if pa.pixelMatchesColor(leftX + p_x, leftY + p_y, (p_r, p_g, p_b)) == True:  # 수덕원 예약 아이콘 좌표 및 색상코드
            break
        print('%s번째 시도중...' %(i))
        i += 1
        time.sleep(1)

def clickIwant(_x,_y):
    pa.click(leftX + _x,leftY + _y,clicks=1,interval=0.25)
    time.sleep(0.75)

a = 'http://bms.ken.go.kr/?USERID=driver'
b = '과제카드선택'
c = '문서처리'

aCoord = findWindowAndPosition(a)
leftX, leftY = aCoord[0:2]
print(leftX, leftY)

# bCoord = findWindowAndPosition(b)
# leftX, leftY = bCoord[0:2]
# print(leftX, leftY)

cCoord = findWindowAndPosition(c)
leftX, leftY = cCoord[0:2]
print(leftX, leftY)
