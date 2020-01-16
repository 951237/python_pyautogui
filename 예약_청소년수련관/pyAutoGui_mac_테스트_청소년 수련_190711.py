#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
#사용방법
- 파이참 실행 / 스크립트 준비
- 호멮이지 접속 후 온라인 강좌 신청하기 메뉴 접속
- 강좌선택후 신청
- 파이참 스크립트 실행
'''

#라이브러리 임포트
import pyautogui as pa
import time

#변수값
v_interval = 0.03
v_pause = 0.3
v_timeSleep = 0.5

# 연천 및 안성수덕원 객실 좌표
checkBox = {'0' : [1287, 619], #여백
            '1' : [455, 582],  #개인정보동의
            '2' : [796, 742]   #신청하기 버튼
             }

pay = {
    'chk' : [706, 598],
    'acc' : [831, 599],
    'cash' : [598, 600]
}

# time.sleep(5)
pa.hotkey('command','tab', pause=0.3)

print('여백 클릭') #스크롤 방지
pa.click(checkBox['0'], interval=v_interval, pause=v_pause) #여백 체크박스 클릭

print('-15만큼 이동합니다.')
pa.scroll(-15)
time.sleep(v_timeSleep)
print('1번째 체크박스 클릭')
pa.click(checkBox['1'], interval=v_interval, pause=v_pause) #첫번째 체크박스 클릭

print('-7만큼 이동합니다.')
pa.scroll(-7)
time.sleep(v_timeSleep)

print('결재수을 선택합니다.')
pa.click(pay['chk'], interval=v_interval, pause=v_pause) #결재유형 - 신용카드

print('신청하기 클릭')
pa.click(checkBox['2'], interval=v_interval, pause=v_pause) #신청하기
