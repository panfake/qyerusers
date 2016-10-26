#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-03-14 11:45:33
# @Author  : PanFake

import os
from multiprocessing.dummy import Pool as ThreadPool
import urllib2
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8') #允许打印unicode字符

def get(userid):
	url = "http://www.qyer.com/u/%s/place-comment" %userid
	# url = "http://www.qyer.com/u/704/place-comment" #指定用户测试
	try:
		content = urllib2.urlopen(url)
	except urllib2.HTTPError,e:
		content = ""
		pass
	except urllib2.URLError,e:
		content = ""
		pass
	if content == "":
		print userid , "is Blocked."
		pass
	else:
		soup = BeautifulSoup(content)
		username = str(soup.find_all(attrs={"data-bn-ipg": "usercenter-username"})[0].text)
		if username=="" :
			print userid , "does not exist."
			pass
		else:
			comments = str(soup.find_all("span", class_="tag")[2].text)
			comments = filter(str.isdigit, comments)
			if int(comments)>500:
				output = open('500.txt', 'a')
				txt500 = "%s | %s | %s | %s\n" %(userid , username , url , comments)
				output.write(txt500)
				output.close()
				pass
			print userid ," | ", username ," | ", url , " | ", comments
			output = open('result.txt', 'a')
			txt = "%s | %s | %s | %s\n" %(userid , username , url , comments)
			output.write(txt)
			output.close()

if __name__ == '__main__':
	maximum_userid = input("Please input maximum_userid:\n")
	print ">>>>>>The maximum_userid is" , maximum_userid
	userids = range(1 , maximum_userid+1)
	pool = ThreadPool(30)
	results = pool.map(get, userids)
	pool.close()
	pool.join()
	print ">>>>>>All Done!"
