#easy way found
import time
import os
import json
import pandas as pd
File_name=[];dates=[];crtime=[];Path=[] #empty lists for appending info

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



folder_to_track='C:/Users/usert/Desktop/deutch'
#try:
#    os.mkdir('C:/Users/usert/Desktop/deutch')         #source Directory
#except FileExistsError:pass
folder_destination='C:/Users/usert/Desktop/deutch'        #target directory (main dir)
os.chdir(folder_destination)                              #changes working dir
iterator()

dicts={'File_name':File_name,'date':dates,'crtime':crtime,'Path':Path} #creates dictionary
column_name=['File_name','date','crtime','Path']    #sets column name
df=pd.DataFrame(dicts,columns=column_name)          #converting to dataframe
if not 'changelog.csv' in os.listdir(folder_to_track):  #if changelog not present, creates one
    df.to_csv("changelog.csv",index=False)                         #saving to csv
else:df.to_csv('changelog.csv', mode='a',index=False,header=False)  #if cl present, appends it
print(df)
