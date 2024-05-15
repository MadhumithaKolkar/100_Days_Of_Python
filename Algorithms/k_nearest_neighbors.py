import numpy as np

def euclidean_distance(p1,p2):
    #Returns the root of the summed square differnce between two points
    return np.sqrt(np.sum(p1-p2)**2)

def knn_predict(X_train,y_train,X_test,k):
    # k= Number of the nearest neighboring data points to consider

    y_pred = np.zeros(X_test.shape[0])
    for index,test_point in enumerate(X_test):

        distances = [euclidean_distance(test_point,point) for point in X_train]

        sorted_data = sorted(zip(distances,y_train))

        k_nearest_neighbors = [labels for distance,labels in sorted_data[:k]]

        predicted_label = np.bincount(k_nearest_neighbors).argmax()

        y_pred[index] = predicted_label

    return y_pred

X_train = np.array([[1,2],[3,4],[5,6],[1,0],[3,1]])
y_train = np.array([0,0,1,1,0])
X_test = np.array([[2,3]])
k=3
y_pred = knn_predict(X_train,y_train,X_test,k)
print(f"The class label for {X_test} is {y_pred}")