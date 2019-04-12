import numpy as np
import time
import  networkx as nx
import pydot
import os
start = time.time()
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'


matrix = []
with open("matrix.txt") as f :
    first_line = f.readline()
    for line in f:
        digits = []
        data = line.split()        
        for number in data:   
            if number == line[0]  or number == '\n':
                #print(number)
                continue
            else:
                #print(number)
                digits.append(number)
        digits = [[int(i) for i in digits]]     
        matrix.extend(digits)
       

matrix = np.array(matrix)
letters = []
first_line = first_line.split()
for let in first_line :
    if let == '-':
        continue
    letters.append(let)



G = pydot.Dot(graph_type='digraph')

#letters = ['A','B','C','D','E']
'''
matrix = np.array([[0, 2, 3, 4, 5],
[2, 0, 3, 4, 5],
[3, 3, 0, 4, 5],
[4, 4, 4, 0, 5],
[5, 5, 5, 5, 0]])
'''


while matrix.shape != (2,2) :
    print(matrix)
    minElement = matrix[0][1]
    min_i = 0
    min_j = 1
    for i in range (np.size(matrix,0)):        
        for j in range (np.size(matrix, 1)):            
            if matrix[i][j] < minElement and i != j:               
                minElement = matrix[i][j]
                min_i = i
                min_j = j

                
    if(min_i >  min_j):
        min_ij = min_j
    else:
        minij = min_i
   
    new_Array = []
    for k in range(np.size(matrix,1)):
        if k == min_j and minij != min_j:
            new_Array.append(0)
            continue
        if k == min_j and minij == min_j:
            continue
        if k== min_i and minij == min_i:
            continue
        if k == min_i and minij != min_i:
            new_Array.append(0)
            continue
        new_Array.append((matrix[k][min_i] + matrix[k][min_j])/2 )
        
   
    new_node = letters[min_i] + letters[min_j]
    print("new node: ", new_node)
    
    if len(letters[min_i]) == 1 and len(letters[min_j]) == 1  :
        
        node1 = pydot.Node(letters[min_i],  texlbl= letters[min_i] ,shape ="circle", style="filled", fillcolor="white")
        node2 = pydot.Node(letters[min_j],  texlbl= letters[min_j] ,shape ="circle", style="filled", fillcolor="white")
        node3 = pydot.Node(new_node,  texlbl= new_node ,shape ="circle", style="filled", fillcolor="white")
        G.add_node(node3)
        G.add_node(node1)
        G.add_node(node2)        
        G.add_edge(pydot.Edge(new_node, letters[min_i]))
        G.add_edge(pydot.Edge(new_node, letters[min_j]))
        
    elif len(letters[min_i]) == 1 and len(letters[min_j]) != 1:

        namei = pydot.Node(letters[min_i],  texlbl= letters[min_i] ,shape ="circle", style="filled", fillcolor="white")        
        namenew = pydot.Node(new_node,  texlbl= new_node ,shape ="circle", style="filled", fillcolor="white")
        
        G.add_node(namenew)
        G.add_node(namei)
        
        G.add_edge(pydot.Edge(new_node,letters[min_i]))
        G.add_edge(pydot.Edge(new_node,letters[min_j]))
        
    elif len(letters[min_j]) == 1 and len(letters[min_i]) != 1:
        
        node1 = pydot.Node(letters[min_j],  texlbl= letters[min_j] ,shape ="circle", style="filled", fillcolor="white")        
        node3 = pydot.Node(new_node,  texlbl= new_node ,shape ="circle", style="filled", fillcolor="white")
        G.add_node(node1)
        G.add_node(node3)        
        G.add_edge(pydot.Edge(new_node,letters[min_i]))
        G.add_edge(pydot.Edge(new_node,letters[min_j]))

    elif len(letters[min_i]) != 1 and len(letters[min_j]) != 1:
        node3 = pydot.Node(new_node,  texlbl= new_node ,shape ="circle", style="filled", fillcolor="white")
        G.add_node(node3)
        G.add_edge(pydot.Edge(new_node,letters[min_i]))
        G.add_edge(pydot.Edge(new_node,letters[min_j]))

    
    if(min_i >  min_j):
        matrix = np.delete(matrix, min_j, axis = 0)
        matrix = np.delete(matrix, min_j , axis = 1)
        matrix [min_i-1] =  new_Array
        matrix [:,min_i -1] = new_Array
        letters[min_i] = new_node
        letters.remove(letters[min_j])
    else:
        
        matrix = np.delete(matrix, min_i,axis = 0)
        matrix = np.delete(matrix,  min_i , axis = 1)           
        matrix [min_j-1] =  new_Array
        matrix [:,min_j -1] = new_Array
        letters[min_j] = new_node
        letters.remove(letters[min_i])
        
    

print(matrix)     
new_node = letters[0] + letters[1]
node4 = pydot.Node(new_node,  texlbl= new_node ,shape ="circle", style="filled", fillcolor="yellow")
if (len(letters[1]) == 1) :
    node5 = pydot.Node(letters[1],  texlbl= letters[1] ,shape ="circle", style="filled", fillcolor="white")
else:
     node5 = pydot.Node(letters[0],  texlbl= letters[0] ,shape ="circle", style="filled", fillcolor="white")
    
G.add_node(node4)
G.add_node(node5)
G.add_edge(pydot.Edge(new_node,letters[1]))
G.add_edge(pydot.Edge(new_node,letters[0]))   

stop = time.time()
time_taken = stop-start
print("time taken: ", time_taken)
G.write_png('treetopology008.png')
 

""" 
for n, p in pos.iteritems():
    G.node[n]['pos'] = p

nx.draw(X, pos)
plt.show()


pos = hierarchy_pos(G,1)    
nx.draw(G, pos=pos, with_labels=True)
plt.savefig('tree.png')

  
nx.draw(G, with_labels = True)
plt.show()
   



pos = nx.nx_agraph.graphviz_layout(G)
pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
"""            
