
from sklearn.neighbors import KNeighborsClassifier
import pickle

def train_knn(nearest_neighbors, training_features, train_classes):
    # write your code here
    X = training_features
    y = train_classes
    neigh = KNeighborsClassifier(n_neighbors=nearest_neighbors)
    neigh.fit(X, y)
    return neigh

train_dict = pickle.load(open("/Users/oshpd/vikhyati/Desktop/training_data.pickle"))
xx = train_dict['training_features']
yy = train_dict['categories']
model = train_knn(1000 , xx , yy)

print model.score(xx ,yy )
print model.predict([xx[100]]) , yy[100]
# call train_knn function here