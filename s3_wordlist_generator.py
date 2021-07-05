#!/usr/bin/env python3
#syntex = python3 s3_wordlist_generator.py wordlist_name.txt
from sys import argv
script,f=argv
read=open(f,'r')
for x in read:
	print(x,end='',file=open('aws_s3_wordlist.txt', 'a'))
	print("-"+x,end='',file=open('aws_s3_wordlist.txt', 'a'))
	print("."+x,end='',file=open('aws_s3_wordlist.txt', 'a'))
	print("_"+x,end='',file=open('aws_s3_wordlist.txt', 'a'))
