from LMautorun import *
import pyautogui as pg
import time
import win32api,win32con
''' vx直接登录再登录龙猫(目前最佳）'''

time.sleep(30)#等待模拟器启动
onerun("")  #""内填你微信密码，onerun中有sleep来等待模拟器启动完成
time.sleep(400) #等待跑完时间400s
killNox()   #关闭模拟器