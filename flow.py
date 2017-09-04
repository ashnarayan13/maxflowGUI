import maxflow

#print maxflow.__version__

g = maxflow.Graph[int](100,100)

nodes = g.add_nodes(5)

print nodes

g.add_edge(nodes[0], nodes[2], 4, 0)

g.add_edge(nodes[0], nodes[3], 1, 0)

g.add_edge(nodes[1], nodes[2], 2, 0)

g.add_edge(nodes[1], nodes[4], 6, 0)

g.add_edge(nodes[2], nodes[3], 2, 0)

g.add_edge(nodes[4], nodes[2], 4, 0)

g.add_tedge(nodes[0], 2, 0)

g.add_tedge(nodes[1], 3, 0)

g.add_tedge(nodes[2], 6, 0)

g.add_tedge(nodes[3], 0, 8)

g.add_tedge(nodes[2], 0, 1)

g.add_tedge(nodes[4], 0, 7)

flow = g.maxflow()

print flow
