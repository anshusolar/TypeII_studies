#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:34:26 2019

@author: anshu
"""

import glob
import numpy as np
#path = '/home/anshu/Desktop/events/2018_events'
files = [f for f in glob.glob("**/2019*.txt", recursive=True)]
files.sort()
for f in files:
    print(f)
    
num = np.size(files)


def find(substr, infile, outfile):
  with open(infile) as a, open(outfile, 'w') as b:
   for line in a:
    if substr in line:
     b.write(line + '\n')

k=['II',':Product:']
searchstrings = ('II', 'Product')

for i in files:
    print('-'*90)#just a line to distinguish between all the outputs
    print(i)
    print('*'*len(i))#just some underlining

    with open(i,'r') as f:
        for line in f.readlines():
            #print(line)
            with open('test1.txt', 'a') as file:
                file.write(line)
                for word in searchstrings:
                    if word in line:
                        print(line,file=open("test2.txt", "a"))


bad_words = ['III','VII']

with open('test2.txt') as oldfile, open('test3.txt', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)

with open('test3.txt', 'r+') as fd:
    lines = fd.readlines()
    fd.seek(0)
    fd.writelines(line for line in lines if line.strip())
    fd.truncate()


#####################################
    
    ## to combine everythng###
    
#import os
#filelist = os.listdir(os.getcwd())
#filelist.sort()
#
#for i in filelist:
#    print('-'*90)#just a line to distinguish between all the outputs
#    print(i)
#    print('*'*len(i))#just some underlining
#    try:
#        with open(i,'r') as f:
#            for line in f.readlines():
#                print(line)
#                with open('test.txt', 'a') as file:
#                    file.write(line)   
#
#    except:
#        pass
#        