from sklearn.ensemble import RandomForestClassifier
import pandas as pd
# import numpy as np commented for flake8 reasons


class MachineLearningRange2:

    def __init__(self):
        self.__data_frame = self.read_csv()
        self.__features = self.__data_frame.columns[:27]
        self.__clf = self.random_forest(self.__data_frame, self.__features)
        self.__target_names = self.get_target_names(self.__data_frame)

    def classify_patient(self, patient):
        predicted = self.__clf.predict(patient)
        return self.__target_names[predicted[0]]

    def calc_probabilities(self, patient):
        probabilities = self.__clf.predict_proba(patient)
        return probabilities

    def random_forest(self, data_frame, features):
        # factorize the classification possibilities
        y = pd.factorize(data_frame['Classificacao'])[0]
        clf = self.train_the_classifier(features, data_frame, y)
        return clf

    def train_the_classifier(self, features, data_frame, y):
        clf = RandomForestClassifier(n_jobs=2)
        clf.fit(data_frame[features], y)
        return clf

    def feature_importance(self):
        return list(zip(self.__data_frame[self.__features],
                        self.__clf.feature_importances_))

    def read_csv(self):
        df = pd.read_csv('apps/risk_rating/class_29d_2m.csv',
                         true_values=["Sim"], false_values=["Não", "Nao"])
        df = df.drop(df.columns[[0, 2, 29]], axis=1)
        columns_tls = list(df.columns.values)

        # changing last and penultimate values
        columns_tls[26], columns_tls[27] = columns_tls[27], columns_tls[26]
        df = df.reindex(columns=columns_tls)

        return df

    def get_target_names(self, data_frame):
        duplicateless_df = data_frame['Classificacao'].drop_duplicates()
        return duplicateless_df.values.tolist()
