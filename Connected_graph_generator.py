
import random
import string
import math
import json

text = "Hello \n"

#savefile = open('T.txt','w')
#savefile.write("id\titem\tAddress\tDays till delivery \n")
#for i in range (100):
#    example_delivery = DeliveryOrder(i,"item" + str(random.randint(1,99)),"2601", random.randint(1,365))
#    savefile.write(example_delivery.Printclass())
#savefile.close()


#testfile = open('Hash_test.txt','w')
#testfile.write("Item\tLocation \n")
#for i in range (250):
##    s.insert("item" + str(i+1), 120 + i)
#    testfile.write("item" + str(i+1) + "\t" + random.choice(string.ascii_uppercase)
#    + str(random.randint(1,99)) + random.choice(string.ascii_uppercase) + "\n" )
#testfile.close()


#crimefile = open(fileName, 'r')
#yourResult = [line.split(',') for line in crimefile.readlines()]

num_vertices = 10
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
#testfile = open('D_test.txt','w')
#testfile.write(graph)


with open('test-f3-5.txt', 'w') as f:
    f.write(json.dumps(graph))

#Now read the file back into a Python list object
#with open('test.txt', 'r') as f:
#    a = json.loads(f.read())
