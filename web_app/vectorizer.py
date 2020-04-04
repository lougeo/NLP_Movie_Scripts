import numpy as np
import pandas as pd

import spacy
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from functions import my_preprocessor, my_tokenizer

X = pd.read_csv('../../data/X_plus.csv')

tfidf = TfidfVectorizer(min_df=0.2, 
                        max_df=0.9, 
                        preprocessor=my_preprocessor, 
                        tokenizer=my_tokenizer, 
                        ngram_range=(1,3)).fit(X['scripts'])

# Most important piece of the puzzle, decreasing the size by 3 order of magnitude
tfidf.stop_words_ = None

# Exporting the fit vectorizer
joblib.dump(tfidf, '../models/tfidf_full.pkl')

# Transforming and building the dataframe for the models to use
X_transformed = tfidf.transform(X['scripts'])
X_vecs = pd.DataFrame(columns=tfidf.get_feature_names(), data=X_transformed.toarray())

X_merged = pd.concat([X.drop('scripts', axis=1).reset_index(drop=True), X_vecs], axis=1)
X_merged.to_csv('../../data/X_merged.csv', columns=X_merged.columns, index=False)
