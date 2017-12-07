from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import re



class MachineLearning:

    def __init__(self, csv, cls):
        self.__csv = csv
        self.__data_frame = self.read_csv()

        if cls:
            cls_df = pd.DataFrame(list(cls))
            del cls_df['id']
            cls_df = cls_df.rename(columns={'classification': 'Classificacao'})
            self.classification_number_to_string(cls_df)
            snake_case_name_list = self.camel_to_snake_case(list(self.__data_frame))
            snake_case_name_list2 = self.camel_to_snake_case(list(cls_df))
            print(snake_case_name_list)
            print(snake_case_name_list2)
            # self.__data_frame = pd.concat([self.__data_frame, cls_df])

        data_frame_length = len(list(self.__data_frame))
        self.__features = self.__data_frame.columns[:data_frame_length-1]
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
        df = pd.read_csv(self.__csv,
                         true_values=["Sim"], false_values=["Não", "Nao"])
        df = df.drop(["Carimbo de data/hora", "Diagnostico", "profissional"],
                     axis=1)
        # columns_tls are the columns tiles
        columns_tls = df.columns.tolist()
        for index in range(len(columns_tls)):
            if columns_tls[index] == 'Classificacao':
                # changing last and penultimate values
                columns_tls[index], columns_tls[-1] = columns_tls[-1], \
                                                      columns_tls[index]
                break

        df = df.reindex(columns=columns_tls)
        return df

    def get_target_names(self, data_frame):
        duplicateless_df = data_frame['Classificacao'].drop_duplicates()
        return duplicateless_df.values.tolist()

    def classification_number_to_string(self, data_frame):

        for idx, val in enumerate(data_frame['Classificacao']):

            if val == 1:
                data_frame['Classificacao'][idx] = 'AtendimentoImediato'
            elif val == 2:
                data_frame['Classificacao'][idx] = 'AtendimentoHospitalar'
            elif val == 3:
                data_frame['Classificacao'][idx] = 'AmbulatorialGeral'
            elif val == 4:
                data_frame['Classificacao'][idx] = 'AtendimentoEletivo'

    def camel_to_snake_case(self, names):
        name_list = []
        for name in names:
            s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
            snake_name = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

            name_list.append(snake_name)

        return name_list
