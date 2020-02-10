from requests import get
from multiprocessing import Pool
from sys import exit, argv

def check(name):
	name = name.strip()
	if (get("https://google.com").status_code) != 200:
		print("No connection")
		return()
	statusCode = get("https://github.com/" + name).status_code
	if statusCode == 404:
		return(name)

# set thread count
threads = Pool(processes=100)

try:
	with open(argv[1],"r") as file:
		lines = file.readlines()
		results = threads.map(check,lines)
		for i in results:
			if i != None: print(i)
except KeyboardInterrupt: sys.exit()


