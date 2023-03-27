# -*- coding: utf-8 -*-
"""ML_CE008_Lab9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Bt72coFK299W3gnthgjn_vzA8tn5fNm5
"""

# Imports
from sklearn.datasets import make_blobs
X, _ = make_blobs(n_samples=100, centers=3, n_features=2, cluster_std=0.2, random_state=0)

# Commented out IPython magic to ensure Python compatibility.
# Scatter plot of the data points
import matplotlib.pyplot as plt
# %matplotlib inline

# Using scikit-learn to perform K-Means clustering
from sklearn.cluster import KMeans
# Specify the number of clusters (3) and fit the data X

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

import numpy as np

labels = kmeans.predict(X)
centroids  = kmeans.cluster_centers_  #means of shape
centroid_labels = [centroids[i] for i in labels]
# centroid_labels = [*set(centroid_labels)]
np.unique(centroid_labels, axis= 0)

# get centroids
centroids = kmeans.cluster_centers_
cen_x = [i[0] for i in centroids] 
cen_y = [i[1] for i in centroids]
## add to df
df = X
df['cen_x'] = df.cluster.map({0:cen_x[0], 1:cen_x[1], 2:cen_x[2]})
df['cen_y'] = df.cluster.map({0:cen_y[0], 1:cen_y[1], 2:cen_y[2]})
# define and map colors
colors = ['#DF2020', '#81DF20', '#2095DF']
df['c'] = df.cluster.map({0:colors[0], 1:colors[1], 2:colors[2]})

import matplotlib.pyplot as plt
plt.scatter(df.Attack, df.Defense, c=df.c, alpha = 0.6, s=10)

"""Exercise

4. Use the k-means algorithm in python to cluster the following 8 examples into 3 clusters:
A1=(2,10), A2=(2,5), A3=(8,4), A4=(5,8), A5=(7,5), A6=(6,4), A7=(1,2), A8=(4,9).

(a) Suppose that the centers of each cluster are A1, A4 and A7.

  i. The new clusters (i.e. the examples belonging to each cluster)(mention the appropriate attribute used to identify the clusters in sklearn)

  ii. The centers of the new clusters (mention the appropriate attribute used to identify the cluster centers in sklearn)
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[2,10],[2,5],[8,4],[5,8],[7,5],[6,4],[1,2],[4,9]])
# plt.scatter(X[:,0], X[:,1])
centroid = np.array([[2,10],[5,8],[1,2]])

# 1st iteration
kmeans = KMeans(n_clusters=3, init=centroid, max_iter=1).fit(X)
print("cluster center for 1st iteration:\n", kmeans.cluster_centers_)

c1 = kmeans.cluster_centers_
plt.scatter(X[:,0], X[:,1])
plt.scatter(c1[:,0], c1[:,1])

#2nd iteration
kmeans = KMeans(n_clusters=3, init=c1, max_iter=1).fit(X)
print("\ncluster center 2nd iteration:\n", kmeans.cluster_centers_)

c2 = kmeans.cluster_centers_
plt.scatter(X[:,0], X[:,1])
plt.scatter(c2[:,0], c2[:,1])

#3rd iteration
kmeans = KMeans(n_clusters=3, init=c2, max_iter=1).fit(X)
print("\ncluster center 3rd iteration:\n", kmeans.cluster_centers_)
c3 = kmeans.cluster_centers_
plt.scatter(X[:,0], X[:,1])
plt.scatter(c3[:,0], c3[:,1])