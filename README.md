# Video Mover

MP4 Mover is a small program I created to move movies from my torrent folder to my data server

## Download & Run

Download the code and type the follwoing:

```bash
py newMain.py
```

## Requirements

Python3

##Usage
1. Open newMain.py and change the source folder and destination folder to which folders you'd like to use

### How it works

The program will scan the directory and sub directories you enter in at the top of the file.
If it finds a mp4 file it will move it over to the destination you have 

### Future Updates
+ Option to copy folders not just files
+ More video file support
+ UI for ease of use
+ Option 
+ More data about the file it is moving
+ Option to over right if the file is already in the destination folder

#### Known Bugs
+ The program will not delete the original folder once it moves file
+ If the file is already there, it is just skipped