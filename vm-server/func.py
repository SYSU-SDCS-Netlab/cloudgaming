# -*- coding: utf-8 -*-
import os
import json
import web
import subprocess

urls = (
	'/(.*)/', 'redirect', 
	'/getproc', 'getproc',
	'/rungame', 'rungame',
	'/killga', 'killga',
	)

class redirect:
    def GET(self, path):
        web.seeother('/' + path)
		
class getproc:
	def GET(self):
		process_list = list()
		for line in os.popen('tasklist /nh'):
			process_list.append(line.strip().split(" ")[0])
		return json.dumps(process_list)

class rungame:
	def GET(self):
		game = web.input()
		result = ""
		# if game.id == "1":
		# 	result += "<h2>catch!</h2>"
		# 	subprocess.Popen(r'C:\Users\Cloud_Gaming_VM1\Desktop\gaminganywhere-0.7.5\bin\ga-server-event-driven.exe C:\Users\Cloud_Gaming_VM1\Desktop\gaminganywhere-0.7.5\bin\config\server.assaultcube.win32.conf')
		subprocess.Popen(r'C:\Users\Cloud_Gaming_VM1\Desktop\gaminganywhere-0.7.5\bin\ga-server-event-driven.exe C:\Users\Cloud_Gaming_VM1\Desktop\gaminganywhere-0.7.5\bin\config\server.%s.conf' %game.name)
		return result+"<h1>"+game.name+"</h1>"
		
class killga:
	def GET(self):
		subprocess.Popen(r'taskkill /im ga-server-event-driven.exe /t')
		return "SUCCESS"
    	
application = web.application(urls, globals()).wsgifunc()
