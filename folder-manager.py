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

inputfolder = '/home/nikhil/Documents/Test-For-Folder-Thing'
outputfolder = '/tmp/folder-manager'
filenamelist = os.listdir(inputfolder)

for filename in filenamelist:
  folderdate = filename[8:16]
  filenamecheck = filename[0:3]
  if filenamecheck == "DCS":
	mkdir_p(os.path.join(outputfolder, folderdate))
	shutil.move((os.path.join(inputfolder, filename)), os.path.join(outputfolder, folderdate, filename))
