#!/bin/python3
from requests import head
from multiprocessing import Pool
from sys import exit, argv

def check(name):
	name = name.strip()
	#if (head("https://www.google.com").status_code) != 200:
		#print("No connection")
		#return()
	statusCode = head("https://github.com/" + name).status_code
	if statusCode == 404:
		with open('result.txt', mode='a+') as filename:
			filename.write(name+'\n')
		print(name)
		return(name)

# set thread count
if len(argv) == 3:
	threads = Pool(processes=int(argv[2]))
else: threads = Pool(processes=100)

try:
	with open(argv[1],"r") as file:
		lines = file.readlines()
		results = threads.map(check,lines)
		for i in results:
			if i != None: print(i)
except KeyboardInterrupt: sys.exit()


