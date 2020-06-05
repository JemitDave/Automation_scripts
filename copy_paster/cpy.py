##application:copy and pasting while reading journals,research papers, pdfs word etc
##pastes copied text as a .txt file
##saves screenshots of specific region as png
import pyperclip as ppc,os,keyboard,pyautogui as pag
from ctypes import windll
from time import strftime,localtime
import time
os.chdir('C:\\Users\\usert\\Desktop\\copy_paster\\tester')
start_time=strftime('%d_%b_%Y_%H_%M_%S',localtime())
text=open('endtest.txt','w')
text.write(f"Started at {start_time}\n")
text.close()
##empty array for screenshot
xp=[]
yp=[]


##completely empties clipboard
def clear_clip():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()


##appends text
def writer(para):
    text=open('endtest.txt','a')
    text.write(para)
    text.write("\n\n")
    text.close()

##uses mouse location of top left and bottom right to take a screenshot
def take_ss(xp,yp):
    print(xp,yp)
    x1=min(xp)
    y1=min(yp)
    x2=max(xp)
    y2=max(yp)
    box=(x1,y1,x2-x1,y2-y1)
    name=strftime('%d_%b_%Y_%H_%M_%S',localtime())
    try:
        ss=pag.screenshot(region=box)
        ss.save(f"{name}.png")
    except:
        pag.alert('unable to take ss')
    xp.clear()
    yp.clear()



##initial clearing of clipboard
clear_clip()

while True:
    ##for screenshots
    # while True:
    try:
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
    except:break
    ##for text
    ##waits for non-empty string to be copied on clipboard
    para=ppc.waitForPaste()
    ##break from loop if single character selected i.e. ends script
    if len(para)==1:break
    writer(para)
    # pag.alert('Copying Concluded') #graphical alert
    ##empties clipboard after every copy and paste
    clear_clip()


clear_clip()
text=open('endtest.txt','r+')
print(text.read())
