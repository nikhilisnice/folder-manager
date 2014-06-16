import codecs
import os, errno

def mkdir_p(path):
	try:
		os.makedirs(path)
	except OSError as exc:
		if exc.errno == errno.EEXIST and os.path.isdir(path):
			pass
		else: raise
		
def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)

f = codecs.open('sample_filenames.txt', 'r', 'utf-8')
folders = []
outputfolder = '/tmp/folder-manager'
for line in f:
  myline = line.lstrip( unicode( codecs.BOM_UTF8, "utf8" ) )
  filename = myline
  folderdate = myline[8:16]
  folderdatestring = str(folderdate)
  folders.append(folderdate)
  mkdir_p (os.path.join(outputfolder, folderdatestring))
  touch (os.path.join(outputfolder, folderdatestring, filename))
