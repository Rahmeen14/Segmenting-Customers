import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import sys

dataset = pd.read_csv(sys.argv[1])
X= dataset.iloc[:, [3,4]].values
lenR, lenC = X.shape
from sklearn.cluster import KMeans
wcss = []

for i in range(1,11):
    cluster = KMeans(n_clusters=i, init='k-means++',  random_state=0)
    cluster.fit(X)
    wcss.append(cluster.inertia_)

plt.plot(range(1, 11),wcss)   
plt.title('Elbow technique ' )
plt.xlabel('k ')
plt.ylabel('WCSS')
plt.legend()
#plt.show()

plt.savefig('./plotPics/Elbow.png')
    
plt.clf() 
data= {"name" : "Elbow Techinique for choosing optimal k for the KMeans Clustering Algorithm","pic" : './plotPics/Elbow.png'}

#Dumping to a json file
with open('output', 'w') as outfile:
	json.dump(data, outfile)
 
print(data)
sys.stdout.flush()    