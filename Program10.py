# Import train_test_split function
from sklearn.neighbors import KNeighborsClassifier        #Import knearest neighbors Classifier model
from sklearn.model_selection import train_test_split      #Import train_test_split function
from sklearn.metrics import confusion_matrix              # confusion matrix to evaluate the accuracy of a classification.
from sklearn import metrics                               #Import scikit-learn metrics module for accuracy calculation
import matplotlib.pyplot as plt                           #matplotlib.pyplot (for plotting)
from sklearn.metrics import plot_confusion_matrix
from sklearn.metrics import classification_report
X = [[1], [2], [3], [6]]                                  # Assigning features and label variables
y = [6, 7, 10, 11]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
knn = KNeighborsClassifier(n_neighbors=2)                 #Create KNN Classifier
knn.fit(X_train, y_train)                                 #Train the model using the training sets
y_pred = knn.predict(X_test)                              #Predict the response for test dataset

knn.score(X_test, y_test)
cm = confusion_matrix(y_test,y_pred)


color = 'white'
matrix = plot_confusion_matrix(knn, X_test, y_test, cmap=plt.cm.Blues)
matrix.ax_.set_title('Confusion Matrix', color=color)
plt.xlabel('Predicted Label', color=color)
plt.ylabel('True Label', color=color)
plt.gcf().axes[0].tick_params(colors=color)
plt.gcf().axes[1].tick_params(colors=color)
plt.show()

print(classification_report(y_test, y_pred))