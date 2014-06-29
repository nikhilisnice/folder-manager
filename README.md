folder-manager
==============

At a scheduled time, I will put photos from a wireless camera into a new folder that is the current date.

https://kb.iu.edu/d/afiz - Useful info about crontab and how to use it
To create the file, use
{{{
crontab -e

}}}
To make the command run daily, put a number for the minute of the day, and a 
number for the hour of the day to be put, in succession with spaces between \
them. Then add a space and an asterix three times. Afterwards, add the
path for the file

i.e. 0 5 * * * /tmp/folder-manager/
