
import random
import string
import math
import json


num_vertices = 6
graph= [[100]*num_vertices for i in range(num_vertices)]
print(graph)
for i in range(len(graph)):
    for j in range(len(graph)):
        print(i,j)
        if i == j:
            graph[i][j] = 0
            continue
        if graph[i][j] !=100:
            continue

        r = random.randint(1,math.floor(num_vertices*0.2))
        if r == 1:
            num = random.randint(1,10)
            graph[i][j] = num
            graph[j][i] = num
print(graph)
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] == 100:
            graph[i][j] = 0
            
            
print (graph)



with open('connected_graph.txt', 'w') as f:
    f.write(json.dumps(graph))

#Now read the file back into a Python list object
#with open('test.txt', 'r') as f:
#    a = json.loads(f.read())
