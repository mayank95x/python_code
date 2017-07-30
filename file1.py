import networkx as nx

import matplotlib.pyplot as plt



G=nx.Graph()

G.add_node(1)

G.add_nodes_from([2,3])

G.add_edge(1,2)

e=(2,3)

 G.add_edge(*e)

 G.number_of_nodes()

 G.number_of_edges()

 G.nodes()

 G.neighbors(1)

 G.add_edge(1,3)

 G[1][3]['color']='blue'

 #Access to all edges

 for (u,v,d) in FG.edges(data='weight'):
...     if d<0.5: print('(%d, %d, %.3f)'%(n,nbr,d))



#Assign graph attributes when creating a new graph

G = nx.Graph(day="Friday")
G.graph



G.add_node(1, time='5pm')


#Directed graphs
DG=nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5), (3,1,0.75)])
DG.out_degree(1,weight='weight')


DG.degree(1,weight='weight')
DG.successors(1)
DG.neighbors(1)

nx.draw(G)
