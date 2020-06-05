##application:copy and pasting while reading journals,research papers, pdfs word etc
##pastes copied text as a .txt file
##saves screenshots of specific region as png


from pynput.keyboard import Key, Listener
from pynput import mouse
import pyperclip as ppc,os,pyautogui as pag
from time import strftime,localtime,sleep
from ctypes import windll

os.chdir("J:\Python\zdocs for copy paster")
start_time=strftime('%d_%b_%Y_%H_%M_%S',localtime())
doc_name=pag.prompt('Enter the txt file name')+'.txt'
if os.path.isfile(doc_name):
    ans=pag.prompt('''    File already Exists,to continue press ok
    else type new name ''')
    if ans!='':doc_name=ans+'.txt'
text=open(f"{doc_name}",'a')
text.write(f"Started at {start_time}\n")
text.close()
xp=[]
yp=[]
##completely empties clipboard
def clear_clip():
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

##appends text
def writer(para):
    text=open(f"{doc_name}",'a')
    text.write(para)
    text.write("\n\n")
    text.close()

##takes ss of a user defined region
def take_ss(xp,yp):
    global doc_name
#    print(xp,yp)
    x1=min(xp)
    y1=min(yp)
    x2=max(xp)
    y2=max(yp)
    box=(x1,y1,x2-x1,y2-y1)
    ss=pag.screenshot(region=box)
    name=strftime('%d_%b_%Y_%H_%M_%S',localtime())
    try:
        ss.save(doc_name+' '+name+'.png')
#        print('ss taken')
    except:pag.alert("unable to take ss")
    xp.clear()
    yp.clear()

def on_click(x, y, button, pressed):
    if pressed:
#        print(f"pressed at {x,y}")  ##to append top left position of image
        xp.append(x)
        yp.append(y)
    else :
#        print(f"Released at {x,y}")    ##to append bottom left position of image
        xp.append(x)
        yp.append(y)
        sleep(2)
        take_ss(xp,yp)
        return False                ##stops mouse listener's thread
        

def on_press(key):
    if key==Key.ctrl_r:
#        print('screenshot mode (ctrl_r is pressed)')
#        print("starting mouse listner")
        m_listener= mouse.Listener(on_click=on_click)
        m_listener.start()


    elif key==Key.ctrl_l:
        ##copy paste code
#        print('copy paste mode(ctrl_l is pressed)\n (text pasted)')
        para=ppc.waitForPaste()
        writer(para)         ##accepts any text with lenght greater than 0
        clear_clip()                        ##empties clipboard after every copy and paste


    else:pass

def on_release(key):
    if key == Key.esc:
        ans=pag.confirm('close program?')
        ## Stop listener
        if ans=='OK':return False
        
clear_clip()
## Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as k_listener:
    k_listener.join()
