#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#라이브러리 임포트
from PIL import ImageGrab as IG
import pyautogui as pa
import os
import time

#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def waitWindows(p_x, p_y, p_r, p_g, p_b):
    i = 1
    while True:
        if pa.pixelMatchesColor(p_x, p_y, (p_r, p_g, p_b), tolerance=10) == True: #구글마크중 초록색 l마크 좌표 및 색상
            print('수덕원 페이지 로딩 완료.')
            break
        print("%s번째 시도중..." %(i))
        time.sleep(0.5)
        i += 1
        continue


#변수값
v_interval = 0.02
v_pause = 0.5
v_page = ',duscjs'


#수덕원 사이트 좌표 구하기

print('수덕원 홈페이지로 이동중...')
pa.hotkey('ctrl', 'space', interval=v_interval, pause=v_pause) #스팟라이트 실행
pa.typewrite(v_page, interval=v_interval, pause=v_pause) #상용구 안성수덕원 입력
pa.hotkey('space', pause=0.05)

print('페이지 찾는중....')
time.sleep(2)
pa.hotkey('command', 'tab', pause=0.05)

waitWindows(1058, 558, 106, 177, 86)

print('계정정보 입력중...')
pa.click(x=950, y=520, interval=v_interval, pause=v_pause)
pa.click(x=950, y=540, interval=v_interval)
pa.doubleClick(x=1064, y=558, interval=0.02, pause=1)

print('로그인 완료.')
pa.hotkey('enter',pause=1)

print('예약페이지로 이동')
pa.click(x=200, y=535, interval=v_interval)
pa.click(x=200, y=535, interval=v_interval)


'''
#과제 
- 크롬창이 떠있을 때 확인후 활성화 시키기
- 크롬창이 떠있지 않으면 크롬창 부르기
'''

