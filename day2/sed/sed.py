#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sys
file = sys.argv[1]
oldfile = sys.argv[2]
newfile = sys.argv[3]
f = open(file,"r")
f2 = open("tmp_file","w")
for line in f:
    if oldfile in line:
        line= line.replace(oldfile,newfile)
        f2.write(line)
        f2.flush()
f.close() 
f2.close()
os.remove(file)
os.rename("tmp_file",file)