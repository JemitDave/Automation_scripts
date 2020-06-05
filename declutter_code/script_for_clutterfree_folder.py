from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os
import json

def folder(filename):
    file_name, file_extension = os.path.splitext(filename)  #splits filane name
    folder_name=file_extension[1:]+'_files'  #.jpg becomes jpg_files (for new folder)
    if not os.path.exists(folder_name):         #check if dir present
        os.mkdir(folder_name)                   #makes new dir
        print("Directory " , folder_name ,  " Created ")
    new_name=folder_destination+'/'+folder_name+'/'+filename    #new location of file
    return new_name

class Myhandler(FileSystemEventHandler):
    i=1
    def on_modified(self,event):
        for filename in os.listdir(folder_to_track):  #iterates in directory
            src=folder_to_track+'/'+filename          #source Directory
            new_destination=folder(filename)          #new directory
            os.rename(src,new_destination)

folder_to_track='C:/Users/usert/Downloads/sorter2'           #source Directory
folder_destination='C:/Users/usert/Downloads'        #target directory (main dir)
os.chdir(folder_destination)                          #changes working dir
event_handler=Myhandler()
Observer=Observer()
Observer.schedule(event_handler,folder_to_track,recursive=True)
Observer.start()                                    #creates a new thread

try:
    while True:
        time.sleep(10)                              #keeps the thread running
except KeyboardInterrupt:
    Observer.stop()                                 #stops if interrupted
Observer.join()                                     #does some work before the thread terminate
