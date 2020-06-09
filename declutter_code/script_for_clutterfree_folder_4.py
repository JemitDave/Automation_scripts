from win10toast import ToastNotifier
import os,time

# os.chdir("C:/Users/usert/Desktop/test")
path=os.getcwd()
current_folder=os.path.split(path)[-1]  #gets working folder name to target
file_list=os.listdir(path)
for file in file_list:
    if file.endswith('.py' or '.pyw'):continue
    if os.path.isfile(file):
        src=os.path.join(path,file)
        folder_name=f"{(os.path.splitext(file)[1])[1:]}_files" #gets the extension of file
        try:
            if not os.path.exists(folder_name):         #check if dir present
                os.mkdir(folder_name)                   #makes new dir
        except FileExistsError:pass

        dst=os.path.join(path,folder_name,file)
        try:
            os.rename(src,dst)
        except FileExistsError:     #renames file name as 'copy_of_file'
            dst=os.path.join(path,folder_name,'copy_of_'+file)
            os.rename(src,dst)

#Windows notification, autocollapse after 3 sec
toaster=ToastNotifier()
toaster.show_toast(f"From {current_folder.capitalize()} Folder","folder organized",duration=3)
