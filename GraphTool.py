from graph_tool.all import *
import cv2

class Flow:
    def __init__(self):
        self.load = True
        self.g = Graph()
        self.n = 0
        self.edges = 0
        self.res = 0
        self.src = 0
        self.tgt = 0
        self.vx = False

    def graph_init(self, load, file=None):
        self.load = load
        if self.load:
            self.file = file
            self.file = self.file + ".xml.gz"
            self.g = graph_tool.load_graph(self.file)
        else:
            self.g = Graph()

    def edit_graph(self):
        if self.load:
            for v in self.g.vertices():
                print(v)
            for e in self.g.edges():
                print(e)

    def addVertex(self, vertex):
        counter = 0
        for v in self.g.vertices():
            self.vprop[v] = vertex[counter]
            counter = counter+1
        self.g.vertex_properties["name"] = self.vprop
        self.vx = True

    def load_graph(self, n=None, edges=None, links=None, weights=None):
        if self.load == False:
            self.n = n
            self.g.add_vertex(self.n)
            self.edges = edges
            self.cap = self.g.new_edge_property('int')
            self.vprop = self.g.new_vertex_property("string")
            for i in range(self.edges):
                self.g.add_edge(links[i][0], links[i][1])
            counter = 0
            for e in self.g.edges():
                self.cap[e] = weights[counter]
                counter = counter+1
            self.g.edge_properties["cap"] = self.cap
        else:
            self.n = len(list(self.g.vertices()))
            self.edges = len(list(self.g.edges()))
            self.cap = self.g.edge_properties["cap"]
            self.vprop = self.g.vertex_properties["name"]

    def max_flow(self, src, tgt, file=None):
        if self.load:
            self.src = src
            self.tgt = tgt
            self.res = graph_tool.flow.edmonds_karp_max_flow(self.g, self.src, self.tgt, self.cap)
            self.res.a = self.cap.a - self.res.a
            self.output = self.file
            self.output = self.output[:-7]
            self.output = self.output + ".png"
            if len(list(self.vprop))>1:
                print("Entered vprop")
                graph_draw(self.g, vertex_text=self.g.vertex_properties["name"], edge_text=self.res, output=self.output)
            else:
                graph_draw(self.g, vertex_text=self.g.vertex_index, edge_text=self.res, output=self.output)
            self.g.save(self.file)
        else:
            self.src = src
            self.tgt = tgt
            self.res = graph_tool.flow.edmonds_karp_max_flow(self.g, self.src, self.tgt, self.cap)
            self.res.a = self.cap.a - self.res.a
            self.output = str(file)
            self.output = self.output + ".png"
            if self.vx or self.load:
                print("Entered vprop")
                graph_draw(self.g, vertex_text=self.g.vertex_properties["name"], edge_text=self.res, output=self.output)
            else:
                graph_draw(self.g, vertex_text=self.g.vertex_index, edge_text=self.res, output=self.output)
            self.file = str(file)
            self.file = self.file + ".xml.gz"
            self.g.save(self.file)


    def display_graph(self):
        img = cv2.imread(self.output)
        cv2.imshow('Flow', img)

    def graph_interact(self):
        if self.load or self.vx:
            graph_tool.draw.interactive_window(self.g, vertex_text=self.g.vertex_properties["name"], edge_text=self.res)
        else:
            graph_tool.draw.interactive_window(self.g, vertex_text=self.g.vertex_index, edge_text=self.res)


'''
g = Graph()

n = input('Enter the number of nodes')

vlist = g.add_vertex(n)

edges = input('Enter the number of edges')

for i in range(edges):
    temp = raw_input('Enter the vertices').split()
    g.add_edge(g.vertex(temp[0]), g.vertex(temp[1]))

cap = g.new_edge_property("int")
for e in g.edges():
    cap[e] = randint(1,9)

g.edge_properties["cap"] = cap

temp = raw_input('Enter source and target').split()
src, tgt = temp[0], temp[1]

res = graph_tool.flow.boykov_kolmogorov_max_flow(g, src, tgt, cap)

res.a = cap.a - res.a

graph_draw(g, vertex_text=g.vertex_index, edge_text=res, output="two-nodes.pdf")
g.save("basic.xml.gz5")
'''