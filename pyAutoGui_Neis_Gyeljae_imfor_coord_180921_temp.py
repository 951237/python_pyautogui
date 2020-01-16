from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re


pa.FAILSAFE = True

#윈도우 창 타이틀
t1 = 'http://bms.ken.go.kr/?USERID=driver'
t2 = '과제카드'
t3 = '문서처리'

#윈도우 창찾기
def findWindowAndPosition(title):
    all = pa.getWindows()
    for i in all:
        if title in i:
            r_window = i
        else:
            continue
    # pa.getWindow(r_window).set_foreground()
    result = pa.getWindow(r_window).get_position()
    return result

#창의 색깔이 바뀜
print('결재정보를 찾는 중...')
t1Coord = findWindowAndPosition(t1)
print('창의 좌표 : %s' %(str(t1Coord)))

#창의 좌측 상단의 X좌표와 Y좌표를 변수로 지정
leftX, leftY = t1Coord[0:2]

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

print('결재창 찾는중...')
waitWindow(132,159,240,240,240)

print('결재정보 선택... ')
clickIwant(67,124)

#창의 색이 바뀜
print('과제카드 찾는 중....')
print('돋보기 선택....')
clickIwant(784,251)

print('과제카드 창 찾고 기다리는 중...')
t2Coord = findWindowAndPosition(t2)
print('창의 좌표 : %s' %(str(t2Coord)))
leftX, leftY = t2Coord[0:2]

# waitWindow()

print('정보 단위과제 선택....')
clickIwant(172,421)
print('확인 클릭....')
clickIwant(552,91)

#창의 색이 바뀜.
print('문서처리 선택....')
t1Coord = findWindowAndPosition(t1)
leftX, leftY = t1Coord[0:2]

clickIwant(412,93)

print('문서처리창 기다리는 중....')
waitWindow(107,346,248,248,248)
t3Coord = findWindowAndPosition(t3)
print('창의 좌표 : %s' %(str(t3Coord)))
leftX, leftY = t3Coord[0:2]

time.sleep(3)
print('확인 클릭....')
clickIwant(726,146)
# for i in range(2):
#     time.sleep(4)
#     pa.hotkey('enter')
#
# print('결재 완료')



