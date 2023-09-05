import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

lista = []

with open("datosReduccion (1).txt", "r") as f:
    for line in f:
        line = line.split()
        lista.append([float(line[0]),float(line[1])]) 

tamLista = int(len(lista) * 0.2)

lista = lista[:tamLista]

np.array(lista)

num_cluster = 3

kmeans = KMeans(n_init = num_cluster)

kmeans.fit(lista)

clusters = kmeans.cluster_centers_list

print(clusters)
