import numpy as np
import pandas as pd

import spacy
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

from flask import Flask, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from forms import Script_Submit
from functions import feature_df, script_transformer, merger, my_preprocessor, my_tokenizer

# Initializing the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '420SWED69'

# Initializing the db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# Loading in the pickles
tfidf = joblib.load('../models/full_tfidf.pkl')
logreg_imdb = joblib.load('../models/imdb_logreg_full.pkl')
logreg_rt = joblib.load('../models/rt_logreg_full.pkl')
logreg_profit = joblib.load('../models/profit_logreg_full.pkl')
xgbc_imdb = joblib.load('../models/imdb_xgbc_full.pkl')
xgbc_rt = joblib.load('../models/rt_xgbc_full.pkl')
xgbc_profit = joblib.load('../models/profit_xgbc_full.pkl')


class Script_Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    genre1 = db.Column(db.Boolean)
    genre2 = db.Column(db.Boolean)
    title = db.Column(db.String)
    script = db.Column(db.String)

    def __repr__(self):
        return f"Script for: {self.title}"


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = Script_Submit()
    if form.validate_on_submit():
        flash('Script accepted', 'success')
        # Dealing with the data locally
        global title, script, genre_info
        title = form.title.data
        script = form.script.data
        genre_info = [[form.genre1.label, form.genre1.data],
                      [form.genre2.label, form.genre2.data]]
        df_features = feature_df(script, genre_info)
        df_vecs = script_transformer(df_features)
        # Sending the data to a database
        # Not implemented yet
        post = Script_Data(genre1=form.genre1.data,
                           genre2=form.genre2.data,
                           title=form.title.data,
                           script=form.script.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('results'))
    return render_template('submit.html', title='Script Submit', form=form)

@app.route('/results', methods=["GET", "POST"])
def results():
    
    return render_template('results.html', title='Results Page', test=title)

if __name__ == '__main__':
    app.run(debug=True)
    db.drop_all() 
    db.create_all()