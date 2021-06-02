#!/usr/bin/env python3
from sys import argv
script,f=argv
read=open(f,'r')
for x in read:
        print('http://'+x,end='',file=open('http_sub.txt','a'))
