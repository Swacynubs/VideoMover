import os
import shutil

import _thread

import time
import sys

from pathlib import Path

###
def MoveFile():

    sourceDir = "Y:\\torrents\\complete"
    destDir = ""

    for root, dirs, files in os.walk(sourceDir):
        for file in files:
            if file.endswith(".mp4"):
                #print("File:",file)
                #print("root",root)
                if(root != sourceDir):
                    print("Moveing: ", os.path.join(root, file))
                    print("\ndir:",os.getcwd())
                    _thread.start_new_thread( MoveDir, (root,) )
                    trackProgress(root,file)
                    try:
                        print("HI")
                       
                       #_thread.start_new_thread( trackProgress, (root,file,) )
                       
                    except:
                       print ("Error: unable to start thread")
                    
                    #MoveDir(root)
                    print("\nDone!\n")
                    #os.rename(os.path.join(root, file), os.path.join(destDir,root,file))
                    

def trackProgress(sourceDir="Y:\\torrents\\complete\\test",file="",destDir="\\\\192.168.2.125\\Movies"):
    # assing size
    size = 0
    print("Tracking!")
    # assign folder path
    #Folderpath = 'C:/Users/Geetansh Sahni/Documents/R'
    
    

    # get size
    #Check for main file
    if(file != ""):
        fp = os.path.join(sourceDir, file)
        size = os.path.getsize(fp)
        print("Path+File:",sourceDir,file,"\n")
        dirname = os.path.dirname(fp)
        print("\n=== Parent:===\n",dirname)

    else:
        for path, dirs, files in os.walk(sourceDir):
            for f in files:
                fp = os.path.join(path, f)
                size += os.path.getsize(fp)
    print("Size: ",size)
    total = int(size) #1007  # total number to reach
    bar_length = 30  # should be less than 100


    #Get the new file and check it's size
    newFile = os.path.join(destDir, file)
    notFull = True
    i=0
    print("Looking at: ",newFile)
    while notFull:
        i=os.path.getsize(newFile)
        #os.path.getsize(os.path.join(destDir,file))
        percent = 100.0*i/total
        #percent = 100.0*os.path.getsize(newFile)/total
        sys.stdout.write('\r')
        sys.stdout.write("Completed: [{:{}}] {:>3}%"
                         .format('='*int(percent/(100.0/bar_length)),
                                 bar_length, int(percent)))
        sys.stdout.flush()
        if(i >= size):
            notFull = False

        time.sleep(1)

def MoveDir(sourceDir="Y:\\torrents\\complete\\test",destDir="\\\\192.168.2.125\\Movies"):
    #sourceDir = "Y:\\torrents\\complete\\test"
    #destDir = "\\\\192.168.2.125\\Movies"

    try:
        shutil.move(sourceDir,destDir)
    except:
        print("ERROR: Folder already there!")
    return


MoveFile()