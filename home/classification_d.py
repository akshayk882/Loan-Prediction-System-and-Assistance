import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#import csv


# Importing the dataset
class classification_d():
    




    names = ['Loan_ID','Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area','Loan_Status']

    df = pd.read_csv("media/datst.csv",names=names)


    from sklearn.preprocessing import LabelEncoder
    var_mod = ['Gender','Married','Dependents','Education','Self_Employed','Property_Area','Loan_Status']
    le = LabelEncoder()
    for i in var_mod:
        df[i] = le.fit_transform(df[i])

    array = df.values
    X = array[:,6:12]
    y = array[:,12]
    y = y.astype('int')


    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state = 0)


    # Feature Scaling
    from sklearn.preprocessing import StandardScaler
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)


    # Fitting Decision Tree Classification to the Training set
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    classifier.fit(X_train, y_train)

    # Predicting the Test set results

    y_pred = classifier.predict(X_test)

    #To test for user given values

    @classmethod
    def decision_tree_predict_loan(cls,temp):
        temp = cls.sc.transform(temp)
        tryyy = cls.classifier.predict(temp)
        return tryyy
    
    
    # Making the Confusion Matrix
    from sklearn.metrics import confusion_matrix
    cm = confusion_matrix(y_test, y_pred)

decision_tree_predict_loan = classification_d.decision_tree_predict_loan