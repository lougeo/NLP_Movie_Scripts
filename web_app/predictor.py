# Here I need to build a function which creates a dataframe identical to the one used to train the final models
# Then it needs to load the pickled pipeline, and run a prediction
# It also needs to then build those graphs
# Finally, it needs to return all that onto a nice results page

# Organization:
# genre logic
## pos count
## vec transform
# concat pos, vec, and genre
# predict 
# graph
# export

import numpy as np
import pandas as pd

import spacy
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from xgboost import XGBClassifier

import matplotlib.pyplot as plt

# Take the inputs and put them all into a dataframe with 'script' as the column with the script

# This section will count the POS
nlp = spacy.load("en_core_web_sm")
# Initializing columns
df['Num_NOUN'], df['Num_PRON'], df['Num_PROPN'], df['Num_ADJ'], df['Num_VERB'], df['Num_ADV'] = 0, 0, 0, 0, 0, 0

# Initializing the spacy class
doc = nlp(df['script'][0])

# Condition for a good token
for token in doc:
    if (token.is_stop == False) & \
       (token.is_punct == False) & \
       (token.is_space == False) & \
       ('\n' not in str(token)):
        pos = token.pos_
        # Condition for each POS
        if pos == 'NOUN':
            df['Num_NOUN'][i] += 1
        elif pos == 'PRON':
            df['Num_PRON'][i] += 1
        elif pos == 'PROPN':
            df['Num_PROPN'][i] += 1
        elif pos == 'ADJ':
            df['Num_ADJ'][i] += 1
        elif pos == 'VERB':
            df['Num_VERB'][i] += 1
        elif pos == 'ADV':
            df['Num_ADV'][i] += 1


# Vectorizing the input
tfidf = joblib.load('../models/tfidf_full.pkl')
# Transforming the input script
in_transformed = tfidf.transform(string)
# Turning it into a dataframe
X_vecs = pd.DataFrame(columns=tfidf.get_feature_names(), data=in_transformed.toarray())



# Merging all of the features
X_merged = pd.concat([X.drop('scripts', axis=1).reset_index(drop=True), X_vecs], axis=1)


# Predicting on the input dataframe
logreg_imdb = joblib.load('../models/imdb_logreg_full.pkl')
logreg_rt = joblib.load('../models/rt_logreg_full.pkl')
logreg_profit = joblib.load('../models/profit_logreg_full.pkl')
xgbc_imdb = joblib.load('../models/imdb_xgbc_full.pkl')
xgbc_rt = joblib.load('../models/rt_xgbc_full.pkl')
xgbc_profit = joblib.load('../models/profit_xgbc_full.pkl')

logreg_imdb.predict(X_merged)
logreg_rt.predict(X_merged)
logreg_profit.predict(X_merged)

logreg_imdb.predict_proba(X_merged)
logreg_rt.predict_proba(X_merged)
logreg_profit.predict_proba(X_merged)

xgbc_imdb.predict(X_merged)
xgbc_rt.predict(X_merged)
xgbc_profit.predict(X_merged)

xgbc_imdb.predict_proba(X_merged)
xgbc_rt.predict_proba(X_merged)
xgbc_profit.predict_proba(X_merged)