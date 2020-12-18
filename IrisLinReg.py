import matplotlib.pyplot as plt
import csv
import random

#setosa is linearly seperable from versicolor and virginica
#0      1               2           3               4           5
#id, sepal length, sepal width, Petal length, petal width, species
data = list(csv.reader(open("C://Users//camer//Downloads//Iris.csv")))
d = []
def getData():
    for i in range(len(data)):
        if i > 0:#change indices below to put different characteristics against each other
            d.append([float(data[i][2]), float(data[i][4])])
getData()
#using sepal width and petal width for (x,y)
class LinearRegressor:
    def __init__(self, x, y):
        self.xs = x
        self.ys = y
        self.weights = [.1 for i in range(len(self.xs))]
        self.learning_rate = .001

    def getLineCoords(self):
        lcs = []
        for i in range(len(self.weights)):
            lcs.append([self.xs[i], self.weights[i]*self.xs[i]])
        return lcs

    def regress(self):
        err = 0
        for i in range(len(self.weights)):
            err += ((self.weights[i]*self.xs[i]) - self.ys[i])**2
        err = 1/2 * err
        sum_of_diffs_times = 0
        for j in range(len(self.weights)):
            sum_of_diffs_times += (self.ys[j] - (self.weights[j] * self.xs[j])) * self.xs[j]

        for k in range(len(self.weights)):
            self.weights[k] += (self.learning_rate * sum_of_diffs_times)
        plt.scatter(self.xs, self.ys)
        plt.plot(*zip(*self.getLineCoords()))
        plt.show(block=False)
        plt.pause(.2)
        plt.cla()
lr = LinearRegressor(*zip(*d))
epochs = 100
for i in range(epochs):
    lr.regress()
