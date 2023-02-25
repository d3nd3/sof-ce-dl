import requests
import sys

def errorExit(r):
	if r.status_code != 200:
		print("error")
		sys.exit(1)
version="7"
url = f"https://www.sof1.org/download/Soldier_of_Fortune_Community_Edition_V{version}.exe"

s = requests.Session()
s.headers.update( {"User-Agent" : "Mozilla/5.0 (X11; CrOS aarch64 13597.84.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.57 Safari/537.36",
"Accept-Encoding" : "gzip, deflate, br",
"Accept-Language" : "en-GB,en-US;q=0.9,en;q=0.8",
"Pragma" : "no-cache",
"Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
})
r=s.get("https://www.sof1.org/app.php/sof1-download")
errorExit(r)
r=s.get(url,headers={"Referer":"https://www.sof1.org/app.php/sof1-download"})
errorExit(r)


with open("sof_ce_installer.exe", "wb") as f:
    f.write(r.content)
print("done")
