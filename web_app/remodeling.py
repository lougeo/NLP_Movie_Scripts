import numpy as np
import pandas as pd

import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


# Reading in the data
X = pd.read_csv('../../data/X_merged.csv')
y = pd.read_csv('../../data/y.csv')

y_imdb = y.loc[:, 'IMDb_score'].to_frame()
y_rt = y.loc[:, 'RT_score'].to_frame()
y_profit = y.loc[:, 'Per_Profit'].to_frame()


# Modeling
# Hyperparameters are those identified as optimal in the modeling notebook

logreg_imdb = LogisticRegression(C=0.1, 
                                 penalty='l2').fit(X, y_imdb)
joblib.dump(logreg_imdb, '../models/full_imdb_logreg.pkl')

rf_rt = RandomForestClassifier(max_depth=None, 
                               n_estimators=500).fit(X, y_rt)
joblib.dump(rf_rt, '../models/full_rt_rf.pkl')

rf_profit = RandomForestClassifier(max_depth=None, 
                                   n_estimators=500).fit(X, y_profit)
joblib.dump(rf_profit, '../models/full_profit_rf.pkl')