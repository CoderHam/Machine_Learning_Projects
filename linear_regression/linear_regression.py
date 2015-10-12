import matplotlib.pyplot as plt
import numpy
from time import time
import random

ages = []
ages_test=[]

for i in range(0,60):
    ages.append(random.randint(20,65))

net_worths_train = [ii * 6.25 + numpy.random.normal(scale=40.) for ii in ages]

ages = numpy.reshape(numpy.array(ages), (len(ages),1))
net_worths_train = numpy.reshape(numpy.array(net_worths_train), (len(net_worths_train),1))

ages_train = ages

for i in range(0,20):
    ages_test.append(random.randint(20,65))

ages_test = numpy.reshape(numpy.array(ages_test), (len(ages_test),1))
net_worths_test = [ii * 6.25 + numpy.random.normal(scale=40.) for ii in ages_test]
net_worths_test = numpy.reshape(numpy.array(net_worths_test), (len(net_worths_test),1))


plt.scatter(ages_train, net_worths_train, color = "b", label="train")
plt.scatter(ages_test, net_worths_test, color = "r", label="test")
plt.legend()
plt.xlabel("Age")
plt.ylabel("Net Worth")

from sklearn.linear_model import LinearRegression

reg = LinearRegression ()

t0 = time()
reg.fit(ages_train, net_worths_train)
print "training time:", round(time()-t0, 3), "s\n"

t0 = time()
print "prediction value: ", reg.predict(ages_test)
print "precition time:", round(time()-t0, 3), "s\n"
print "slope: ", reg.coef_
print "\nintercept: ", reg.intercept_

print "\nR-square score for training data: ", reg.score(ages_train, net_worths_train)
print "\nR-square score for test data: ", reg.score(ages_test, net_worths_test)

#plt.plot(ages_train, net_worths_train, color = "b", linewidth=3)
plt.show()
