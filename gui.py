import Tkinter
from Tkinter import *
import max_flow_ff
fn = max_flow_ff.FlowNetwork()
fn.addVertex('s', True, False)
fn.addVertex('t', False, True)
nodes = 0
names = []
ed = 0
a_list = []

initialize_nodes = Tkinter.Tk()
initialize_nodes.title("Initialization")

def helloCallBack():
    global nodes
    nodes = int(text.get())
    initialize_nodes.destroy()

button = Tkinter.Button(initialize_nodes, text="Enter Nodes", command=helloCallBack)
text = Entry(initialize_nodes, bd=5)
text.pack(side=RIGHT)
button.pack(side=LEFT)

initialize_nodes.mainloop()

#enter node names
for i in range(nodes):
    inputs = Tkinter.Tk()
    inputs.title("Nodes "+str(i))
    def name_callback():
        names.append(str(t2.get()))
        inputs.destroy()
    t1 = Tkinter.Label(inputs, text="Node "+str(i))
    t2 = Tkinter.Entry(inputs, bd=5)
    t3 = Tkinter.Button(inputs, text="Accept", command=name_callback)
    t1.pack()
    t2.pack()
    t3.pack()
    inputs.mainloop()

for i in names:
    fn.addVertex(i)

#enter edges
edges = Tkinter.Tk()
edges.title("edges")

def edges_ip():
    global ed
    ed=int(text1.get())
    edges.destroy()

button1 = Tkinter.Button(edges, text="Enter edges", command=edges_ip)
text1 = Tkinter.Entry(edges, bd=5)
text1.pack(side=RIGHT)
button1.pack(side=LEFT)

edges.mainloop()

#enter weights
for i in range(ed):
    wts = Tkinter.Tk()
    wts.title("Edges "+str(i))
    def addEdge():
        temp = []
        temp.append(str(tx1.get()))
        temp.append(str(tx2.get()))
        temp.append(str(tx3.get()))
        a_list.append(list(temp))
        wts.destroy()

    l1 = Tkinter.Label(wts, text="start")
    l1.grid(row=0, column=0)
    l2 = Tkinter.Label(wts, text="destination")
    l2.grid(row=0, column=1)
    l3 = Tkinter.Label(wts, text="weight")
    l3.grid(row=0, column=2)
    tx1 = Tkinter.Entry(wts, bd=5)
    tx1.grid(row=1, column=0)
    tx2 = Tkinter.Entry(wts, bd=5)
    tx2.grid(row=1, column=1)
    tx3 = Tkinter.Entry(wts, bd=5)
    tx3.grid(row=1, column=2)
    b1 = Tkinter.Button(wts, text="Accept", command=addEdge)
    b1.grid(row=2, column=1)
    wts.mainloop()

for i in range(len(a_list)):
    fn.addEdge(a_list[i][0],a_list[i][1],int(a_list[i][2]))

print fn.calculateMaxFlow()
print [vertex.name for vertex in fn.vertices]
print ['%s -> %s' % (e.start, e.end) for e in fn.getEdges()]

