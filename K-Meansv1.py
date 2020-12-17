import matplotlib.pyplot as plt
import random
import math

#k means clustering version 1
#this vers only 3 clusters/centroids and sloppy code
#centroids and data points
#assign each data point to the closest centroid
#move the centroid towards the mean of the data assigned to it

d = [[random.uniform(0,10), random.uniform(0,10)]*1 for i in range(40)]

def dist(p0, p1):
    return math.sqrt(((p1[0] - p0[0])**2)+((p1[1] - p0[1])**2))

class K_Means_Clusterer:

    def setData(self, data, k):
        self.data = data
        self.labeled_points = []
        self.centroids = [[random.uniform(0, 10), random.uniform(0, 10)]*1 for i in range(k)]

    
    def classifyPoint(self, point):
        mindist = 100000
        lab = 0
        for i in range(len(self.centroids)):
            dist = math.sqrt(((point[0] - self.centroids[i][0])**2) + ((point[1] - self.centroids[i][1])**2))
            if dist < mindist:
                mindist = dist
                lab = i
        point.append(lab)
        return point

    def label(self):
        self.labeled_points = []
        for i in range(len(self.data)):
            self.labeled_points.append(self.classifyPoint(self.data[i]))

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
        if len(g1) > 0:
            self.centroids[0] = self.getCenter(g1)
        if len(g2) > 0:
            self.centroids[1] = self.getCenter(g2)
        if len(g3) > 0:
            self.centroids[2] = self.getCenter(g3)
 
        

km = K_Means_Clusterer()

km.setData(d, 3)
epochs = 15
for i in range(epochs):
    km.cluster()

