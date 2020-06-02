#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = 'http://neis.goe.go.kr/'

# 함수 - bs4로 html 가져오기
driver = webdriver.Ie()
print('사이트에 접속중..')
driver.get(url)

try:
    driver.forward()
    driver.maximize_window()
    driver.implicitly_wait(10)
    print('아이디 입력중...')
    driver.find_element_by_xpath('//*[@id="login_input_area"]/input[1]').send_keys('driver1')

    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="login_input_area"]/input[2]').send_keys(Keys.ENTER)

    print('인증서 선택 - 이동식 디스크')
    driver.find_element_by_xpath('//*[@id="kc_cert_position"]/tbody/tr[2]/td[2]/button').click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@id="kc_cert_position"]/tbody/tr[2]/td[2]/ul/li[1]/a').click()

    driver.implicitly_wait(10)
    print('비밀번호를 입력합니다.')
    driver.find_element_by_xpath('//*[@id="kc_content_default"]/table/tbody/tr/td[2]/div/div[1]/table/tbody/tr/td[2]/form/input').click()
    input('Press Enter to continue...')


except Exception as e:
    print(e)
