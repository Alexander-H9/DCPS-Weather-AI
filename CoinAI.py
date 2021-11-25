import numpy as np
from ExtractDataPoints import *

def getKNearestNeighbors(x,X,k=1):          # realizes nearest neighbor search of x in database X
    """
    compute the k nearest neighbors for a query vector x given a data matrix X
    :param x: the query vector x
    :param X: the N x D data matrix (in each row there is data vector) as a numpy array
    :param k: number of nearest-neighbors to be returned
    :return: return list of k line indixes referring to the k nearest neighbors of x in X
    """
    d=[np.linalg.norm(X[i]-x) for i in range(len(X))]                   
    d = np.argsort(d)
    print("sort d after index: ", d)
    return d[:k]           

# ***** MAIN PROGRAM ********

# Generate dummy data 
X = np.array([[2, 2, 2, 2.3], [1, 1, 1, 2.2], [0.5, 0.5, 0.5, 2.2], [0.2, 0.2, 0.2, 1.9], [0.1, 0.1, 0.1, 1.7] \
            ,[0.05, 0.05, 0.05, 1.4], [0.02, 0.02, 0.02, 1.3], [0.01, 0.01, 0.01, 1.1]]);           # data matrix X: list of data vectors (=database) of dimension D=4

# x = np.array([1.5, 0.6, 0.7, 1.3]);
d = Data()
messerte = [2,4,56,7,6,5,3,2,3,45,6,78,9,9,8,7,6,5,4,3,345,456,78,5,4,3,2,3,4,5,1]
d.extract(messerte)
x = np.array([d.minL, d.minR, d.maxM, d.length])
print("Data matrix X=\n",X)
print("Test vector x=",x)

# Print all Euklidean distances to test vector x
print("Euklidean distances to x: ", [np.linalg.norm(X[i]-x) for i in range(len(X))])                # compute list of Euklidean distances   

# Search for k nearest neighbor
k=2

idx_knn = getKNearestNeighbors(x,X,k)                                                               # get indexes of k nearest neighbors
print("idx_knn=",idx_knn)

# output results
print("The k Nearest Neighbors of x are the following vectors:")
for i in range(k):
    idx=idx_knn[i]
    print("The", i+1, "th nearest neighbor is: X[",idx,"]=",X[idx]," with distance ", np.linalg.norm(X[idx]-x))