import pyperclip as ppc,os
# import pyautogui as pag
from ctypes import windll
os.chdir('C:\\Users\\usert\\Desktop')
text=open('t4.txt','w')
text.write("Start\n")
text.close()


def clear_clip():                           #completely empties clipboard
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

def writer(para):                           #appends text
    text=open('t4.txt','a')
    text.write(para)
    text.write("\n")
    text.close()


clear_clip()        #initial clearing of clipboard
while True:
    para=ppc.paste()
    if len(para)>1:writer(para)         #accepts any text with lenght greater than 1
    if len(para)==1:                    #break from loop
        # pag.alert('Copying Concluded') #graphical alert
        break
    clear_clip()                        #empties after every copy

text=open('t4.txt','r+')
print(text.read())
