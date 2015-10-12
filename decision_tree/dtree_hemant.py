#!/usr/bin/python

"""
    this is the code to accompany the Lesson 3 (decision tree) mini-project

    use an DT to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1
    from sklearn import tree
    x = [[0,1],[1,1]]
    y = [0,1]
clf = tree.DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0, max_features=None, random_state=None, max_leaf_nodes=None, class_weight=None)
    clf.fit(x,y)
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier(criterion='gini', splitter='best', max_depth=None, min_samples_split=2, min_samples_leaf=1, max_features=None, random_state=None, max_leaf_nodes=None)

t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "precition time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
print "accuracy: ", accuracy_score(pred, labels_test)
