from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re


pa.FAILSAFE = True

#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def waitWindow(p_x, p_y, p_r, p_g, p_b):
    i = 1
    while True:
        if pa.pixelMatchesColor(p_x, p_y, (p_r, p_g, p_b)) == True:  # 수덕원 예약 아이콘 좌표 및 색상코드
            break
        print('%s번째 시도중...' %(i))
        i += 1
        time.sleep(1)

#윈도우 창찾기
def findWindow():
    all = pa.getWindows()
    for i in all:
        if 'http://bms.ken.go.kr/?USERID=driver' in i:
            r_window = i
        else:
            continue
    return r_window

#윈도우창 위치 찾기
def getPosition(p_win):
    pa.getWindow(p_win).set_foreground()
    result = pa.getWindow(p_win).get_position()
    return result

#윈도우내에서 일치하는 이미지 검색
def imgSearchClick(p_imgName):
    i = 0
    while True:
        if pa.locateOnScreen(p_imgName) != None:
            v_imgLocation = pa.locateOnScreen(p_imgName)
            imgLocationX, imgLocationY = pa.center(v_imgLocation)
            pa.click(imgLocationX, imgLocationY, interval=0.5, pause=0.5)
        print('%s번째 시도중...' %(i))
        i += 1
        time.sleep(1)

print('결재창 찾는중...')
waitWindow(662,315,240,240,240)

#창의 색깔이 바뀜
print('결재정보를 찾는 중...')
p_win = findWindow()
r_region = getPosition(p_win)

print('창의 좌표 : %s' %(str(r_region)))
# time.sleep(5)
#결재정보 선택

print('결재정보 찾는 중....')
imgSearchClick('imgNeisGyeljae01.png')

#창의 색이 바뀜
print('과제카드 찾는 중....')
imgSearchClick('imgNeisGyeljae02.png')
imgSearchClick('imgNeisGyeljae03.png')
imgSearchClick('imgNeisGyeljae04.png')

#창의 색이 바뀜.
print('문서처리 찾는 중....')
imgSearchClick('imgNeisGyeljae05.png')

print('문서처리창 기다리는 중....')
waitWindow(637,502,248,248,248)
imgSearchClick('imgNeisGyeljae04.png')
for i in range(2):
    time.sleep(3)
    pa.hotkey('enter')

print('결재 완료')

#과제카드 선택
#과학교과교육활동 선택
#확인 선택
#문서처리 선택