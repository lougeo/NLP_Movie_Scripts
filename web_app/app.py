import numpy as np
import pandas as pd

import spacy
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

from flask import Flask, render_template, redirect, url_for, flash
#from flask_sqlalchemy import SQLAlchemy

from forms import Script_Submit
from functions import script_input, genre_convert, pos_counter, my_preprocessor, my_tokenizer

# Initializing the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '420SWED69'

# # Initializing the db
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# db = SQLAlchemy(app)

# class Script_Data(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     genre1 = db.Column(db.Boolean)
#     genre2 = db.Column(db.Boolean)
#     title = db.Column(db.String)
#     script = db.Column(db.String)

#     def __repr__(self):
#         return f"Script for: {self.title}"


# Loading in the pickles
tfidf = joblib.load('../models/full_tfidf.pkl')
logreg_imdb = joblib.load('../models/imdb_logreg_full.pkl')
logreg_rt = joblib.load('../models/rt_logreg_full.pkl')
logreg_profit = joblib.load('../models/profit_logreg_full.pkl')
xgbc_imdb = joblib.load('../models/imdb_xgbc_full.pkl')
xgbc_rt = joblib.load('../models/rt_xgbc_full.pkl')
xgbc_profit = joblib.load('../models/profit_xgbc_full.pkl')


def merger(script, genre_info):
    #Creating the features
    df_s = script_input(script)
    df_sg = genre_convert(genre_info, df_s)
    df_sgp = pos_counter(df_sg)
    #Transforming the script
    in_transformed = tfidf.transform(df_sgp['script'])
    # Turning it into a dataframe
    df_vecs = pd.DataFrame(columns=tfidf.get_feature_names(), data=in_transformed.toarray())
    # Merging all of the features
    X_merged = pd.concat([df_sgp.drop('script', axis=1).reset_index(drop=True), df_vecs], axis=1)

    return X_merged


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    # Initialize form
    form = Script_Submit()
    # Condition for valid submition
    if form.validate_on_submit():
        # Flash message 
        flash('Script accepted', 'success')
        
        # Dealing with the data locally rather than via db
        global title, df
        title = form.title.data
        script = form.script.data
        genre_info = [[form.genre1.description, form.genre1.data],
                      [form.genre2.description, form.genre2.data],
                      [form.genre3.description, form.genre3.data],
                      [form.genre4.description, form.genre4.data],
                      [form.genre5.description, form.genre5.data],
                      [form.genre6.description, form.genre6.data],
                      [form.genre7.description, form.genre7.data],
                      [form.genre8.description, form.genre8.data],
                      [form.genre9.description, form.genre9.data],
                      [form.genre10.description, form.genre10.data],
                      [form.genre11.description, form.genre11.data],
                      [form.genre12.description, form.genre12.data],
                      [form.genre13.description, form.genre13.data],
                      [form.genre14.description, form.genre14.data],
                      [form.genre15.description, form.genre15.data],
                      [form.genre16.description, form.genre16.data],
                      [form.genre17.description, form.genre17.data],
                      [form.genre18.description, form.genre18.data],
                      [form.genre19.description, form.genre19.data],
                      [form.genre20.description, form.genre20.data],
                      [form.genre21.description, form.genre21.data],
                      [form.genre22.description, form.genre22.data]]
        df = merger(script, genre_info)

        # Sending the data to a database
        # Not implemented yet
        # post = Script_Data(genre1=form.genre1.data,
        #                    genre2=form.genre2.data,
        #                    title=form.title.data,
        #                    script=form.script.data)
        # db.session.add(post)
        # db.session.commit()

        return redirect(url_for('results'))
    return render_template('submit.html', title='Script Submit', form=form)

@app.route('/results', methods=["GET", "POST"])
def results():
    try:
        scores = [logreg_imdb.predict_proba(df),
                logreg_rt.predict_proba(df),
                logreg_profit.predict_proba(df),
                xgbc_imdb.predict_proba(df),
                xgbc_rt.predict_proba(df),
                xgbc_profit.predict_proba(df)]

        return render_template('results.html', title='Results Page', stitle=title, scores=scores)

    except:
        return render_template('results.html', title='Results Page')
    

if __name__ == '__main__':
    app.run(debug=True)
    # db.drop_all() 
    # db.create_all()