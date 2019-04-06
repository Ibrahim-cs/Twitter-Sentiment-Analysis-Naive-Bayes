import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

class naiveClassifier():
    def __init__(self):
        self.naive = None
        self.count_vector = None
        self.initnaiveclassifier()
        

    def initnaiveclassifier(self):

        location = r'C:\Users\Ibrahim\my1\project1\smsspamcollection\sentimenttrainingdataset.csv'
        # Dataset available using filepath 'smsspamcollection/SMSSpamCollection'
        df = pd.read_csv(location, 
                        header=None, 
                        names=['label', 'sms_message'])


        # Data Preprocessing
        df['label'] = df.label.map({'ham':0, 'spam':1})


        # split into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(df['sms_message'], 
                                                            df['label'], 
                                                            random_state=1)
                        
        # Instantiate the CountVectorizer method
        self.count_vector = CountVectorizer()

        # Fit the training data and then return the matrix
        training_data = self.getCountVectorizedData(X_train)
        # Transform testing data and return the matrix. Note we are not fitting the testing data into the CountVectorizer()
        testing_data = self.getCountVectorizedTestData(X_test)

        # Naive Bayes implementation using scikit-learn
        self.naive_bayes = MultinomialNB()
        self.naive_bayes.fit(training_data, y_train)
        predictions = self.naive_bayes.predict(testing_data)
        print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
        print('Precision score: ', format(precision_score(y_test, predictions)))
        print('Recall score: ', format(recall_score(y_test, predictions)))
        print('F1 score: ', format(f1_score(y_test, predictions)))

    def getCountVectorizedData(self, X_train):
        return self.count_vector.fit_transform(X_train)
    
    def getCountVectorizedTestData(self, X_test):
        return self.count_vector.transform(X_test)
 
        
        
    def getPrediction(self, text):
        count_text = self.getCountVectorizedTestData(text)
        return self.naive_bayes.predict(count_text)


    """def printScores():
        print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
        print('Precision score: ', format(precision_score(y_test, predictions)))
        print('Recall score: ', format(recall_score(y_test, predictions)))
        print('F1 score: ', format(f1_score(y_test, predictions)))"""

"""if __name__== "__main__":
    a = naiveClassifier()
    prediction = a.getPrediction(['This is a tweet'])"""
