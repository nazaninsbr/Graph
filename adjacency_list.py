class Node:
	def __init__(self, value, next='/'):
		self.value = value
		self.next = next

	def getNext(self):
		return self.next

	def getValue(self):
		return self.value

	def setNext(self, next):
		self.next = next

	def setValue(self, value):
		self.value = value


class Graph:
	def __init__(self, number_of_nodes):
		self.number_of_nodes = number_of_nodes
		self.nodes = []
		self.create_initial_nodes()

	def create_initial_nodes(self):
		for x in range(self.number_of_nodes):
			self.nodes.append(0)

	def findLastNode(self, first_node):
		node = first_node
		while not node.getNext()=='/':
			node = node.getNext()
		return node

	def addEdge(self, node1, node2):
		if self.nodes[node1-1]==0:
			newNode = Node(node2-1)
			self.nodes[node1-1]= newNode
		else:
			newNode = Node(node2-1)
			last_node = self.findLastNode(self.nodes[node1-1])
			last_node.setNext(newNode)

		if self.nodes[node2-1]==0:
			newNode = Node(node1-1)
			self.nodes[node2-1]= newNode
		else:
			newNode = Node(node1-1)
			last_node = self.findLastNode(self.nodes[node2-1])
			last_node.setNext(newNode)

	def printNodeList(self, node, nodeNumber):
		if node==0:
			print('node {} has no edges'.format(nodeNumber+1))
		else:
			output = ''
			while not node=='/':
				output = output+str(node.getValue()+1)+' '
				node = node.getNext()
			print('node {} -> {}'.format(nodeNumber+1, output))

	def printMatrix(self):
		for nodeId in range(0, self.number_of_nodes):
			self.printNodeList(self.nodes[nodeId], nodeId)
		

g = Graph(5)
g.addEdge(1, 2)
g.addEdge(4, 2)
g.addEdge(5, 2)
g.printMatrix()