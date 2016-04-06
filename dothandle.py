#******************************************************
# you jusst need to use the two important function add_edge(a,b) and find_ALL_routes(y)
#i give an example at the end of the program
# 


class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		super(Graph, self).__init__()
		self.inventory=[]
		self.neighber={}
		self.visited={}
	def add_node(self , dot):
		if not dot in self.nodes():
			self.neighber[dot]=[]
#-------------------------------------------------------
#add an edge for the graph. it take two parameters which means wanna add an edge from dot1 to dot2 
	def add_edge(self,dot1,dot2):#expand the edge of the graph
		if dot1 not in self.nodes():
			self.add_node(dot1)

		if dot2 not in self.nodes():
			self.add_node(dot2)

		if (dot2 not in self.neighber[dot1] ):
			self.neighber[dot1].append(dot2)
#--------------------------------------------------
#that is the main function i use to implement the func 
# so it's out of your concern
#---------------------------------------
	def find_routes(self,start,end,path=[]):
		path=path + [start]
		if start==end:
			return [path]
		if start not in self.nodes():
			return []
		paths =[]
		for node in self.neighber[start]:
			if node not in path:
				newpaths=self.find_routes(node ,end ,path)
				for newpath in newpaths:
					paths.append(newpath)
		return paths

#----------------------------------------------------------
# the final function  ,return a dict which have all the roads from dot(the start you define) to all the end
#----------------------------------------------------------
	def find_ALL_routes(self,dot):
		final_result={}
		print self.neighber.keys()
		for x in self.neighber:
			if self.neighber[x]==[]:
				final_result['%s->%s '%(dot,x)]=self.find_routes(dot,x)
		return final_result		
	def nodes(self):
		return self.neighber.keys()
#example  
if __name__ == '__main__':
	hello=Graph()
	hello.add_edge('a','b')
	hello.add_edge('b','c')
	hello.add_edge('b','d')
	hello.add_edge('c','e')
	hello.add_edge('d','y')
	hello.add_edge('e','g')
	hello.add_edge('e','f')

	result=hello.find_ALL_routes('a')
	print result