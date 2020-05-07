from numpy import *

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score
from sklearn.model_selection import cross_val_score, train_test_split, cross_validate

from sklearn.datasets import make_blobs

# load features and labels into numpy nd.arrays
dataset_features = loadtxt('features.txt', delimiter=',')
dataset_labels = loadtxt('labels.txt', delimiter=',')
feature_size = len(dataset_features[0])

# construct a random forrest classifier using features and labels
clf = RandomForestClassifier(n_estimators=feature_size)
clf = clf.fit(dataset_features, dataset_labels)

# score the accuracy and recall of the model using 10-fold cross validation
scoring = ['accuracy', 'recall_macro']
X_train, X_test, y_train, y_test = train_test_split(
    dataset_features, dataset_labels, test_size=0.1)
scores = cross_validate(clf, X_train, y_train, cv=10, scoring=scoring)
acc = scores['test_accuracy'].mean()*100
rec = scores['test_recall_macro'].mean()*100

# display the results of the model
print("[!] Model Results")
print("\t[+] Accuracy  = %2.5f" % (acc))
print("\t[+] Recall    = %2.5f" % (rec))

