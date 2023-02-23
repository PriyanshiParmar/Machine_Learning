# -*- coding: utf-8 -*-
"""ML_CE008_Lab8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Yj1FUkvFjJIArw6kJ6znRksNsIVanOpm

Stacking
"""

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import StackingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree
# models = [ ('rf', RandomForestClassifier(n_estimators=10, random_state=42)),('dt', DecisionTreeClassifier(random_state=0)),('bayes', GaussianNB())]
# stacking = StackingClassifier(estimators=models, final_estimator=LogisticRegression())

# lr = LogisticRegression()
# clf_stack = StackingClassifier(classifiers =[KNC, NB], meta_classifier = lr, use_probas = True, use_features_in_secondary = True)

# dataset = pd.read_csv('drive/MyDrive/Sem-6/ML/Contrete.csv')
dataset = load_breast_cancer()
# print(dataset)
features_names = dataset.feature_names
features = dataset.data
target_names = dataset.target_names
targets = dataset.target
data_df = pd.DataFrame(data = dataset.data,columns = dataset.feature_names)
# print("Features: ", features)
# print("Target Values: ", targets)
# print(data_df)
X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size = 0.33, random_state=42)
# stacking.fit(X_train, y_train).score(X_test, y_test)
estimators = [
    ('gnb', GaussianNB()),
    ('dt', tree.DecisionTreeClassifier(max_depth=1)),
    ('mnb', MultinomialNB())
]

model_stacked = StackingClassifier(estimators=estimators).fit(X_train, y_train)
y_pred = model_stacked.predict(X_test)
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
print("F1 score:",metrics.f1_score(y_test, y_pred))

"""Stacking from Scratch"""

from numpy import mean
from numpy import std
from sklearn import preprocessing
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from matplotlib import pyplot
from sklearn.datasets import load_breast_cancer
import pandas as pd

dataset = load_breast_cancer()

features_names = dataset.feature_names
features = dataset.data
target_names = dataset.target_names
targets = dataset.target
data_df = pd.DataFrame(data = dataset.data,columns = dataset.feature_names)

#Preprocessing
features = preprocessing.MinMaxScaler().fit_transform(features)

from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn import metrics

X_train, X_test, Y_train, Y_test = train_test_split(features, targets, train_size = 0.85, random_state= 8)
X = X_train
Y = Y_train

#DT
X_train_dt, X_test_dt, Y_train_dt, Y_test_dt = train_test_split(X, Y, train_size = 0.5, random_state = 8)
dt = tree.DecisionTreeClassifier()
dt = dt.fit(X_train_dt, Y_train_dt)
Y_pred_dt = dt.predict(X_test_dt)
print("Accuracy:",metrics.accuracy_score(Y_test_dt, Y_pred_dt))
print("Precision:",metrics.precision_score(Y_test_dt, Y_pred_dt))
print("Recall:",metrics.recall_score(Y_test_dt, Y_pred_dt))
print("F1 score:",metrics.f1_score(Y_test_dt, Y_pred_dt))

#Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB

X_train_gnb, X_test_gnb, Y_train_gnb, Y_test_gnb = train_test_split(X, Y, train_size = 0.8)
gnb = GaussianNB()

gnb.fit(X_train_gnb, Y_train_gnb)
Y_pred_gnb = gnb.predict(X_test_gnb)
print("Accuracy:",metrics.accuracy_score(Y_test_gnb, Y_pred_gnb))
print("Precision:",metrics.precision_score(Y_test_gnb, Y_pred_gnb))
print("Recall:",metrics.recall_score(Y_test_gnb, Y_pred_gnb))
print("F1 score:",metrics.f1_score(Y_test_gnb, Y_pred_gnb))

#Multinomial Naive Bayes
from sklearn.naive_bayes import MultinomialNB

X_train_mnb, X_test_mnb, Y_train_mnb, Y_test_mnb = train_test_split(X, Y, train_size = 0.8)
mnb = MultinomialNB()

mnb.fit(X_train_mnb, Y_train_mnb)
Y_pred_mnb = mnb.predict(X_test_mnb)
print("Accuracy:",metrics.accuracy_score(Y_test_mnb, Y_pred_mnb))
print("Precision:",metrics.precision_score(Y_test_mnb, Y_pred_mnb))
print("Recall:",metrics.recall_score(Y_test_mnb, Y_pred_mnb))
print("F1 score:",metrics.f1_score(Y_test_mnb, Y_pred_mnb))

#Combining all the above models
from sklearn.linear_model import LogisticRegression 

X_train_final = []
Y_train_final = []

Y_train_1 = dt.predict(X)
Y_train_2 = gnb.predict(X)
Y_train_3 = mnb.predict(X)

for i in range(len(Y_train_1)):
  X_train_final.append([Y_train_1[i], Y_train_2[i], Y_train_3[i]])
  Y_train_final.append(Y[i])

final_model = LogisticRegression().fit(X_train_final, Y_train_final)

from sklearn import metrics

X_test_final = []
Y_test_final = []

Y_test_1 = dt.predict(X_test)
Y_test_2 = gnb.predict(X_test)
Y_test_3 = mnb.predict(X_test)

for i in range(len(Y_test_1)):
  X_test_final.append([Y_test_1[i], Y_test_2[i], Y_test_3[i]])
  Y_test_final.append(Y_test[i])

Y_pred_final = final_model.predict(X_test_final)
print("Accuracy:",metrics.accuracy_score(Y_test_final, Y_pred_final))
print("Precision:",metrics.precision_score(Y_test_final,Y_pred_final))
print("Recall:",metrics.recall_score(Y_test_final,Y_pred_final))
print("F1 score:",metrics.f1_score(Y_test_final,Y_pred_final))

"""Bagging

"""

from sklearn.ensemble import BaggingClassifier

bagging_model = BaggingClassifier(max_features = 0.80).fit(X, Y)

pred_bagging = bagging_model.predict(X_test)
print("Accuracy:",metrics.accuracy_score(Y_test, pred_bagging))
print("Precision:",metrics.precision_score(Y_test, pred_bagging))
print("Recall:",metrics.recall_score(Y_test, pred_bagging))
print("F1 score:",metrics.f1_score(Y_test, pred_bagging))

"""RandomForest

"""

from sklearn.ensemble import RandomForestClassifier

rnd_forest = RandomForestClassifier(n_estimators=81).fit(X, Y)
Y_pred_rnd_frst = rnd_forest.predict(X_test)

print("Accuracy:",metrics.accuracy_score(Y_test, Y_pred_rnd_frst))
print("Precision:",metrics.precision_score(Y_test, Y_pred_rnd_frst))
print("Recall:",metrics.recall_score(Y_test, Y_pred_rnd_frst))
print("F1 score:",metrics.f1_score(Y_test, Y_pred_rnd_frst))

"""AdaBoost"""

from sklearn.ensemble import AdaBoostClassifier

adaboost = AdaBoostClassifier(n_estimators=100, learning_rate=1).fit(X, Y)
y_pred_adaboost = adaboost.predict(X_test)

print("Accuracy:",metrics.accuracy_score(Y_test, y_pred_adaboost))
print("Precision:",metrics.precision_score(Y_test, y_pred_adaboost))
print("Recall:",metrics.recall_score(Y_test, y_pred_adaboost))
print("F1 score:",metrics.f1_score(Y_test, y_pred_adaboost))

"""AdaBoost on Diabetes Dataset"""

from sklearn.ensemble import AdaBoostClassifier
import pandas as pd

data = pd.read_csv("drive/MyDrive/diabetes.csv")
features = data.iloc[:,:-1]
label = data.iloc[:, -1:]
# label
X_train, X_test, Y_train, Y_test = train_test_split(features, label, train_size=0.8, random_state=9)
adaboost1 = AdaBoostClassifier(n_estimators=100, learning_rate=1).fit(X_train, Y_train)
y_pred_adaboost = adaboost1.predict(X_test)

print("Accuracy:",metrics.accuracy_score(Y_test, y_pred_adaboost))
print("Precision:",metrics.precision_score(Y_test, y_pred_adaboost))
print("Recall:",metrics.recall_score(Y_test, y_pred_adaboost))
print("F1 score:",metrics.f1_score(Y_test, y_pred_adaboost))

from sklearn.ensemble import AdaBoostRegressor
import pandas as pd
from sklearn.metrics import mean_squared_error

data = pd.read_csv("drive/MyDrive/diabetes.csv")
features = data.iloc[:,:-1]
label = data.iloc[:, -1:]
# label
X_train, X_test, Y_train, Y_test = train_test_split(features, label, train_size=0.8, random_state=9)
adaboostr = AdaBoostRegressor(n_estimators=100, learning_rate=1).fit(X_train, Y_train)
y_pred_adaboost = adaboostr.predict(X_test)

print("Accuracy:",adaboostr.score(X_test, Y_test))
print("MSE ", mean_squared_error(Y_test, y_pred_adaboost))

"""AdaBoost Regressor on Contrete Dataset"""

from sklearn.ensemble import AdaBoostRegressor
import pandas as pd

data = pd.read_csv("drive/MyDrive/Contrete.csv")
features = data.iloc[:,:-1]
label = data.iloc[:, -1:]
# label
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(features, label, train_size=0.8, random_state=9)
adaboost2 = AdaBoostRegressor(n_estimators=100, learning_rate=1).fit(X_train1, Y_train1)
y_pred_adaboost = adaboost2.predict(X_test1)

print("Accuracy:",adaboost2.score(X_test1, Y_test1))