#!/usr/bin/env python3
from sys import argv
script,f,output_file=argv
w='github'
read=open(f,'r')
for x in read:
	if w in x:
		continue
	else:
        	print('http://'+x,end='',file=open(output_file,'a'))
