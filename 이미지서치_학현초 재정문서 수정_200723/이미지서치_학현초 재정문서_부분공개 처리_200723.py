import time
import pyautogui as pa

pa.FAILSAFE = True

# 이미지 경로
img_수정 = 'img/수정.png'
img_한건수정 = 'img/한건수정.png'
img_부분공개 = 'img/부분공개.png'
img_저장 = './img/저장.png'
img_수정사유 = './img/수정사유.png'
img_확인 = './img/확인.png'


def img_search_move_click(p_img_file, p_click=None):
    try:
        loc_img = pa.locateCenterOnScreen(p_img_file)  # 이미지파일 센터값 저장
        if loc_img == None:
            print('이미지를 찾지 못함.')
            exit()
        else:
            print(loc_img)
            time.sleep(0.1)
            pa.moveTo(loc_img)
            pa.click(loc_img)  # 강의실 입장 센터값 클릭
            time.sleep(0.1)  # 화면 바뀌기 대기
    except:
        print('이미지를 찾지못함!')
        exit()

# 인터넷 창 찾기
# 창의 크기 내에서 이미지 검색하기

img_search_move_click(img_수정)
img_search_move_click(img_한건수정)
time.sleep(6)
img_search_move_click(img_부분공개)
img_search_move_click(img_저장)
time.sleep(0.5)
img_search_move_click(img_수정사유)
# 사유 : 본문부분공개
pa.hotkey('ctrl', 'v')
img_search_move_click(img_확인)
time.sleep(3)
pa.hotkey('enter')