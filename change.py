#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import sys

if len(sys.argv) < 2:
	print "Please , enter the file name."
elif len(sys.argv) > 2:
	print "You have entered many files name."
else:
	page_name = sys.argv[1]
	page = urllib.urlopen(page_name)

	page_chance=""
	for i in page.read():
		if i=="<":
			page_chance=page_chance+"&lt;"
		elif i==">":
			page_chance=page_chance+"&gt;"
		else:
			page_chance=page_chance+i

	page_crate = open("new.html","w")
	page_crate.write(page_chance)
	page.close()
	page_crate.close()
