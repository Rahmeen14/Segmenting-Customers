
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import sys

dataset = pd.read_csv(sys.argv[1])
X= dataset.iloc[:, [3,4]].values

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=sys.argv[2], init='k-means++', n_init=10,  random_state=0)
y_kmeans = cluster.fit_predict(X)
color = ['pink','cyan','blue', 'orange', 'red', 'green', 'black', 'yellow', 'violet', 'purple', 'brown']
for i in range(0,sys.argv[2]):
	plt.scatter(X[y_kmeans == i , 0], X[y_kmeans == i, 1], s = 100, c=color[i-1])


#plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.savefig('./plotPics/result.png')
pic = './plotPics/result.png'
print(pic)