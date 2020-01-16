#라이브러리 임포트
from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re

#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

#실행된 프로그램 리스트 만들기


#수덕원 사이트 좌표 구하기


pa.hotkey('win', '3') #크롬창 실행시키기

v_chrome = 'Google - Chrome'
#크롬창이 뜰때까지 기다리기
while True:
    if v_chrome in pa.getWindows():
        win = pa.getWindow('Google - Chrome')
        break

while True:
    if pa.pixelMatchesColor(766, 311, (52, 168, 83)) == True: #구글마크중 초록색 l마크 좌표 및 색상
        screenGrab() #스크린샷 찍기
        pa.doubleClick(x= 1119, y= 545 , interval=0.02) #로그인 클릭
        break
win.maximize() #창 최대화하기

#수덕원 사이트 접속하기
pa.hotkey('ctrl', 'l') #주소표시줄 단축키
pa.typewrite('http://www.gew.kr/anseong/main.php', interval=0.01) #안성수덕원 접속하기
pa.hotkey('enter') #주소입력후 엔터 입력

#수덕원 사이트 로그인하기
#수덕원 사이트 스크린샷
while True:
    if pa.pixelMatchesColor(239, 550, (136, 211, 229)) == True: #수덕원 예약 아이콘 좌표 및 색상코드
        screenGrab() #스크린샷 찍기
        break

pa.doubleClick(x= 1119, y= 545 , interval=0.02) #로그인 클릭

while True:
    if pa.pixelMatchesColor(239, 550, (255, 255, 255)) == True: #수덕원 예약 아이콘 좌표 및 색상코드
        screenGrab() #스크린샷 찍기
        break

pa.hotkey('enter') #환영메세지 창 닫기

#예약사이트로 이동하기
while True:
    if pa.pixelMatchesColor(234, 548, (136, 211, 229)) == True: #수덕원 예약 아이콘 좌표 및 색상코드
        pa.doubleClick(x= 234, y= 548 , interval=0.02) #로그인 클릭
        screenGrab() #스크린샷 찍기
        break






'''
#과제 
- 크롬창이 떠있을 때 확인후 활성화 시키기
- 크롬창이 떠있지 않으면 크롬창 부르기
'''

