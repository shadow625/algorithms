#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,re
"""this class is designed to analysis the smali files of the android apks
it will give a collection of all the important components in a highly organized way 
well i think that won't be hard to read ,so that's it:it's a doc   ｡◕‿◕｡
""" 

class Inventory:
	
	def __init__(self,location):
		self.location     	= location
		self.AppInventory 	= {}

	def do_walk(self):
		self.AppInventory = {}
		for root, dirs, files in os.walk( self.location ):
			for file in files:
				if file.endswith(".smali"):
					with open(root+"/"+file, "r") as file_handle:
						#print 'base 29true file:'+file
						content = file_handle.read()
						mid = re.search('^\.class\s+(.*?)(\r|\n)\.super\s+(.*?)(\r|\n)\.source\s+(.*?)(\r|\n)', content)
						if not mid:
							break
						class_name=mid.groups()[0].split(' ')[-1]
						self.AppInventory[class_name] = {}
						self.AppInventory[class_name]['Properties'] = re.findall('[.]field\s+(.*?)(\r|\n)', content, re.DOTALL)
						self.AppInventory[class_name]['Methods'] = []
						for m in re.findall('[.]method\s+(.*?)\n+(.*?)[.]end\s+method', content, re.DOTALL):
							ind_meth = {}
							ind_meth['Name'] = m[0].split(' ')[-1]
							ind_meth['Instructions'] = []
							for i in m[1].split('\n'):
								if len(i)>0:
									ind_meth['Instructions'].append( i.lstrip().rstrip() )
							self.AppInventory[class_name]['Methods'].append( ind_meth )
		return self.AppInventory
