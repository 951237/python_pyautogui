from PIL import ImageGrab as IG
import pyautogui as pa
import sys
import os
import time
import re


pa.FAILSAFE = True

#스크린샷
def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def waitWindow(p_x, p_y, p_r, p_g, p_b):
    i = 1
    while True:
        if pa.pixelMatchesColor(p_x, p_y, (p_r, p_g, p_b)) == True:  # 수덕원 예약 아이콘 좌표 및 색상코드
            print('결재창 찾음!')
            break
        print('%s번째 시도중...' %(i))
        i += 1
        time.sleep(1)

#윈도우 창찾기

def findWindow(윈도우이름):
    all = pa.getWindows()
    for i in all:
        if 윈도우이름 in i:
            r_window = i
            print('결재창 여부 확인~')
        else:
            continue
    return r_window

#윈도우창 위치 찾기
def getPosition(p_win):
    pa.getWindow(p_win).set_foreground()
    result = pa.getWindow(p_win).get_position()
    print('윈도우 위치값 확인!')
    return result

#윈도우내에서 일치하는 이미지 검색
def imgSearchClick(p_imgName):
    v_imgLocation = pa.locateOnScreen(p_imgName)
    imgLocationX, imgLocationY = pa.center(v_imgLocation)
    pa.click(imgLocationX, imgLocationY, interval=0.5, pause=0.5)

print('결재창 찾는중...')
waitWindow(700,200,44,133,191) # 앞의 700, 200은 x, y 위치값 / 뒤의 44, 133, 191은 rgb값임

#창의 색깔이 바뀜
print('결재정보를 찾는 중...')
결재창 = 'https://klef.goe.go.kr/?USERID=driver'
p_win = findWindow(결재창)
r_region = getPosition(p_win)

print('창의 좌표 : %s' %(str(r_region)))

#창의 좌측 상단의 X좌표와 Y좌표를 변수로 지정
leftX, leftY = r_region[0:2]

def clickIwant(좌표):
    pa.click(leftX + 좌표[0],leftY + 좌표[1],clicks=1,interval=0.25)
    print('딸깍!')
    time.sleep(0.75)

# 결재정보 선택 - todo 색을 인식하여 클릭하기
print('결재정보 선택... ')
결재정보 = [57,122]
clickIwant(결재정보)

# todo 공람 여부 물어보기

#창의 색이 바뀜
print('과제카드 찾는 중....')
print('돋보기 선택....')
결재정보_돋보기 = [775,249]
clickIwant(결재정보_돋보기)
print('정보 단위과제 선택....')
waitWindow(880,244,44,133,191)  # 과제선택창 기다리기
time.sleep(2)
pa.hotkey('alt', 'tab')
pa.hotkey('alt', 'tab')

# 과제목록 출력
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
pa.hotkey('alt', 'tab')

if select == 1:
    과제카드 = [200,475] # 과학교과
elif select == 2:
    과제카드 = [200,450] # 정보교과
elif select == 3:
    과제카드 = [200,325] # 개인정보
elif select == 4:
    과제카드 = [200,400] # 정보기기관리
elif select == 5:
    과제카드 = [200,350] # 보안관리
elif select == 6:
    과제카드 = [200,375] # 홈페이지
elif select == 7:
    과제카드 = [200,425] # 안전공제
elif select == 8:
    과제카드 = [200,500] # 연수관리
elif select == 9:
    과제카드 = [200,525] # 교육과정

time.sleep(1)
clickIwant(과제카드)

print('확인 클릭....')
과제카드_확인 = [687,175]
clickIwant(과제카드_확인)

#창의 색이 바뀜.
print('문서처리 선택....')
문서처리 = [420, 80]
clickIwant(문서처리)

print('문서처리창 기다리는 중....')

waitWindow(800,310,44,133,191)
time.sleep(3)
print('확인 클릭....')
문서처리_확인 = [770, 230]
clickIwant(문서처리_확인)
for i in range(2):
    time.sleep(2)
    pa.hotkey('enter')

print('결재 완료')



