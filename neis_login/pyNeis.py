import pyautogui as pa, sys, os, time
from PIL import ImageGrab as IG

pa.FAILSAFE = True
sec_between_keys = 0.25
sec_between_term = 3
sec_sleep = 0.5

def screenGrab():
    box = ()
    im = IG.grab(box)
    im.save(os.getcwd() + '\\img\\full_snap__' + str(int(time.time())) + '.png', 'PNG')

def neis_before_login():
    #나이스 사이트 접속, 상용구 이
    # pa.hotkey('win','r')
    pa.typewrite(',skdl', interval=0.15)
    time.sleep(5)

    screenGrab()

    #나이스 로그인 - 아이디 입력
    pa.typewrite('driver1', interval=0.15)
    pa.press('tab')
    pa.press('enter')

    time.sleep(sec_between_term)
    #나이스 로그인 - 인증서 로그인
    # pa.typewrite(['tab','enter','tab','down','enter','tab'])

    screenGrab()
    pa.click(x=880, y=349,interval=0.1)
    time.sleep(sec_sleep)
    screenGrab()
    pa.click(x=940, y=400,interval=0.1)
    time.sleep(sec_sleep)
    screenGrab()
    pa.click(x=1030, y=621,interval=0.1)
    time.sleep(sec_sleep)

neis_before_login()

# if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
#     neis_before_login()

