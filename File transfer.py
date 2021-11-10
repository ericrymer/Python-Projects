import shutil
import os
import time

SECONDS_IN_DAY = 24 * 60*60 

#set where the source of the files are
src = "C:\Users\Student\Desktop\FolderA"

#set the destinaton path to folder b
dst = "C:\Users\Student\Desktop\FolderB"

now = time.time()
before = now - SECONDS_IN_DAY

#define function time
def last_mod_time(fname):
    return os.path.getmtime(fname)


for fname in os.listdir(src):
    src_fname = os.path.join(src, fname)
    if last_mod_time(src_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.move(src_fname, dst_fname)

