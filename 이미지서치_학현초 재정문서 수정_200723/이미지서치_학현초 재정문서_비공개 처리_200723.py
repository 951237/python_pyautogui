import time
import pyautogui as pa

pa.FAILSAFE = True

# 이미지 경로
img_비공개 = 'img/비공개.png'
img_재정문서 = './img/재정문서.png'
img_지우기 = './img/지우기.png'
img_저장 = './img/저장.png'


def img_search_move_click(p_img_file, p_click=None):
    loc_img = pa.locateCenterOnScreen(p_img_file)  # 이미지파일 센터값 저장
    print(loc_img)
    time.sleep(0.25)
    pa.moveTo(loc_img)
    pa.click(loc_img)  # 강의실 입장 센터값 클릭
    time.sleep(0.25)  # 화면 바뀌기 대기

img_search_move_click(img_비공개)
img_search_move_click(img_재정문서)
img_search_move_click(img_지우기)
pa.hotkey("ctrl", "v")
img_search_move_click(img_저장)