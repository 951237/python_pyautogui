from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re

# Note where the bot's window is.
# input('Move mouse over bot window and press Enter.')
# botWindow = pa.position()


# 프로그램에 필요한 버튼 좌표
탭_결재정보 = [54, 121]
버튼_문서처리 = [418, 78]
탭_공람 = [132, 462]
버튼_공람지정 = [815, 490]
버튼_문서처리 = [441, 80]
공람_학현초 = [74, 446]
공람_화살표 = [440, 410]
공람_확인 = [828, 223]
버튼_돋보기 = [792, 245]
빈공간 = [851, 115]
빈공간_터미널 = [39, 478]

neis_title = 'https://klef.goe.go.kr/?USERID=driver'
neis_card = ' -- 웹 페이지 대화 상자'
neis_confirm = '- 문서처리'
cmd_windows = 'C:\Windows\py.exe'

def waitWindow(p_x, p_y, p_r, p_g, p_b): # 좌표값과 rgb값
        i = 1
        while True:
            if pa.pixelMatchesColor(p_x, p_y, (p_r, p_g, p_b)) == True:  # 수덕원 예약 아이콘 좌표 및 색상코드
                print('결재창 찾음!')
                break
            print('%s번째 시도중...' % (i))
            i += 1
            time.sleep(1)

def findWindow(p_title):
    time.sleep(3)
    all = pa.getWindows()
    # print(all)
    for i in all:
        if p_title in i:
            result = i
            print(f'{result} 윈도우 여부 확인~')
        else:
            continue
    win = pa.getWindow(result)
    coord_win = win.get_position()
    print(f'결재창의 위치 {coord_win}를 찾습니다.')
    # input('결재창을 선택하세요.')
    return coord_win

def clickIwant(coord, 좌표):
    pa.click(coord[0] + 좌표[0], coord[1] + 좌표[1], clicks=1, interval=0.25)
    time.sleep(1.5)

def setup():
    cmd = findWindow(cmd_windows)

    _main = findWindow(neis_title)
    input('결재창을 선택하세요.')

    print('결재정보 선택... \n')
    clickIwant(_main, 탭_결재정보)

    print('과제카드 찾는 중....')
    print('돋보기 선택....\n')
    clickIwant(_main, 버튼_돋보기)
    return _main, cmd

def select_card(_main, cmd):
    # 과제카드 선택 창 작업
    print('정보 단위과제 선택....')
    sub_01 = findWindow(neis_card)

    # 단위과제 출력
    print('''
    1. 과제카드_과학교과
    2. 과제카드_정보교과
    3. 과제카드_개인정보
    4. 과제카드_정보기기관리
    5. 과제카드_보안관리
    6. 과제카드_홈페이지
    7. 과제카드_안전공제
    8. 과제카드_연수관리
    9. 과제카드_교육과정
    ''')
    select = int(input('선택할 단위과제는? : '))
    clickIwant(cmd, 빈공간_터미널)


    if select == 1:
        과제카드 = [200,435] # 과학교과
    elif select == 2:
        과제카드 = [200,410] # 정보교과
    elif select == 3:
        과제카드 = [200,285] # 개인정보
    elif select == 4:
        과제카드 = [200,360] # 정보기기관리
    elif select == 5:
        과제카드 = [200,310] # 보안관리
    elif select == 6:
        과제카드 = [200,335] # 홈페이지
    elif select == 7:
        과제카드 = [200,385] # 안전공제
    elif select == 8:
        과제카드 = [200,460] # 연수관리
    elif select == 9:
        과제카드 = [200,485] # 교육과정

    time.sleep(1)
    clickIwant(_main, 빈공간)
    clickIwant(sub_01, 과제카드)

    print('확인 클릭....')
    과제카드_확인 = [653,133]
    clickIwant(sub_01, 과제카드_확인)

def final(_main):
    #문서처리 작업 시작
    print('문서처리 시작....')
    clickIwant(_main, 버튼_문서처리 )

    # 문서처리창 작업하기
    sub_02 = findWindow(neis_confirm)

    # 문서처리창 확인 클릭하기
    print('확인 클릭....')
    문서처리_확인 = [714, 126]
    clickIwant(sub_02, 문서처리_확인)
    # for i in range(2):
    #     time.sleep(4)
    #     pa.hotkey('enter')
    #

    # print('결재 완료')

# 작업처리
_main, cmd = setup()
select_card(_main, cmd)
final(_main)

test = pa.getWindows()
for i in test:
    print(i)


