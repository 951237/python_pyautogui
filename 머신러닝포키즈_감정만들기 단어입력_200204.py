import pyautogui
import pyperclip
import time
import sys
import pandas as pd

pyautogui.FAILSAFE = True

FILE_PATH = '/Users/mac/Documents/python_work/my_project/pyAutogui/feelings.xlsx'

time.sleep(3)
df = pd.read_excel(FILE_PATH, sheet_name='Sheet1')
goodwords = \
    df[df["감정범주"].isin(["기쁨", "흥미"])].sort_values(by='감정정도M',
                                                  ascending=False)[51:-1][
        ["단어"]].drop_duplicates().values.flatten()

badwords = \
    df[df["감정범주"].isin(["분노", "혐오"])].sort_values(by='감정정도M', ascending=False)[51:-1][
        ["단어"]].drop_duplicates().values.flatten()

allwords = [goodwords, badwords]


def click(x, y):
    time.sleep(0.5)
    pyautogui.moveTo(x, y)
    pyautogui.click(clicks=1)
    time.sleep(0.5)


x = 0
for words in allwords:
    for i in range(len(words)):
        click(360 + x, 850)
        # click(632, 489)
        pyperclip.copy(words[i])
        pyautogui.hotkey("command", "v")
        time.sleep(0.5)
        click(839, 602)
        click(839, 602)
    x += 690
