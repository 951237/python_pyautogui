import pyautogui,Quartz

destination = 300
pyautogui.click()
while destination > 0:
    pyautogui.dragRel(destination,0,duration=0.01)
    destination -= 10
    pyautogui.dragRel(0,destination,duration=0.01)
    pyautogui.dragRel(-destination,0,duration=0.01)
    destination -= 10
    pyautogui.dragRel(0,-destination,duration=0.01)

