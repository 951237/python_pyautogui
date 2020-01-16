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

time.sleep(5)
pa.vscroll(-750)
for i in range(0, 2, 1):
    v_checkLocation = pa.locateOnScreen('suCheck.png', region=(1050, 200, 1250, 700))
    suCheckX, suCheckY = pa.center(v_checkLocation)
    pa.click(suCheckX, suCheckY)

pa.vscroll(-750)
screenGrab()
pa.click(x=570, y=224, interval=0.03) #객식 '선택'클릭
pa.click(x=570, y=264, interval=0.03) #객실 ' 1개 ' 선택
pa.click(x=570, y=264, interval=0.03) #객실 ' 1개 ' 선택
pa.click(x=530, y=301, interval=0.03) #숙박인원 선택
pa.typewrite('4')
pa.click(x=628, y=485, interval=0.03) #핸드폰 번호 입력 좌표 이동
pa.typewrite('010', interval=0.03)
pa.hotkey('tab')
pa.typewrite('2719', interval=0.03)
pa.hotkey('tab')
pa.typewrite('9719', interval=0.03)
pa.click(x=554, y=557, interval=0.03) #직위 입력 좌표로 이동
pa.typewrite('teacher', interval=0.03)
pa.click(x=719, y=612, interval=0.03) #예약 클릭

# 빈공간 클릭
# 예약 확인 메세지 클릭 하기 전까지 루프문 돌리기 - 픽셀 확인
    # 새로고침
    # 페이지업 3회 반복
    # 입력작업 다시 시작


