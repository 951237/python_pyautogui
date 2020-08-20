import pyautogui as pa
import time

pa.FAILSAFE = True

좌표 = {
    '결재정보' : [57,122],
    '결재정보_돋보기' : [780,249],
    '윈도우_스크립트' : [390,300],
    '윈도우_결재' : [1322,276],
    '과제카드_확인' : [687,175],
    '문서처리' : [420, 80],
    '문서처리_확인' : [770, 230]
}

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
def findWindow(p_win_title):
    all = pa.getWindows()
    for i in all:
        if p_win_title in i:
            r_window = i
            print('결재창 찾기 완료~')
        else:
            continue
    return r_window

#윈도우창 위치 찾기
def getPosition(p_win):
    pa.getWindow(p_win).set_foreground()
    result = pa.getWindow(p_win).get_position()
    print('윈도우 위치값 확인!')
    return result

def clickIwant(p_name, 좌표):
    print(f'{p_name}를 클릭합니다.','\n')
    x = leftX + 좌표[0]
    y = leftY + 좌표[1]
    pa.click(x,y,clicks=1,interval=0.25)
    print(f'x좌표 : {x}, y좌표 : {y} 클릭!')
    time.sleep(0.75)

def clickIwant_global(p_name, 좌표):
    print(f'{p_name}를 클릭합니다.','\n')
    pa.click(좌표[0],좌표[1],clicks=1,interval=0.25)
    print(f'x좌표 : {좌표[0]}, y좌표 : {좌표[1]} 클릭!')
    time.sleep(0.75)

def change_window(window_subject):
    i = 1
    while True:
        try:
            result = findWindow(window_subject)
            return result
            break
        except:
            print(f"{i}차 시도!")
            time.sleep(1)
            i += 1


def find_sign_window():
    print('결재창 찾는중...')
    waitWindow(700, 200, 44, 133, 191)  # 앞의 700, 200은 x, y 위치값 / 뒤의 44, 133, 191은 rgb값임

    # 창의 색깔이 바뀜
    print('결재정보를 찾는 중...')
    w_title = 'https://klef.goe.go.kr/?USERID=driver'
    p_win = findWindow(w_title)
    r_region = getPosition(p_win)

    print('창의 좌표 : %s' % (str(r_region)))

    # 창의 좌측 상단의 X좌표와 Y좌표를 변수로 지정
    leftX, leftY = r_region[0:2]
    return  leftX, leftY

def find_subject_windows():
    # 결재 정보 선택
    clickIwant('결재정보', 좌표['결재정보'])

    # 과제 카드 창 띄우기
    clickIwant('결재정보_돋보기', 좌표['결재정보_돋보기'])

    # 단위 과제 창 찾기
    # win_subject = change_window("K-에듀파인 -- 웹")
    # pa.getWindow(win_subject).set_foreground()

def select_subject():
    # 스크립트 창 바꾸기
    win_cmd = change_window('C:\Windows')
    pa.getWindow(win_cmd).set_foreground()
    # 과제 단위 화면 출력
    print('''
    1. 과제카드_과학교과
    2. 과제카드_정보교과
    3. 과제카드_개인정보
    4. 과제카드_정보기기관리
    5. 과제카드_보안관리
    6. 과제카드_홈페이지
    7. 과제카드_안전공제
    ''')
    select = int(input('선택할 단위과제는? : '))
    # 결제창으로 바꾸기
    # clickIwant_global('윈도우_결재',좌표['윈도우_결재'])
    win_subject = change_window("K-에듀파인 -- 웹")
    pa.getWindow(win_subject).set_foreground()

    # 과제카드 선택
    if select == 1:
        과제카드 = [200, 475]  # 과학교과
    elif select == 2:
        과제카드 = [200, 450]  # 정보교과
    elif select == 3:
        과제카드 = [200, 275]  # 개인정보
    elif select == 4:
        과제카드 = [200, 400]  # 정보기기관리
    elif select == 5:
        과제카드 = [200, 350]  # 보안관리
    elif select == 6:
        과제카드 = [200, 375]  # 홈페이지
    elif select == 7:
        과제카드 = [200, 425]  # 안전공제
    # elif select == 8:
    #     과제카드 = [200,500] # 연수관리
    # elif select == 9:
    #     과제카드 = [200,525] # 교육과정
    time.sleep(1)

    #과제카드 선택
    clickIwant("과제카드", 과제카드)

    #과제카드 확인
    clickIwant("과제카드_확인", 좌표["과제카드_확인"])

def handle_card():
    clickIwant("문서처리", 좌표["문서처리"])
    # 문서처리창 기다리기
    change_window('https://klef.goe.go.kr/ - 문서처리')

    # 문서처리창 확인 클릭
    clickIwant('문서처리_확인', 좌표['문서처리_확인'])

    # 확인
    for i in range(2):
        time.sleep(4)
        pa.hotkey('enter')


if __name__ == "__main__":
    # 터미널 창에서 결재창으로 전환하기
    pa.hotkey('alt', 'tab')

    # 결재창 찾아서 좌표 출력하기
    leftX, leftY = find_sign_window()

    # 과제 카드 창 찾기
    find_subject_windows()

    # 과제 카드 선택하기
    select_subject()

    # 문서 처리하기
    handle_card()

    # 결재완료 출력
    print('결재완료!!!')

