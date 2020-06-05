import pyautogui as pag
import keyboard,os
from time import strftime,localtime
os.chdir('C:\\Users\\usert\\Desktop\\copy_paster\\tester')
xp=[]
yp=[]
def take_ss(xp,yp):
    print(xp,yp)
    x1=min(xp)
    y1=min(yp)
    x2=max(xp)
    y2=max(yp)
    box=(x1,y1,x2-x1,y2-y1)
    # pag.alert('ss taken')
    ss=pag.screenshot(region=box)
    name=strftime('%d_%b_%Y_%H_%M_%S',localtime())
    ss.save(name+'.png')
    print('ss taken')
    xp.clear()
    yp.clear()



while True:
    if keyboard.is_pressed('a'):
        print('give loc for ss and press z')
        for i in range(0,2):
            keyboard.wait('z')
            xi,yi=pag.position()
            print('position {} recorded'.format(i))
            xp.append(xi)
            yp.append(yi)
        take_ss(xp,yp)
        break
    else:pass
