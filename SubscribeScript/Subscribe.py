from json.tool import main
import time
from pyautogui import *
import pyautogui
import sys
import win32api, win32con
import os

#clicks mouse using windows api   
def click(x,y):
    win32api.SetCursorPos( (x,y) )
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#finds chosen image
def findTarget(image):
    #locates image with grayscale and 90% confidence. returns bool and position
    if pyautogui.locateCenterOnScreen(image, grayscale=True, confidence=0.9) !=None:
        pos =pyautogui.locateCenterOnScreen(image, grayscale=True, confidence=0.9)
        print("target found")
        return True, pos
    else:
        print("target not found")
        pos = (0,0)
        return False, pos

#exits browser
def exitBrowser(cBrowser):
    #use browser pic name, replace format and kill task
    browserW = cBrowser.replace('png','exe',1)
    os.system("taskkill /im "+ browserW + " /f")
    sys.exit()

#finds chrome or firefox to click
def findBrowser():
    #iterate to find either chrome or firefox
    browsers = ['chrome.png','firefox.png']

    for i in browsers:
        browser = i
        print(browser)
        found, pos = findTarget(browser)
        if found:
            return pos, browser

#subscribes
def subscribe():
    #search channel name, find swedish or english sub button
    time.sleep(0.5)
    pyautogui.write('DannysBlazingBonfire',0.01)
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(2.5)
    buttons = ['subscribe.png','subscribesw.png']
    for i in buttons:
        button = i
        found,(x,y) = findTarget(button)
        if found:
            return (x,y)
    
#main method    
def main():
    #set pyautogui sleep to 0.01sec
    pyautogui.PAUSE=0.01
    #findbrowser, enter youtube, search name, subscribe, close window, close program
    (x,y),cBrowser = findBrowser()
    pyautogui.moveTo(x,y)
    click(x,y)
    time.sleep(0.1)
    click(x,y)
    time.sleep(3)
    pyautogui.write('https://www.youtube.com/', 0.01)
    pyautogui.press('enter')
    time.sleep(3)
    found,(x,y) = findTarget('youtube.png')
    if(found):
        click(x+300,y)
    else:
        sys.exit()
    (x,y) = subscribe()
    click(x,y)
    time.sleep(0.8)
    exitBrowser(cBrowser)

#start program
if __name__ == "__main__":
    main()