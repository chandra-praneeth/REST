#!/usr/bin/env python3
import requests
import json

url = "http://api.duckduckgo.com/"
payload = {'q':'chandra','format':'json'}

r = requests.get(url,params = payload)

if r.ok:
	jData = json.loads(r.content.decode("utf-8"))
	
	print(type(jData))

	#print(format(len(jData))+"\n")

	for key in jData:
		print(key+" : " + format(jData[key]))	
else:
	r.raise_for_status()
