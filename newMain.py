import os
import shutil

import _thread

import time
import sys

###
def MoveFile():

    sourceDir = "Y:\\torrents\\complete"
    destDir = ""

    for root, dirs, files in os.walk(sourceDir):
        for file in files:
            if file.endswith(".mp4"):
                if(root != sourceDir):
                    fileToMove = os.path.join(root, file)
                    print("Moveing: ", os.path.join(root, file))
                    
                    try:
                        _thread.start_new_thread( MoveDir, (fileToMove,) )
                        trackProgress(root,file)
                    except:
                       print ("Error: unable to start thread & moving the file.")
                    
                    #MoveDir(root)
                    doneMSG = "\nDone moving: {}\n".format(file)
                    print(doneMSG)
                    
                    #os.rename(os.path.join(root, file), os.path.join(destDir,root,file))
                    

def trackProgress(sourceDir="Y:\\torrents\\complete\\test",file="",destDir="\\\\192.168.2.125\\Movies"):
    
    size = 0
    

    # get size
    #Check for main file
    if(file != ""):
        time.sleep(1.5)
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

    total = int(size) #1007  # total number to reach
    bar_length = 30  # should be less than 100

    print("Tracking!")
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
    print("Moveing...")
    try:
        shutil.move(sourceDir,destDir)
    except:
        print("ERROR: Folder/File already there!")
    return


MoveFile()