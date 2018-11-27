#!/usr/bin/python

'''
Signup on www.toplinked.com
Download - http://www.toplinked.com/invitemelist/?p=freedownload
'''

import codecs
import sys
import os
import pandas as pd

log = codecs.open("output.txt","w",encoding='utf-8')

Input_filename = sys.argv[1]

df = pd.read_csv(Input_filename)

eng = df.values.T.tolist()

for k in range(0,len(eng[0])):

    print(eng[0][k]) 

    log.write(eng[0][k] + ',')	

