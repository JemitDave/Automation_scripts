import time
import os
import pyautogui as pag
#import json
import pandas as pd
File_name=[];dates=[];crtime=[];Path=[];Folder_for_dict=[] #empty lists for appending info

def changelogger(folder_to_track,filename,new_destination):#details of changelog
    c_time = os.path.getctime(folder_to_track)  #gets time of creation of file
    local_time = time.ctime(c_time)             #converts time to local time
    x=local_time.split()
    date,timex=x[2]+x[1]+x[4],x[3]
    File_name.append(filename)
    dates.append(date)
    crtime.append(timex)
    Path.append(new_destination)


def folder(filename):#creates new folder based on extension
    file_name, file_extension = os.path.splitext(filename)  #splits filane name
    folder_name=file_extension[1:]+'_files'  #.jpg becomes jpg_files (for new folder)
    Folder_for_dict.append(folder_name)
    try:
        if not os.path.exists(folder_name):         #check if dir present
            os.mkdir(folder_name)                   #makes new dir
            print("Directory " , folder_name ,  " Created ")
    except FileExistsError:pass
    new_name=folder_destination+'/'+folder_name+'/'+filename    #new location of file
    return new_name

def iterator():
    for filename in os.listdir(folder_to_track):  #iterates in directory
            if 'changelog' in filename:pass
            else:
                name=folder_to_track+'/'+filename
                if os.path.isfile(name):                      #works only on files not folder
                    src=folder_to_track+'/'+filename          #source Directory
                    new_destination=folder(filename)          #new directory
                    changelogger(folder_to_track,filename,new_destination)
                    os.rename(src,new_destination)


start_time=time.clock()
#folder_to_track='C:/Users/usert/Desktop/deutch'             #for test
folder_to_track=input('Enter folder to track')
folder_destination=input('Enter destination folder')     #target directory (main dir)
try:
    os.mkdir(folder_destination)                         #destinaton Directory
    print("New Folder Created")
except FileExistsError:pass

#folder_destination='C:/Users/usert/Desktop/deutch'         #for test
os.chdir(folder_destination)                              #changes working dir
iterator()

dicts={'File_name':File_name,'FOLDER':Folder_for_dict,'date':dates,'crtime':crtime,'Path':Path,} #creates dictionary
column_name=['File_name','FOLDER','date','crtime','Path']    #sets column name
df=pd.DataFrame(dicts,columns=column_name)          #converting to dataframe
sorted_df=df.sort_values(by='FOLDER')
if not 'changelog.csv' in os.listdir(folder_to_track):  #if changelog not present, creates one
    sorted_df.to_csv("changelog.csv",index=False)                         #saving to csv
else:sorted_df.to_csv('changelog.csv', mode='a',index=False,header=False)  #if cl present, appends it
print(sorted_df)
end_time=time.clock()
#print(end_time-start_time)
pag.alert('Downloads folder organized','attention')
