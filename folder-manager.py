import os, errno
import shutil
from os import listdir
from os.path import isfile, join

def mkdir_p(path):
  try:
    os.makedirs(path)
  except OSError as exc:
    if exc.errno == errno.EEXIST and os.path.isdir(path):
       pass
    else: raise

def touch(fname):
    try:
        os.utime(fname, None)
    except:
        open(fname, 'a').close()
        
def mov_files(inputfolder, outputfolder, ds, de):
	filenamelist = os.listdir(inputfolder)
	for filename in filenamelist:
	  folderdate = filename[ds:de]
	  filenamecheck = filename[0:3]
	  if (filenamecheck == "DCS" or filenamecheck == "78A"):
		mkdir_p(os.path.join(outputfolder, folderdate))
		shutil.move((os.path.join(inputfolder, filename)), os.path.join(outputfolder, folderdate, filename))
inputfolder = '/home/nikhil/Documents/Test-For-Folder-Thing'
inputfolder2 = '/home/nikhil/Documents/tf2'
outputfolder = '/tmp/folder-manager'

mov_files(inputfolder, outputfolder, 8, 16)
mov_files(inputfolder2, outputfolder, 24, 32)
