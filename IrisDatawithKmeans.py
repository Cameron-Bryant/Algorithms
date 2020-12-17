import matplotlib.pyplot as plt
import random
import math
import csv
#because of the random start of the centroids sometimes only 2 classes are seperated. 
#Rerun the program until all of the centroids go to their group
#0      1               2           3               4           5
#id, sepal length, sepal width, Petal length, petal width, species
#Iris-setosa, Iris-virginica, Iris-versicolor
data = list(csv.reader(open("C://Users//camer//Downloads//Iris.csv")))
#[y][x]
#correct classification plot
def showCorrect():#change first indices to see different plots
    for i in range(len(data)):
        for j in range(len(data[i][1])):
            if i > 0:
                if data[i][5] == 'Iris-setosa':#blue
                    plt.plot(float(data[i][2]), float(data[i][4]), 'bo')#
                elif data[i][5] == 'Iris-virginica':#red
                    plt.plot(float(data[i][2]), float(data[i][4]), 'ro')
                elif data[i][5] == 'Iris-versicolor':#green
                    plt.plot(float(data[i][2]), float(data[i][4]), 'go')
    plt.show()
showCorrect()
d = []
def getData():
    for i in range(len(data)):
        if i > 0:
            d.append([float(data[i][2]), float(data[i][4])])
print(d)

getData()
class K_Means_Clusterer:
    def setData(self, data, k):
        self.data = data
        self.labeled_points = []
        self.centroids = [[random.uniform(0, max(self.data[0])), random.uniform(0,max(self.data[1]))]*1 for i in range(k)]

    def label(self):
        self.labeled_points = []
        for i in range(len(self.data)):
            #self.labeled_points.append(self.classifyPoint(self.data[i]))
            mindist = 100000
            lab = 0
            for j in range(len(self.centroids)):
                dist = math.sqrt(((self.data[i][0] - self.centroids[j][0])**2) + ((self.data[i][1] - self.centroids[j][1])**2))
                if dist < mindist:
                    mindist = dist
                    lab = j

            self.labeled_points.append([self.data[i][0], self.data[i][1], lab])

    def getCenter(self, points):
        sumX = 0
        sumY = 0
        for i in range(len(points)):
            sumX += points[i][0]
            sumY += points[i][1]
        return [sumX/len(points), sumY/len(points)]

    def showPoints(self):
        for i in range(len(self.labeled_points)):
            if self.labeled_points[i][2] == 0:
                plt.plot(self.labeled_points[i][0], self.labeled_points[i][1], 'bo')
            elif self.labeled_points[i][2] == 1:
                plt.plot(self.labeled_points[i][0], self.labeled_points[i][1], 'ro')
            elif self.labeled_points[i][2] == 2:
                plt.plot(self.labeled_points[i][0], self.labeled_points[i][1], 'go')
        
        plt.plot(self.centroids[0][0], self.centroids[0][1], 'b+')
        plt.plot(self.centroids[1][0], self.centroids[1][1], 'r+')
        plt.plot(self.centroids[2][0], self.centroids[2][1], 'g+')
        
        plt.show(block=False)
        plt.pause(.5)
        plt.cla()

    def cluster(self):
        self.label()
        self.showPoints()

        g1 = []
        g2 = []
        g3 = []

        for i in range(len(self.labeled_points)):
            if self.labeled_points[i][2] == 0:
                g1.append(self.labeled_points[i])
            elif self.labeled_points[i][2] == 1:
                g2.append(self.labeled_points[i])
            elif self.labeled_points[i][2] == 2:
                g3.append(self.labeled_points[i])

        #self.centroids[0] = [sum(g1[0])/len(g1), sum(g1[1])/len(g1)]
        if len(g1) != 0:
            self.centroids[0] = self.getCenter(g1)
        if len(g2) != 0:
            self.centroids[1] = self.getCenter(g2)
        if len(g3) != 0:
            self.centroids[2] = self.getCenter(g3)

km = K_Means_Clusterer()
km.setData(d, 3)
print(km.data)
for i in range(15):
    km.cluster()
    print(i)
