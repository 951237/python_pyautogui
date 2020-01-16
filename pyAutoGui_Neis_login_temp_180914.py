from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re


pa.FAILSAFE = True
sec_between_keys = 0.25
sec_between_term = 3
sec_sleep = 0.5

#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def waitWindow(p_x, p_y, p_r, p_g, p_b):
    i = 1
    time.sleep(2)
    while True:
        if pa.pixelMatchesColor(p_x, p_y, (p_r, p_g, p_b)) == True:  # 수덕원 예약 아이콘 좌표 및 색상코드
            break
        print('%s번째 시도중...' %(i))
        i += 1
        time.sleep(0.25)

#나이스 화면 띄우기에서 비밀번호 입력전까지

#나이스 사이트 접속, 상용구 이
pa.typewrite(',skdl', interval=0.15, pause=0.25) #상용구로 나이스접속
waitWindow(1143, 307, 251, 15, 12)

#나이스 로그인 - 아이디 입력
pa.click(x= 1174, y = 386, interval=0.02, pause=0.25)
pa.typewrite('driver1', interval=0.15) #아이디 입력
pa.hotkey('tab', interval=0.02) #탭키 누르기
pa.hotkey('enter', interval=0.02) #엔터키 입력

#인증서화면이 나올때 까지 기다리기
waitWindow(1038, 706, 14, 110, 166)

pa.click(x=874, y=339, interval=0.02, pause=0.5) #이동식디스크 아이콘 클릭
pa.click(x=912, y=398, interval=0.02) #D드라이브 선택
pa.click(x=1000, y=622, interval=0.02) #비번 입력칸 선택
pa.click(x=1000, y=622, interval=0.02) #비번 입력칸 선택
pa.click(x=1000, y=622, interval=0.02) #비번 입력칸 선택

