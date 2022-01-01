import time
import random
import math
import matplotlib.pyplot as plt
#linear regression ml model using matplotlib
#sloppy code first time doing linear regression
dlen = 20

xdata = [random.randint(0,10) for i in range(dlen)]
ydata = [random.randint(0,10) for i in range(dlen)]


class LinearRegressor:
    def __init__(self, inpx, inpy):
        self.slope = 0
        self.error = None
        self.yintercept = 0
        self.ys = []
        self.lr = .01
        self.input_xs = inpx
        self.input_ys = inpy
        self.bestSlope = 0
        self.bestyintercept = 0


    def findBestFit(self):
        #slope = ((meanX * meanY) - meanXY)/((meanX)**2 - meanXsquared)
        xSum = 0
        ySum = 0
        xySum = 0
        xsquaredSum = 0
        for i in range(len(self.input_xs)):
            xSum += self.input_xs[i]
            ySum += self.input_ys[i]
            xySum += self.input_xs[i] * self.input_ys[i]
            xsquaredSum += self.input_xs[i]**2
        xmean = xSum/len(self.input_xs)
        ymean = ySum/len(self.input_xs)
        xymean = xySum/len(self.input_xs)
        xsquaredMean = xsquaredSum/len(self.input_xs) 
        self.bestSlope = ((xmean * ymean) - xymean)/(xmean**2 - xsquaredMean)
        #y-int = yMean - slope * meanX
        self.bestyintercept = ymean - (self.bestSlope * xmean)

    def costFunction(self):#mse
        exp_outputs = []
        outputs = []
        for l in range(len(self.input_xs)):
            exp_outputs.append((self.bestSlope*self.input_xs[l]) + self.bestyintercept)
        for i in range(len(outputs)):
            squaredSum += (outputs[i] - exp_outputs[i])
        mse = squaredSum * (1/len(outputs))
        return mse

    def derivativeSlope(self):
        ySum = 0
        dSum = 0
        for i in range(len(self.input_xs)):
            dSum += self.input_xs[i] * ((self.slope * self.input_xs[i] + self.yintercept) - ((self.bestSlope * self.input_xs[i]) + self.bestyintercept))
        ds = dSum * (-2/len(self.input_xs))
        return ds

    def derivativeYint(self):
        ySum = 0
        DYSum = 0

        for i in range(len(self.input_ys)):
            DYSum += (self.slope * self.input_xs[i] + self.yintercept) - ((self.bestSlope * self.input_xs[i]) + self.bestyintercept)
        dy = DYSum * (-2/len(self.input_ys))
        return dy

    def train(self):
        #slope = slope - (lr * derivativeSlope)
        #y int = yint - (lr * derivativeYint)
        ds = self.derivativeSlope()
        dy = self.derivativeYint()

        self.slope += (self.lr * ds)
        self.yintercept += (self.lr * dy)

    def getLineCoords(self):
        lcs = []
        for i in range(11):
            lcs.append([i, (self.slope*i) + self.yintercept])
        return lcs

    def getBestFitLine(self):
        blcs = []
        for i in range(11):
            blcs.append([i, (self.bestSlope*i) + self.bestyintercept])
        return blcs


lr = LinearRegressor(xdata, ydata)
lr.findBestFit()
plt.xlabel("X")
plt.ylabel("Y")
bx, by = zip(*lr.getBestFitLine())
i = 0
while True:
    lr.findBestFit()
    lr.train()
    lx, ly = zip(*lr.getLineCoords())
    
#plt.scatter(*zip(*linecoords))
    plt.scatter(xdata, ydata)
    plt.plot(lx, ly)
    plt.plot(bx, by)
    plt.show(block = False)
    if lr.slope == lr.bestSlope and lr.yintercept == lr.bestyintercept:
        break
    plt.pause(.001)
    plt.cla()
    i += 1
    if i % 50 == 0:
        print(lr.slope)
        print(lr.bestSlope)
        print(lr.yintercept)
        print(lr.bestyintercept)
