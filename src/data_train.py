from yaml import safe_load
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os
import pickle
import joblib
params=safe_load(open("params.yaml"))["train"]
wcss=[]
data=pd.read_csv("data/preprocessed/age_blood_presure1.csv")
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=42)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()
   

# Plot the Elbow graph to determine the number of clusters
def train(preprocessed_data_path,model_path):
    data=pd.read_csv("data/preprocessed/age_blood_presure1.csv")
    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=42)
    data["clusters"]=kmeans.fit_predict(data)
    model=os.makedirs(os.path.dirname(model_path),exist_ok=True)
    filename=os.path.dirname(model_path)
    model_path1 = os.path.join(filename, "blood1.joblib")
    joblib.dump(kmeans,filename=model_path1)
if __name__=="__main__":
    train(params["data1"],params["model2"])    



params1=safe_load(open("params.yaml"))["train2"]
def train1(preprocessed_data_path,model_path):
    data=pd.read_csv("data/preprocessed/age_diabetess1.csv")
    kmeans1 = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=42)
    data["clusters"]=kmeans1.fit_predict(data)
    model=os.makedirs(os.path.dirname(model_path),exist_ok=True)
    filename=os.path.dirname(model_path)
    model_path1 = os.path.join(filename, "diabetes.joblib")
    joblib.dump(kmeans1,filename=model_path1)
if __name__=="__main__":
   if __name__=="__main__":
    train1(params1["data2"],params1["model3"])   









   

# Plot the Elbow graph to determine the number of clusters
