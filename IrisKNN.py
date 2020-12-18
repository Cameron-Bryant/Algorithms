import matplotlib.pyplot as plt
import random
import csv
import math
dat = list(csv.reader(open("C://Users//camer//Downloads//Iris.csv")))
d = []

def getData(dataset):
    dat_arr = []
    for i in range(len(dataset)):
        if i > 0:
            dat_arr.append([float(dataset[i][2]), float(dataset[i][4]), dataset[i][5]])
    return dat_arr
d = getData(dat)
dim = 5#dimensions of the graph

#gen and graph data
def plotData(mixed_data):
    for i in range(len(mixed_data)):
        if mixed_data[i][2] == "Iris-setosa":
            plt.scatter(mixed_data[i][0], mixed_data[i][1], c = "red")
        elif mixed_data[i][2] == "Iris-versicolor":
            plt.scatter(mixed_data[i][0], mixed_data[i][1], c = "blue")
        elif mixed_data[i][2] == "Iris-virginica":
            plt.scatter(mixed_data[i][0], mixed_data[i][1], c = "green")

pos = [random.uniform(1, 5), random.uniform(0, 3)] #the point that you need to classify
plt.scatter(pos[0], pos[1], c = 'green')#label unlabeled point
plotData(d)
plt.annotate("Unlabeled Point", (pos[0], pos[1]))
plt.ylim(0, 3)
plt.xlim(1, 5)
plt.show()

def sortLast(x):#sort by last element/distance
    return x[-1]

def cluster(unlabeled_pos, data):
    k = 5 #the neighbors that the clusterer looks at to decide class
    for i in range(len(data)):#[x, y, label]:> [x, y, label, dist]
        data[i].append(math.sqrt(((data[i][0] - pos[0])**2) +((data[i][1] - pos[1])**2)))
    data = sorted(data, key = sortLast) #sort all the data based on distance
    print(data)

    count0 = 0
    count1 = 0
    count2 = 0
    for j in range(k): #tally up the classes of the knn's 
        if data[k][2] == "Iris-setosa": 
            count0 +=1
        elif data[k][2] == "Iris-versicolor":
            count1 += 1
        elif data[k][2] == "Iris-virginica":
            count2 += 1

    if count0 != count1 or count1 != count2:#label the unlabeled data and plot it
        if (count0 > count1 and count0 > count2):
            unlabeled_pos.append("Iris-setosa")
            plt.scatter(unlabeled_pos[0], unlabeled_pos[1], c = "red")
            plt.annotate("Labeled Point", (pos[0], pos[1]))
        elif (count1 > count0 and count1 > count2):
            unlabeled_pos.append("Iris-versicolor")
            plt.scatter(unlabeled_pos[0], unlabeled_pos[1], c = "blue")
            plt.annotate("Labeled Point", (pos[0], pos[1]))
        elif (count2 > count0 and count2 > count1):
            unlabeled_pos.append("Iris-virginica")
            plt.scatter(unlabeled_pos[0], unlabeled_pos[1], c = "green")
            plt.annotate("Labeled Point", (pos[0], pos[1]))
    for i in range(len(d)):
        if data[i][2] == "Iris-setosa":
            plt.scatter(data[i][0], data[i][1], c = "red")
        elif data[i][2] == "Iris-versicolor":
            plt.scatter(data[i][0], data[i][1], c = "blue")
        elif data[i][2] == "Iris-virginica":
            plt.scatter(data[i][0], data[i][1], c = "green")
    plt.ylim(0, 3)
    plt.xlim(1, 5)
    plt.show()
cluster(pos, d)
