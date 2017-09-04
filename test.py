import GraphTool
import Tkinter
from Tkinter import *

fn = GraphTool.Flow()
links = []
capacities = []
node_name = []
nodes = 0
edges = 0
newData = True

initialize = Tkinter.Tk()
initialize.title("Start")
def loadGraph():
    global fn, newData
    newData = False
    fn.graph_init(True, filename.get())
    initialize.destroy()
def openGraph():
    global fn
    fn.graph_init(False)
    initialize.destroy()
oldGraph = Tkinter.Button(initialize, text="Load", command=loadGraph)
newGraph = Tkinter.Button(initialize, text="New", command=openGraph)
filename = Tkinter.Entry(initialize, bd=5)
oldGraph.grid(row=1,column=0)
newGraph.grid(row=0,column=0)
filename.grid(row=1,column=1)
initialize.mainloop()

if newData:
    nodes_edges = Tkinter.Tk()
    nodes_edges.title("Nodes and edges")
    def neSave():
        global nodes,edges
        nodes = int(nodesIP.get())
        edges = int(edgesIP.get())
        nodes_edges.destroy()
    nodesL = Tkinter.Label(nodes_edges, text="Nodes")
    edgesL = Tkinter.Label(nodes_edges, text="Edges")
    nodesIP = Tkinter.Entry(nodes_edges, bd=5)
    edgesIP = Tkinter.Entry(nodes_edges, bd=5)
    nodes_edgesOK = Tkinter.Button(nodes_edges, text="OK", command=neSave)
    nodesL.grid(row=0,column=0)
    edgesL.grid(row=0,column=1)
    nodesIP.grid(row=1,column=0)
    edgesIP.grid(row=1,column=1)
    nodes_edgesOK.grid(row=2,column=0)
    nodes_edges.mainloop()

for i in range(edges):
    connections = Tkinter.Tk()
    connections.title("Connection")
    def addEdge():
        global links,capacities
        links.append([vertex1T.get(), vertex2T.get()])
        capacities.append(weightT.get())
        connections.destroy()
    vertex1T = Tkinter.Entry(connections, bd=5)
    vertex2T = Tkinter.Entry(connections, bd=5)
    vertex1L = Tkinter.Label(connections, text="Vertex1")
    vertex2L = Tkinter.Label(connections, text="Vertext2")
    weightT = Tkinter.Entry(connections, bd=5)
    weightL = Tkinter.Label(connections, text="Weight")
    addEdgeOK = Tkinter.Button(connections, text="Add Edge", command=addEdge)
    vertex1L.grid(row=0,column=0)
    vertex2L.grid(row=0, column=1)
    weightL.grid(row=0, column=2)
    vertex1T.grid(row=1, column=0)
    vertex2T.grid(row=1, column=1)
    weightT.grid(row=1, column=2)
    addEdgeOK.grid(row=2, column=1)
    connections.mainloop()

fn.load_graph(nodes, edges, links, capacities)

final = Tkinter.Tk()
final.title("MaxFlow")

def calcMax():
    global fn
    global node_name
    fn.max_flow(int(sourceT.get()), int(targetT.get()), saveFileT.get())
    if node_name:
        fn.addVertex(node_name)

def disp():
    global fn
    fn.display_graph()

def interact():
    global fn
    fn.graph_interact()

def addData():
    global fn
    global node_name
    global nodes
    for i in range(nodes):
        def addVal():
            if i<=nodes:
                node_name.append(vertexT.get())
                vertexT.delete(0, 'end')
            else:
                vertexB.destroy()
                vertexL.destroy()
                vertexT.destroy()

        vertexL = Tkinter.Label(final, text="Vertex Name")
        vertexT = Tkinter.Entry(final, bd=5)
        vertexB = Tkinter.Button(final, text="Ok", command=addVal)
        vertexL.grid(row=3,column=0)
        vertexT.grid(row=3, column=1)
        vertexB.grid(row=3, column=2)

def quitMax():
    final.destroy()
sourceT = Tkinter.Entry(final, bd=5)
targetT = Tkinter.Entry(final, bd=5)
sourceL = Tkinter.Label(final, text="Source")
targetL = Tkinter.Label(final, text="Target")
saveFileT = Tkinter.Entry(final, bd=5)
saveFileL = Tkinter.Label(final, text="File Name")
maxflow = Tkinter.Button(final, text="Maxflow", command=calcMax)
displayGraph = Tkinter.Button(final, text="Display Graph", command=disp)
interactGraph = Tkinter.Button(final, text="Interact", command=interact)
quitAll = Tkinter.Button(final, text="Quit", command=quitMax)
add_properties = Tkinter.Button(final, text="Add Properties", command=addData)
sourceL.grid(row=0,column=0)
sourceT.grid(row=1,column=0)
targetL.grid(row=0,column=1)
targetT.grid(row=1,column=1)
saveFileL.grid(row=0,column=2)
saveFileT.grid(row=1,column=2)
maxflow.grid(row=2,column=0)
displayGraph.grid(row=2,column=1)
interactGraph.grid(row=2,column=2)
quitAll.grid(row=2,column=3)
add_properties.grid(row=2, column=4)
final.mainloop()