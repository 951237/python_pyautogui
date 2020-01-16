#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#사용방법
0. 파이참 스크립트 준비하기
    - 객실유형 선택 후 좌표 수정
    - 숙박일 선택 후 좌표 수정
1. 파이참 에디터랑 사파리 창을 같은 윈도우에 둔다.
2. 사파리의 윈도우는 로그인
    - 예약신청/조회 - 예약신청
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
v_interval = 0.03
v_pause = 0.5
v_timeSleep = 0.5

# 연천 및 안성수덕원 객실 좌표
room = {'4a' : [631, 216],  #4인실 온돌 클릭
        '4a1' : [631, 233], #4인실 1개
        '4a2' : [631, 251],
        '8a' : [703, 217],   #8인실 선택
        '8a1' : [703, 233]  #8인실 1개
        }

# 가평수덕원 객실 좌표
ga_room = {'4a' : [631, 216],  # 4인실 클릭
        '4a1' : [631, 233],  # 4인실 1개
        '4a2' : [631, 251],  # 4인실 2개
        '6a' : [703, 217],  # 6인실 클릭
        '6a1' : [703, 233],  # 6인실 1개
        '6a2': [703, 251],  # 6인실 2개
        '8a' : [798, 216],  # 8인실 클
        '8a1' : [798, 233],  # 8인실 1개
           }
stay = {'1' : [602, 253],   #1박
        '2a' : [602, 270],  #1박 클릭좌표
        '2b' : [602, 253]   #2박 선택
        }
checkBox = {'0' : [1287, 619],
            '1' : [1169, 354],
            '2' : [1169, 724]
             }

person = [571, 295]     #숙박인원
phone = [629, 475]      #연락처
grade = [586, 550]      #직위
btnReg = [683, 558]     #예약버튼

# time.sleep(5)
pa.hotkey('command','tab', pause=0.3)

# print('새로고침')
# pa.click(x = 998, y = 42, interval=v_interval, pause=1.5) #오늘 날짜 클
#
# print('날짜 클릭')
# pa.click(x = 704, y = 467, interval=v_interval, pause=1.5) #오늘 날짜 클

print('여백 클릭') #스크롤 방지
pa.click(checkBox['0'], interval=v_interval, pause=v_pause) #여백 체크박스 클릭

print('-15만큼 이동합니다.')
pa.scroll(-15)
time.sleep(v_timeSleep)
print('1번째 체크박스 클릭')
pa.click(checkBox['1'], interval=v_interval, pause=v_pause) #첫번째 체크박스 클릭
print('2번째 체크박스 클릭')
pa.click(checkBox['2'], interval=v_interval) #두번째 체크박스 클릭

time.sleep(v_timeSleep)
pa.vscroll(-18)

print('객실을 선택합니다.')
pa.click(room['8a'], interval=v_interval, pause=v_pause) #객실유형 선택(4인, 8인, 4인침대)
pa.click(room['8a1'], interval=v_interval, pause = v_pause) #객실 ' 1개 ' 선택

print('숙박을 선택합니다.')
# pa.click(stay['1'], interval=v_interval, pause=v_pause) # 1박을 클
# pa.click(stay['2a'], interval=v_interval) # 2박을 선택

print('숙박인원을 입력합니다.')
pa.click(person, interval=v_interval, pause=v_pause) #숙박인원 선택
pa.typewrite('4', interval=0.1)
pa.click(phone, interval=v_interval) #핸드폰 번호 입력 좌표 이동

print('핸드폰 번호를 입력합니다.')
phoneNumber = ['010','2719','9719']
for i in phoneNumber:
    pa.typewrite(i, interval=v_interval)
    pa.hotkey('tab')

print('직위를 입력합니다.')
pa.typewrite('1', interval=v_interval)
# pa.click(btnReg, interval=v_interval) #예약 클릭

print('예약을 완료하였습니다.')
# pa.hotkey('enter')

