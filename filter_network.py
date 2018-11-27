#!/usr/bin/python

'''
Watch this video on youtube
Signup on www.toplinked.com
Download - http://www.toplinked.com/invitemelist/?p=freedownload
'''

import codecs
import sys
import os
import pandas as pd
import time

log = codecs.open("Filter_output.txt","w",encoding='utf-8')

Input_filename = sys.argv[1]

df = pd.read_csv(Input_filename)

eng = df.values.T.tolist()

#ignore list
notlist = ['@gmail.com','@yahoo.com','@hotmail.com','@googlemail.com','@outlook.com','@comcast.net','sales','gmail','@aol.com','@msn.com','.CC','marketing','mail','AOL.com','yahoo.co','@me.com','@webbsite.me','me@','@yahoo','insurance','building','construction','.COM']

for ext in notlist:		

    for eml in eng[0]:
	
        if ext in eml:	
		
		     eng[0].remove(eml)		

log.write(str(eng[0]).replace('[','').replace(']',',').replace("'",""))