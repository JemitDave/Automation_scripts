##application:copy and pasting while reading journals,research papers, pdfs word etc
##pastes copied text as a .txt file
##saves screenshots of specific region as png

from pynput.keyboard import Key, Listener
import keyboard as kyb
import pyperclip as ppc,os,pyautogui as pag
from time import strftime,localtime
from ctypes import windll

# os.chdir('C:\\Users\\usert\\Desktop\\copy_paster\\tester')
start_time=strftime('%d_%b_%Y_%H_%M_%S',localtime())
doc_name=pag.prompt('Enter the doc name')
text=open(f"{doc_name}.txt",'w')
text.write(f"Started at {start_time}\n")
text.close()
xp=[]
yp=[]
#completely empties clipboard
def clear_clip():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

#appends text
def writer(para):
    text=open(f"{doc_name}.txt",'a')
    text.write(para)
    text.write("\n\n")
    text.close()

#takes ss of a user defined region
def take_ss(xp,yp):
    print(xp,yp)
    x1=min(xp)
    y1=min(yp)
    x2=max(xp)
    y2=max(yp)
    box=(x1,y1,x2-x1,y2-y1)
    ss=pag.screenshot(region=box)
    name=strftime('%d_%b_%Y_%H_%M_%S',localtime())
    try:
        ss.save(name+'.png')
        print('ss taken')
    except:pag.alert("unable to take ss")
    xp.clear()
    yp.clear()

''' for debug     '''
def on_press(key):
    if key==Key.ctrl_r:
        print('screenshot mode (ctrl_r is pressed)')
        #enter screenshot Code
        print('go to loc for ss region and press z')
        for i in range(0,2):
            kyb.wait('z')
            xi,yi=pag.position()
            print('position {} recorded'.format(i))
            xp.append(xi)
            yp.append(yi)
        take_ss(xp,yp)

    elif key==Key.ctrl_l:
        #copy paste code
        print('copy paste mode(ctrl_l is pressed)\n (text already pasted)')
        para=ppc.waitForPaste()
        # if len(para)==1:break                    #break from loop
        writer(para)         #accepts any text with lenght greater than 1
        # pag.alert('Copying Concluded') #graphical alert
        clear_clip()                        #empties clipboard after every copy and paste


    else:pass
    # print('{0} pressed'.format(
    #     key))

def on_release(key):
    # print('{0} release'.format(
    #     key))
    if key == Key.esc:
        # Stop listener
        return False

clear_clip()
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
