 #!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1
    eg:
    from sklearn import svm
    x = [[0,1],[1,1]]
    y = [0,1]
    clf = svm.SVC()
    clf.fit(x,y)
    SVC(C=1.0, cache_size = 200, class_weight = None, coef0 = 0.0, degree = 3,
    gamma = 0.0, kernel = 'rbf', max_iter = 1, probability = False,
    random_state = None, shrinking = True, tol = 0.001, verbose = False)
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn import svm
clf = svm.SVC(C=1.0, kernel='rbf', degree=3, gamma=0.0, coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, random_state=None)
t0 = time()
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t0 = time()
pred = clf.predict(features_test)
print "precition time:", round(time()-t0, 3), "s"

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc
#########################################################
