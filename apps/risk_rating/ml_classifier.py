from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np


def classify_csv():
    df = pd.read_csv('apps/risk_rating/class_menos_28.csv', true_values=["Sim"], false_values=["Não", "Nao"])
    df = df.drop(df.columns[[0, 2, 30]], axis=1)

    columnsTitles = list(df.columns.values)
    columnsTitles[27], columnsTitles[28] = columnsTitles[28], columnsTitles[27]
    df = df.reindex(columns=columnsTitles)


    # target_names = np.array(['Ambulatorial', 'Grave'], dtype='<U12')
    df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

    train, test = df[df['is_train']==True], df[df['is_train']==False]

    print('Number of observations in the training data:', len(train))
    print('Number of observations in the test data:',len(test))

    features = df.columns[1:12]

    y = pd.factorize(train['Classificacao'])[0]

    clf = RandomForestClassifier(n_jobs=2)

    clf.fit(train[features], y)

    preds = df['Classificacao'].unique()[clf.predict(test[features])]

    print('\n'*3)
    print(pd.crosstab(test['Classificacao'], preds, rownames=['Actual'], colnames=['Predicted']))
    print('\n'*3)

    print(list(zip(train[features], clf.feature_importances_)))

    print(clf.predict_proba(test[features])[0:10])
