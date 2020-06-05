#application:copy and pasting while reading journals,research papers, pdfs word etc
#pastes copied text as a .txt file 

import pyperclip as ppc,os
# import pyautogui as pag
from ctypes import windll
os.chdir('C:\\Users\\usert\\Desktop')
text=open('t5.txt','w')
text.write("Start==>\n")
text.close()


def clear_clip():                           #completely empties clipboard
    if windll.user32.OpenClipboard(None):
        windll.user32.EmptyClipboard()
        windll.user32.CloseClipboard()

def writer(para):                           #appends text
    text=open('t5.txt','a')
    text.write(para)
    text.write("\n\n")
    text.close()


clear_clip()        #initial clearing of clipboard
while True:
    para=ppc.waitForPaste()
    if len(para)==1:break                    #break from loop
    writer(para)         #accepts any text with lenght greater than 1
        # pag.alert('Copying Concluded') #graphical alert

    clear_clip()                        #empties clipboard after every copy and paste
clear_clip()
#text=open('t5.txt','r+')
#print(text.read())
