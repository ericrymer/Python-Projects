import shutil
import os
import time

SECONDS_IN_DAY = 24 * 60*60 

#set where the source of the files are
source = 'C:/Users/ericr/Desktop/Folder A/'

#set the destinaton path to folder b
destination =  'C:/Users/ericr/Desktop/Folder B/'

now = time.time()
before = now - SECONDS_IN_DAY

#define function time
def last_mod_time(fname):
    return os.path.getmtime(fname)


for fname in os.listdir(source):
    src_fname = os.path.join(src, fname)
    if last_mod_time(source_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.move(src_fname, dst_fname)

