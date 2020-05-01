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

#화면이 켜질때 까지 기다리기
all = pa.getWindows()
for i in all:
    if 'http://bms.ken.go.kr/?USERID=driver' in i:
        print(i, 'yes')
    else:
        continue
pa.getWindow('카카오톡').set_foreground()
te = pa.getWindow('카카오톡').get_position()
print(te)

'''
RAON K Hybrid Agent
Study_webCrawling from 2018 [D:\OneDrive - 학현초등학교\Gdrive\★작업중\SW_PyCharm\studyPython from 2018] - ...\crawling\crawler_naver news_all_180802 .py [Study_webCrawling from 2018] - PyCharm
...\pyAutogui\pyAutoGui_Neis_Gyeljae_180906.py [Study_webCrawling from 2018] - PyCharm
http://bms.ken.go.kr/?USERID=driver1&APPRIDLIST=J10CB182424951849000&APPRDEPTID=J100004848&APPR - Internet Explorer
http://bms.ken.go.kr/ - 결재대기 | 업무관리시스템 - Internet Explorer
업무포털 - 석진일/학현초등학교 - Internet Explorer
경기도교육청
카카오톡
이미지 014.png - 픽픽
WorkFlowy
Windows에서 파이썬 스크립트 실행용 exe 실행파일 구성방법 - Chrome
cli.exe - Everything
받은 쪽지 - 최종철(학현초등학교 전담)
받은 쪽지 - 김소희(학현초등학교 4학년)
Daum 지도 - Chrome
Total Commander 7.04 - University of Amsterdam
백업 및 동기화
'''