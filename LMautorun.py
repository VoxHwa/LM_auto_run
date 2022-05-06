import pyautogui as pg
import time
import win32api,win32con
global x,y,noxpos
#get screen resolution 
def getres():
    '''找一个函数获得当前active screen resolution'''
    global x,y
    inNox()
    y=win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    x=win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    return x,y
def 龙猫logo():
    lm=None
    while lm==None:
        lm=pg.locateOnScreen(r"D:\screenshot\lm1080.png",confidence=0.6,region=noxpos)
    pg.click(lm)
def 龙猫_vx():
    lm_vx=None
    while lm_vx==None:
        lm_vx=pg.locateOnScreen(r"D:\screenshot\lm_vx.png",confidence=0.5,region=noxpos)
    pg.click(lm_vx)
#calculate Nox region
def noxarea():
    global x,y
    x,y=getres()
    global noxpos
    noxpos=None
    if y<=1080:
        test=r"D:\screenshot\header1080.png"
    if 1080<y<=1440:
        test=r"D:\screenshot\header1440.png"
    while noxpos==None: 
        noxpos=pg.locateOnScreen(test,confidence=0.5)
    noxpos=(noxpos.left,noxpos.top,noxpos.width,y)#1000要被替换为resolution的height
    return noxpos
#进入Nox
def inNox():
    time.sleep(1)
    pg.hotkey("win","r")
    #pg.("Nox.exe")
    pg.typewrite('Nox')
    time.sleep(2)
    pg.press("enter")
    time.sleep(20)
#kill Nox
def killNox(): 
    time.sleep(1)
    pg.hotkey("win","r")
    time.sleep(2)
    pg.typewrite('taskkill /f /t /im nox.exe')
    time.sleep(1)
    pg.press("enter")
    time.sleep(3)
#校准初始定位
def locatefix():
    time.sleep(1)
    pg.hotkey("ctrl","9")
    time.sleep(7)
    loc_corf("sc",area=noxpos)
    #loc_corf("box",area=(round(noxpos[0]+0.3*noxpos[2]),noxpos[1],noxpos[2],500))
    time.sleep(1)
    pg.moveRel(0,35)
    pg.doubleClick()
    #pg.typewrite('32.121209')
    #pg.press("tab")
    #pg.typewrite('118.92673')
    #pg.press("enter")
    time.sleep(1)
    
    confirm=loc_corf("confirm1080",mode=2,times=20,area=(round(noxpos[0]+0.7*noxpos[2]),noxpos[1]+500,2*noxpos[2],500))
#    while confirm is None:
#       confirm=pg.locateOnScreen(r'D:\screenshot\confirm1080.png',confidence=0.5)
    if confirm!=None:
        pg.click(confirm)
'''
def correctloc():    
    all=pg.locateAllOnScreen("D:\\screenshot\\startup.png",region=(round(.5*noxpos[2]+noxpos[0]),noxpos[1]+100,noxpos[2],noxpos[3]),confidence=0.8)
    for a in all:
        pg.click(a)
        time.sleep(20)
        locatefix()
        loc_corf("x",area=(noxpos[0]+round(2/3*noxpos[2]),noxpos[1]+100,2*noxpos[2],500))
        time.sleep(1)
        pg.hotkey("ctrl","6")
        time.sleep(8)
        break
'''
#龙猫vx登录
def vxlogin(account,password):
    account=""#vx账户
    password=""#vx密码

    acc=None
    while acc is None:
        time.sleep(1)
        acc=pg.locateOnScreen(r'D:\screenshot\acc1080.png',confidence=0.5,region=noxpos)
    pg.click(acc)
    time.sleep(1)
    pg.typewrite(account)
    time.sleep(1)
    pw=None
    while pw is None:
        time.sleep(1)
        pw=pg.locateOnScreen(r'D:\screenshot\pw1080.png',confidence=0.5,region=noxpos)
    pg.click(pw)
    time.sleep(1)
    pg.typewrite(password)
def confirm():
    loginvxbutton=None
    while loginvxbutton is None:
        loginvxbutton=pg.locateOnScreen(r'D:\screenshot\login.png',confidence=0.4,region=noxpos)
    time.sleep(1)
    pg.click(loginvxbutton)
#直接登录微信，只输入密码
def directvxlogin(password):
    vxlogo=None
    while vxlogo is None:
        vxlogo=pg.locateOnScreen(r'D:\screenshot\vxlogo.png',confidence=0.6,region=noxpos)
    pg.click(vxlogo)
    
    time.sleep(1)
    detectforcequit()

    pw=None
    while pw is None:
        time.sleep(1)
        pw=pg.locateOnScreen(r'D:\screenshot\pw.png',confidence=0.5,region=noxpos)
    pg.click(pw)
    time.sleep(1)
    pg.typewrite(password)
    time.sleep(1)
    confirm()
#forceoutdetect
def detectforcequit():
    '''要修一下被强制下线的的信息识别位置，重新截屏一下，***或者改善定位方式***'''
    count=0
    od=0
    time.sleep(5)
    while True:
        forceout=pg.locateOnScreen(r"D:\screenshot\qd.png",confidence=0.6,region=noxpos)
        count=count+1
        outdate=pg.locateOnScreen(r"D:\screenshot\outdate.png",confidence=0.7,region=noxpos)
        od=od+1
        if forceout!=None:
            #print(forceout)
            #forceresult=(forceout.left+.5*forceout.width,forceout.top+forceout.height)
            #print(forceresult)
            pg.click(forceout)
        if outdate!=None:
            pg.click(outdate)
        if count>20 and od>20:
            break

def loc_corf(name,area=noxarea(),mode=1,times=5):
    '''   mode=f or 2：搜索模式返回是否找到该图片  默认为mode=1(c)点击模式 times=0 默认无限查找点击  '''
    po=None
    name=str(name)
    count=0
    mode=str(mode)
    if mode=="f" or mode=="F" or mode=="2" and times>=1:
        while True:
            po=pg.locateOnScreen("D:\\screenshot\\"+name+".png",confidence=0.5,region=area)
            count=count+1
        
            if po!=None:
                return po
            if count>times:
                return po
    else:
        while po is None:
            po=pg.locateOnScreen("D:\\screenshot\\"+name+".png",confidence=0.5,region=area)
            count=count+1
            if count>200:
                ans=input("Target seem to not exist,need to give up?")
                if ans=='q' or ans=='Q':
                    return po
                else:
                    continue
        pg.click(po)
        time.sleep(1)
        return po
###
def onerunsimple():
    time.sleep(2)
    
    龙猫logo()
    time.sleep(2)
    龙猫_vx()
    time.sleep(2)
    loc_corf("ygrun")

    time.sleep(8)
    loc_corf("set",area=(noxpos[0]+round(2/3*noxpos[2]),noxpos[1],300,noxpos[3]))
    loc_corf("moreset",area=(noxpos[0]+round(2/3*noxpos[2]),noxpos[1],300,noxpos[3]))

    recheader=loc_corf(name="recmain",mode='f',times=20)
    recfield=(recheader.left+round(1/2*recheader.width),recheader.top+recheader.height,recheader.width,100)
    playrec=loc_corf("playrec",area=recfield)
def onerun(password):
    
    directvxlogin(password)
    time.sleep(8)
    #quit vx back to desktop
    if loc_corf(name="wo",mode=2,area=noxpos,times=10):
        time.sleep(2)
        pg.press("esc")
        pg.press("esc")
        time.sleep(5)
        pg.press("esc")
        pg.press("esc")
    else:
        print("可能不在vx主界面")
        pg.press("esc")#可退出后用模拟器自带脚本 simpler
        pg.press("esc")
        time.sleep(5)
        pg.press("esc")
        time.sleep(5)
        pg.press("esc")
        pg.press("esc")
    time.sleep(2)
    
    龙猫logo()
    time.sleep(2)
    龙猫_vx()
    time.sleep(2)
    loc_corf("ygrun")

    time.sleep(8)
    loc_corf("set",area=(noxpos[0]+round(2/3*noxpos[2]),noxpos[1],300,noxpos[3]))
    loc_corf("moreset",area=(noxpos[0]+round(2/3*noxpos[2]),noxpos[1],300,noxpos[3]))

    recheader=loc_corf(name="recmain",mode='f',times=20)
    recfield=(recheader.left+round(1/2*recheader.width),recheader.top+recheader.height,recheader.width,100)
    playrec=loc_corf("playrec",area=recfield)