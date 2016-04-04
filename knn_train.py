from sklearn.neighbors import KNeighborsClassifier
import pickle
import sklearn.cross_validation as cv

def train_knn(nearest_neighbors, training_features, train_classes):
    # write your code here
    X = training_features
    y = train_classes
    neigh = KNeighborsClassifier(n_neighbors=nearest_neighbors)
    neigh.fit(X, y)
    return neigh

def cross_valid(xx, yy):
    clf = KNeighborsClassifier(n_neighbors=1000)
    scores = cv.cross_val_score(clf,xx,yy, cv=5)
    print(scores)

if __name__ == "__main__":
    train_dict = pickle.load(open("/Users/vikhyati/Desktop/training_data.pickle"))
    xx = train_dict['training_features']
    yy = train_dict['categories']
    cross_valid(xx, yy)
    '''
    model = train_knn(1000 , xx , yy)

    print model.score(xx ,yy )
    print model.metrics.f1_score(xx,yy)
    print model.predict([xx[100]]) , yy[100]
    '''
# call train_knn function here