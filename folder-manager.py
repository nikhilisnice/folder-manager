import codecs

f = codecs.open('sample_filenames.txt', 'r', 'utf-8')
folders = []
expectedOutput = [u'20130113', u'20130113', u'20130113', u'20130113', u'20130113', u'20130113', u'20140613', u'20140613', u'20140613', u'20140613', u'20140613', u'20140613', u'20140613', u'20140613', u'20140613', u'20140613', u'20140613', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614', u'20140614']

for line in f:
  myline = line.lstrip( unicode( codecs.BOM_UTF8, "utf8" ) )
  folderdate = myline[8:16]
  folders.append(folderdate)
print folders
if expectedOutput == folders:
	print "Success!"
else:
	print "Try again...:("
