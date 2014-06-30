import os, errno
import shutil
import argparse
from os import listdir
from os.path import isfile, join

parser = argparse.ArgumentParser(description='')
parser.add_argument("inputfolders", nargs="+", help = 'Select the input folder(s) for the program. Add the input folders&#39; paths on top ')
args = parser.parse_args()

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
        
def mov_files(inputfolder, outputfolder):
  filenamelist = os.listdir(inputfolder)
  for filename in filenamelist:
    filenamecheck = filename[0:3]
    if filenamecheck == "DCS":
      ds = 8
      de = 16
    elif filenamecheck == "78A":
      ds = 24
      de = 32
    folderdate = filename[ds:de]
    if (filenamecheck == "DCS" or filenamecheck == "78A"):
      mkdir_p(os.path.join(outputfolder, folderdate))
      shutil.move((os.path.join(inputfolder, filename)), os.path.join(outputfolder, folderdate, filename))
#inputfolder = '/media/untitled/ftp/pi/files/files/ipcam'
inputfolders= args.inputfolders
outputfolder = '/tmp/folder-manager'


#mov_files(inputfolder, outputfolder, 8, 16)
for folder in inputfolders:
  mov_files(folder, outputfolder)
