class Graph:
	def __init__(self, number_of_nodes):
		self.number_of_nodes = number_of_nodes
		self.matrix = []
		self.create_matrix()

	def create_matrix(self):
		for x in range(self.number_of_nodes):
			v = []
			for x in range(self.number_of_nodes):
				v.append(0)
			self.matrix.append(v)

	def addEdge(self, node1, node2):
		self.matrix[node1-1][node2-1] = 1
		self.matrix[node2-1][node1-1] = 1

	def printMatrix(self):
		for row in self.matrix:
			print(row)

g = Graph(5)
g.addEdge(1, 2)
g.addEdge(4, 2)
g.addEdge(5, 2)
g.addEdge(1, 3)
g.printMatrix()