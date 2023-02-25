import requests
import sys
import random
import string
from urllib.parse import urlparse
from urllib.parse import parse_qs

#nc -k 8765

sid_id = "ghtfd"
ce_ver = "7"
def knock_knock(sid,stage):
	formdata = {'username' : 'sofce' , 'password' : 'sofcesofce', 'sid' : sid, 'login' : 'Login','autologin' : 'on', 'redirect' : './index.php'}
	if stage == 1:
		#get cookies
		r = s.get("https://www.sof1.org/index.php")
		#r = s.get("http://localhost:8765")
	if stage == 2:
		r = s.get("https://www.sof1.org/ucp.php?mode=login&sid={sid}")
	elif stage == 3:
		#prepare for redirect
		r = s.post("https://www.sof1.org/ucp.php?mode=login",data=formdata,headers={'Referer': "https://www.sof1.org/ucp.php?mode=login&sid={}".format(sid),"Origin" : "https://www.sof1.org"})
		#r = s.post("http://localhost:8765",data=formdata)

	print(r.status_code)
	if r.status_code == 200:
		print("acquired logged cookies")
	elif r.status_code == 302:
		print("got the redirect!")
	else:
		print("error logging in")
		print(r.text)
		sys.exit(1)

	if stage == 3 :
		print("Expecting location header")
		print(r.headers)
		#sys.exit(0)
		#p = urlparse(r.headers['location'])
		#given_sid = urlparse.parse_qs(p.query)['sid'][0]
		given_sid = s.cookies["phpbb3_" + sid_id + "_sid"]
		print("your sid is : {}".format(given_sid))
		#sys.exit(0)
		#pass
	print(s.cookies.get_dict())
	return r

s = requests.Session()
s.headers.update( {"User-Agent" : "Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.57 Safari/537.36",
"Accept-Encoding" : "gzip, deflate, br",
"Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8",
"Pragma" : "no-cache",
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
})
#sid = int.from_bytes(random.randbytes(16),"little")
#generated_sid = f"{sid:x}"
#print(generated_sid)

#https://www.sof1.org/ucp.php?mode=login&redirect=.%2Findex.php

#when you do not specify cookie, you receive cookie
knock_knock("0000",1)
new_sid = s.cookies["phpbb3_" + sid_id + "_sid"]
print("here it is : {}".format(new_sid))

knock_knock(new_sid,2)
#sys.exit(0)
#share initial cookie and get final cookie
knock_knock(new_sid,3)

r = s.get("https://www.sof1.org/download/Soldier_of_Fortune_Community_Edition_V" + ce_ver + ".exe",headers={"Referer":"https://www.sof1.org/sofdownload.php"})
print(r.status_code)
if r.status_code != 200:
	print("error getting file url")
	sys.exit(1)

with open("sof_ce_installer.exe", "wb") as f:
    f.write(r.content)
print("done")

