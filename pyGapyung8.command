#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#사용방법
1. 파이참 에디터랑 사파리 창을 같은 윈도우에 둔다.
2. 사파리의 윈도우는 로그인 - 예약 신청 페이지에서 대기
3. 스크립트 실행
'''


#라이브러리 임포트
from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re

#변수값
v_interval = 0.02
v_pause = 0.5


#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

# time.sleep(5)
pa.hotkey('command','tab', pause=0.5)
print('-15만큼 이동합니다.')
pa.scroll(-15)
time.sleep(0.5)
print('1번째 체크박스 클릭')
pa.click(x=1088, y=354, interval=v_interval, pause=0.5) #첫번째 체크박스 클릭
print('2번째 체크박스 클릭')
pa.click(x=1088, y=724, interval=v_interval) #두번째 체크박스 클릭
# for i in range(0, 2, 1):
#     v_checkLocation = pa.locateOnScreen('suCheckMac.png', region=(1033, 315, 1161, 741))
#     suCheckX, suCheckY = pa.center(v_checkLocation)
#     print(suCheckX,suCheckY)
#     pa.click(suCheckX, suCheckY)
#     print('%s번째 체크박스 완료' %(i+1))
time.sleep(0.5)
pa.vscroll(-18)

print('객실을 선택합니다.')
pa.click(x=684, y=162, interval=0.03, pause=0.5) #객식 '선택'클릭
pa.click(x=684, y=172, interval=0.03) #객실 ' 1개 ' 선택
# pa.click(x=570, y=168, interval=0.03) #객실 ' 1개 ' 선택

print('숙박인원을 입력합니다.')
pa.click(x=494, y=238, interval=0.03) #숙박인원 선택
pa.typewrite('4')
pa.click(x=584, y=419, interval=0.03) #핸드폰 번호 입력 좌표 이동

print('핸드폰 번호를 입력합니다.')
pa.typewrite('010', interval=0.03)
pa.hotkey('tab')
pa.typewrite('2719', interval=0.03)
pa.hotkey('tab')
pa.typewrite('9719', interval=0.03)

print('직위를 입력합니다.')
pa.click(x=584, y=495, interval=0.03) #직위 입력 좌표로 이동
pa.typewrite('teacher', interval=0.03)
pa.click(x=683, y=558, interval=0.03) #예약 클릭

print('예약을 완료하였습니다.')
pa.hotkey('enter')

