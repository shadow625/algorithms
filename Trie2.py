#/usr/bin/env python
#implement the trie by chain data structure
class Node(object):#that is the node object ,the components of the trie
	"""docstring for Node"""
	def __init__(self, cha):
		self.cha = cha
		self.childs=[]#init the node of the 

class Word(object):
	"""docstring for Word"""
	def __init__(self):
		self.root=Node(None)# init the root node. And it has  
		
	def addNode(self,roo,word):
		if len(word)==0:
			return None#return None if the length of the word need to be added is null
		print word
 		cha = word[0]
 		word=word[1:]
 		roo.childs.append(Node(cha))
 		for i in roo.childs:
 			print "cha"+i.cha
 		pos=self.find(roo.childs,cha)
 		if pos==None:
 			return
 		self.addNode(roo.childs[pos],word)
 		
 	def find(self,nodes,cha):
 		for i in range(0,len(nodes)):
 			if nodes[i].cha==cha:
 				print i
 				return i
 		return

 	def find_in(self,root,word):
 		for i in root.childs:
 			if word!=None:
 				print word[0]
 				if i.cha==word[0]:
 					print "match:->"+word[0]
 					self.find_in(i,word[1:])

 	def find2():
 		pass

 	def show(self,root):
 		if root.cha==None:
 			print 'O->',
 		else:
 			print root.cha,
 		for i in root.childs:
 			self.show(i)
 		
if __name__ == '__main__':
	word=Word()
	word.addNode(word.root,'hello')
	word.addNode(word.root,'but')
	word.show(word.root)