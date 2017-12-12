
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import sys

dataset = pd.read_csv(sys.argv[1])
X= dataset.iloc[:, [3,4]].values
lenR, lenC = X.shape
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, init='k-means++', n_init=10,  random_state=0)
y_kmeans = kmeans.fit_predict(X)

color = ['pink','cyan','blue', 'orange', 'red', 'green', 'black', 'yellow', 'violet', 'purple', 'brown']
for i in range(0,5):
	plt.scatter(X[y_kmeans == i , 0], X[y_kmeans == i, 1], s = 100, c=color[i-1])
	#plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')


#plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label = 'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.savefig('./plotPics/result.png')

plt.clf() 
data= {"pic" : './plotPics/result.png'}

#Dumping to a json file
with open('output2', 'w') as outfile:
	json.dump(data, outfile)
 
print(data)
sys.stdout.flush()    
print(pic)


##

