import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


x,y=datasets.make_classification(n_samples=500,n_features=3,n_informative=2,n_redundant=0,random_state=42)


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

svm_classifier=SVC(kernel="linear",C=1.0)

svm_classifier.fit(x_train,y_train)

y_pred=svm_classifier.predict(x_test)

accuracy=accuracy_score(y_test,y_pred)
print("accuracy",accuracy)
