import matplotlib.pyplot as plt
import random
import math
#polynomial regression with gradient descent
data = [[i, (i+3)*((i-2)**2)*((i+1)**3)] for i in range(-3, 3)]
plt.scatter(*zip(*data))

class PolynomialRegressor:
    def __init__(self, deg, data):
        self.xs, self.ys = zip(*data)
        print(self.xs)
        print(self.ys)
        self.degree = deg
        self.coeffs = [1 for i in range(self.degree + 1)]#coeffs are weights
        self.exponents = [i for i in range(self.degree + 1)]
        self.exponents = [self.exponents[-i] for i in range(len(self.exponents))]
        print("Coeffs:>" + str(self.coeffs))
        print("Deg:>" + str(self.degree))
        print("Exps:>" + str(self.exponents))
        self.lr = .0001
   
    def findCost(self):#mean squared error
        sum_sq_err = 0
        for i in range(len(self.xs)):
            pred = self.calculate(self.xs[i])
            sum_sq_err += (pred - self.ys[i])**2
        return (1/len(self.xs))*sum_sq_err 

    #ax^2 + bx + c...
    def calculate(self, x):
        y = 0
        for i in range(len(self.coeffs)):
            y += self.coeffs[i]*(x**self.exponents[i])
        return y

    def getLine(self):
        lcoords = []
        for i in range(len(self.xs)):
            lcoords.append([self.xs[i], self.calculate(self.xs[i])])
        return lcoords
    #differentiate the polynomial and plug in x to find the slope at that point
    def findSlope(self, x):
        scoeffs = []
        sexps = []
        for i in range(len(self.coeffs)):
            #mult exp by coeff if coeff, else coeff = exp
            if self.coeffs[i] != 0:
                scoeffs.append(self.coeffs[i]*self.exponents[i])
            else:
                scoeffs.append(self.exponents[i])
            #decrement the exponent
            sexps.append(self.exponents[i] - 1)
        #get the slope at the given x
        y = 0
        for j in range(len(scoeffs)):
            if sexps[j] > 0:
                y += scoeffs[j]*(x**sexps[j])
            else:
                y += scoeffs[j] * x
        return y

    def updateCoeffs(self):
        for i in range(len(self.xs)):
            for j in range(len(self.coeffs)):
                self.coeffs[j] = self.coeffs[j] - ((self.lr*(self.calculate(self.xs[i]) - self.ys[i])*self.findSlope(self.xs[i]))/len(self.xs))



p = PolynomialRegressor(4, data)

lcs = p.getLine()

plt.scatter(*zip(*lcs))
plt.show(block=False)
i = 0
while True:
    print(i)
    lcs = p.getLine()
    p.updateCoeffs()
    plt.ylim(min(p.ys), max(p.ys))
    plt.plot(*zip(*lcs))
    plt.plot(*zip(*data))
    plt.show(block=False)
    plt.pause(.1)
    plt.cla()
    i +=1
print(p.coeffs)
