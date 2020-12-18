import matplotlib.pyplot as plt
import random
import math
#shows the point unlabeled, then x out and it will show it labeled
#k-means/k nearest neighbor regression
#find dist from the unknown point to all other points
#order the labeled data from closest to furthest
#find the best number k of neighbors with RMSE
#calculate inverse difference
#tweak any of the values to experiment with the effects
dim = 10 #dimensions of the graph
num_of_points = 15 #number of points on the graph

#gen and graph data
data = [[random.randint(0, dim), random.randint(0, dim)] for i in range(num_of_points)]
plt.scatter(*zip(*data))
pos = [int(dim/2), int(dim/2)]
plt.scatter(pos[0], pos[1], c = 'green')#label unlabeled point
plt.annotate("Unlabeled Point", (pos[0], pos[1]))
plt.show()

def label(data): #takes [[x, y]...] and returns [[x, y, label]...]. 
    for i in range(len(data)):
        #TODO:> use distance from a point to det class bounds
        if data[i][0] < int(dim/2):#tweak here to change label boundary
            data[i].append(1)
        else:
            data[i].append(0)
    return data

data = label(data)
print(data)

def sortLast(x):#sort by last element/distance
    return x[-1]

def cluster(unlabeled_pos, data):
    k = 5 #the neighbors that the clusterer looks at to decide class
    for i in range(len(data)):#[x, y, label]:> [x, y, label, dist]
        data[i].append(math.sqrt(((data[i][0] - pos[0])**2) +((data[i][1] - pos[1])**2)))
    data = sorted(data, key = sortLast) #sort all the data based on distance
    print(data)

    count1 = 0
    count0 = 0
    for j in range(k): #tally up the classes of the knn's 
        if data[k][2] == 1: 
            count1 +=1
        else:
            count0 += 1
    if count0 != count1:#label the unlabeled data and plot it
        if (count0 > count1):
            unlabeled_pos.append(0)
            plt.scatter(unlabeled_pos[0], unlabeled_pos[1], c = "red")
            plt.annotate("Labeled Point", (pos[0], pos[1]))
        else:
            unlabeled_pos.append(1)
            plt.scatter(unlabeled_pos[0], unlabeled_pos[1], c = "blue")
            plt.annotate("Labeled Point", (pos[0], pos[1]))
cluster(pos, data)
for i in range(len(data)):
    if data[i][2] == 1:
        plt.scatter(data[i][0], data[i][1], c = "red")
    else:
        plt.scatter(data[i][0], data[i][1], c = "blue")
plt.show()
    
