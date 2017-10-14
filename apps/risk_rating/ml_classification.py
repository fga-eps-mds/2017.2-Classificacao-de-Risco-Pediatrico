from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


def classify_csv():
    df = pd.read_csv('apps/risk_rating/classificacao.csv',
                     usecols=range(1, 13), true_values=["Sim"],
                     false_values=["Não"])

    df.loc[:, 'Idade'] /= 100

    # target_names = np.array(['Ambulatorial', 'Grave'], dtype='<U12')
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

    train, test = df[df['is_train'] is True], df[df['is_train'] is False]

    print('Number of observations in the training data:', len(train))
    print('Number of observations in the test data:', len(test))

    features = df.columns[1:12]

    y = pd.factorize(train['Gravidade'])[0]

    clf = RandomForestClassifier(n_jobs=2)

    clf.fit(train[features], y)

    preds = df['Gravidade'].unique()[clf.predict(test[features])]

    print('\n' * 3)
    print(pd.crosstab(test['Gravidade'], preds,
                      rownames=['Actual'], colnames=['Predicted']))
    print('\n' * 3)

    print(list(zip(train[features], clf.feature_importances_)))
