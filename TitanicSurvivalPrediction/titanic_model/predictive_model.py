import time
import os.path
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

my_path = os.path.abspath(os.path.dirname(__file__))

class PredictiveModel:
    def __init__(self):
        self._training_path = os.path.join(my_path, r"train.csv")
        self._testing_path = os.path.join(my_path, r"test.csv")
        self._model = self.get_predictive_model()

    def get_predictive_model(self):
        training_data = pd.read_csv(self._training_path)
        testing_data = pd.read_csv(self._testing_path)
    
        training_data, training_label = self.process_training_data(training_data)
        testing_data = self.process_testing_data(testing_data)

        random_forest_clf = RandomForestClassifier(random_state=1, max_depth=5)
        random_forest_clf.fit(training_data, training_label)

        return random_forest_clf

    def make_prediction(self, person_data):
        return self._model.predict(person_data)

    def process_training_data(self, training_data):
        training_data['Embarked'] = training_data.Embarked.fillna('S')
        training_data['Age'] = training_data.Age.fillna(training_data.Age.mean())
        training_data['Fare'] = training_data.Fare.fillna(training_data.Fare.mean())

        training_data['Fare_Bin']=pd.qcut(training_data['Fare'],6)

        training_data['Sex'].replace(['male','female'],[0,1],inplace=True)

        training_data['Embarked'].replace(['S','C','Q'],[0,1,2],inplace=True)

        training_data['Age_cat']=0
        training_data.loc[training_data['Age']<=12,'Age_cat']=0
        training_data.loc[(training_data['Age']>12)&(training_data['Age']<=17),'Age_cat']=1
        training_data.loc[(training_data['Age']>17)&(training_data['Age']<=64),'Age_cat']=2
        training_data.loc[training_data['Age']>64,'Age_cat']=3

        training_data['Fare_cat']=0
        training_data.loc[training_data['Fare']<=7.775,'Fare_cat']=0
        training_data.loc[(training_data['Fare']>7.775)&(training_data['Fare']<=8.662),'Fare_cat']=1
        training_data.loc[(training_data['Fare']>8.662)&(training_data['Fare']<=14.454),'Fare_cat']=2
        training_data.loc[(training_data['Fare']>14.454)&(training_data['Fare']<=26.0),'Fare_cat']=3
        training_data.loc[(training_data['Fare']>26.0)&(training_data['Fare']<=52.369),'Fare_cat']=4
        training_data.loc[training_data['Fare']>52.369,'Fare_cat']=5

        training_data['FamilySize'] = training_data['Parch'] + training_data['SibSp']

        training_data.drop(['Name','Age','Fare','Ticket','Cabin','Fare_Bin','SibSp','Parch','PassengerId'],axis=1,inplace=True)

        training_data_label = training_data[['Survived']]
        training_data_label = np.ravel(training_data_label)
        training_data = training_data.drop('Survived', axis=1)

        return training_data, training_data_label

    def process_testing_data(self, testing_data):
        testing_data.Ticket.fillna(testing_data.Ticket.mean(), inplace=True)
        testing_data.Age.fillna(testing_data.Age.mean(), inplace=True)
        testing_data.Fare.fillna(testing_data.Fare.mean(), inplace=True)

        testing_data['Embarked'].replace(['S','C','Q'],[0,1,2],inplace=True)

        testing_data['Age_cat']=0
        testing_data.loc[testing_data['Age']<=12,'Age_cat']=0
        testing_data.loc[(testing_data['Age']>12)&(testing_data['Age']<=17),'Age_cat']=1
        testing_data.loc[(testing_data['Age']>17)&(testing_data['Age']<=64),'Age_cat']=2
        testing_data.loc[testing_data['Age']>64,'Age_cat']=3

        testing_data['Fare_cat']=0
        testing_data.loc[testing_data['Fare']<=7.775,'Fare_cat']=0
        testing_data.loc[(testing_data['Fare']>7.775)&(testing_data['Fare']<=8.662),'Fare_cat']=1
        testing_data.loc[(testing_data['Fare']>8.662)&(testing_data['Fare']<=14.454),'Fare_cat']=2
        testing_data.loc[(testing_data['Fare']>14.454)&(testing_data['Fare']<=26.0),'Fare_cat']=3
        testing_data.loc[(testing_data['Fare']>26.0)&(testing_data['Fare']<=52.369),'Fare_cat']=4
        testing_data.loc[testing_data['Fare']>52.369,'Fare_cat']=5

        testing_data['FamilySize'] = testing_data['Parch'] + testing_data['SibSp']

        testing_data.drop(['Age','Fare','Ticket','SibSp','Parch','PassengerId'],axis=1,inplace=True)

        return testing_data