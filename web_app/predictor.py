import numpy as np
import pandas as pd

import spacy
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

from xgboost import XGBClassifier

import matplotlib.pyplot as plt

# Take the inputs and put them all into a dataframe with 'script' as the column with the script
def script_input(script):
    lscript = [script]
    df = pd.DataFrame({'script':lscript}, index=range(len(lscript)))
    return df

def genre_convert(genre_info, df):
    for i in genre_info:
        if i[1] == True:
            df[i[0]] = 1
            return df
        else:
            df[i[0]] = 0
            return df

# This section will count the POS HAS TO GO AFTER A DF WITH SCRIPT AND GENRES HAS BEEN CREATED
def pos_counter(df):
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
            # This modification from the pos counter in my notebooks is kind of hacky:
            # It turns all values of the given column to a 1 given the condition, as opposed to only the values for the given script.
            # I'm ok with this because if anything will get saved, it will be an output file with the results of individual scripts.
            # Therefore, I only need the info for the most recent input script. 
            if pos == 'NOUN':
                df['Num_NOUN'] = 1
            elif pos == 'PRON':
                df['Num_PRON'] = 1
            elif pos == 'PROPN':
                df['Num_PROPN'] = 1
            elif pos == 'ADJ':
                df['Num_ADJ'] = 1
            elif pos == 'VERB':
                df['Num_VERB'] = 1
            elif pos == 'ADV':
                df['Num_ADV'] = 1
    return df

def feature_df(script, genre_info):
    df_s = script_input(script)
    df_sg = genre_convert(genre_info, df_s)
    df_sgp = pos_counter(df_sg)

    return df_sgp

# Can this function call tfidf?
def script_transformer(df):
    # Vectorizing the input
    # Transforming the input script
    in_transformed = tfidf.transform(df['script'][0])
    # Turning it into a dataframe
    X_vecs = pd.DataFrame(columns=tfidf.get_feature_names(), data=in_transformed.toarray())

    return X_vecs


def merger(df_features, df_vectors):
    # Merging all of the features
    X_merged = pd.concat([df_features.drop('scripts', axis=1).reset_index(drop=True), df_vectors], axis=1)

    return X_merged




# logreg_imdb.predict(X_merged)
# logreg_rt.predict(X_merged)
# logreg_profit.predict(X_merged)

# logreg_imdb.predict_proba(X_merged)
# logreg_rt.predict_proba(X_merged)
# logreg_profit.predict_proba(X_merged)

# xgbc_imdb.predict(X_merged)
# xgbc_rt.predict(X_merged)
# xgbc_profit.predict(X_merged)

# xgbc_imdb.predict_proba(X_merged)
# xgbc_rt.predict_proba(X_merged)
# xgbc_profit.predict_proba(X_merged)