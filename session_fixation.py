

import requests
import sys
import getpass

if len(sys.argv) !=2:
	print("USAGE: %s URL" %(sys.argv[0]))
	sys.exit(0)


url = str(sys.argv[1])
login = str(input("Type login:  "))
password = getpass.getpass("Type password:  ")
req = requests.get(url)


if req.cookies:
	print ("Initial cookies state: ".upper(), req.cookies)
	cookie_req = requests.post(url, cookies=req.cookies, auth=(login, password))
	print("Authenticated cookie state: ".upper(), cookie_req.cookies)
	if req.cookies == cookie_req.cookies:
		print("Session fixation vulnerability identified")
