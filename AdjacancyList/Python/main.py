from AdjacancyList import AdjacancyList
#       A   B   C

# A     0   15  0
# B     15  0   9
# C     0   9   0

Graph = AdjacancyList()


Graph.Add_Edge('A', 'A', 0)
Graph.Add_Edge('A', 'B', 15)
Graph.Add_Edge('A', 'C', 0)

Graph.Add_Edge('B', 'A', 15)
Graph.Add_Edge('B', 'B', 0)
Graph.Add_Edge('B', 'C', 9)

Graph.Add_Edge('C', 'A', 0)
Graph.Add_Edge('C', 'B', 9)
Graph.Add_Edge('C', 'C', 0)

print(Graph.Search('B', 'C'))
print(Graph.Search('C', 'B'))
print(Graph.Search('A', 'B'))
