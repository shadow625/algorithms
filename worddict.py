import re

class WordDict(object):
	"""docstring for WordDict"""
	def __init__(self):
		self.root=node(None)
	def addWord(self,word):
		root=self.root
		for x in word:
			#print x
			if root.haskey(x):
				pass
			else:
				root.addNode(x,node(x))
			root=root.getNext(x)
	def search(self,word):
		return self.search_in(word,self.root)
	def search_in(self,word,root):
		print word[0]
		target=word[0]
		
		if target=='.':
			print 'match every letter'
			print "root keys:"+repr(root.getKeys())
			for x in root.getKeys():
				print "x->"+x
				if len(word)>1:
					if word[1] in root.getNext(x).getKeys():
						print 1
						self.search_in(word[1:],root.getNext(x))
		else:
			if len(word)>1:
				if word[1] in root.getNext(x).getKeys():
					self.search_in(word[1:],root.getNext(target))
				else:
					return False
		return True

	def echoDic(self,root):
		for x in root.getKeys():
			print x,
			self.echoDic(root.getNext(x))
			print ""
	def echo(self):
		self.echoDic(self.root)
class node(object):
	"""docstring for node"""
	def __init__(self,key):
		self.key=key
		self.next={}
	def addNode(self,key,node):
		if key not in  self.next.keys():
			self.next[key]=node
		return self.next[key]
	def getKeys(self):
		return self.next.keys()

	def getNext(self,key):
		return self.next[key]
	def haskey(self,x):
		if x in self.next.keys():
			return True
		else:
			return False
	


if __name__ == '__main__':
	test=WordDict()
	test.addWord('hello')
	test.addWord('word')
	test.addWord('aadd')
	test.addWord('ward')
	#test.echo()
	#x=raw_input("the target->")
	print test.search(".llo")