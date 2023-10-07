import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


np.random.seed(0)
X=np.random.rand(100,2)
y=np.random.choice([0,1],size=100)#target vector
#(binary classification)

#split the datasets
X_train,X_test,y_train,y_test = train_test_split(X,y ,test_size=0.2,random_state=42)


#create a k nearest neighbor classifier with k=3
k=3
knn_classifier=KNeighborsClassifier(n_neighbors=k)

#fit hte classifier to the training data
knn_classifier.fit(X_train,y_train)


#maek predictions 
y_pred=knn_classifier.predict(X_test)


#calculate the accuracy
accuracy =accuracy_score(y_test,y_pred)
print(f'accuracy :{accuracy* 100:.2f}%')