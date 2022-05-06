from LMautorun import *
import pyautogui as pg
import time
import win32api,win32con

time.sleep(30)#等待模拟器启动
locatefix()#校正定位，初始位置
killNox()#关模拟器