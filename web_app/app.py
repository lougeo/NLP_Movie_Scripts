import numpy as np
import pandas as pd

import spacy
import joblib
from urllib.request import urlopen
from threading import Thread

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

from flask import Flask, render_template, redirect, url_for, flash

from forms import Script_Submit
from functions import script_input, genre_convert, pos_counter, my_preprocessor, my_tokenizer

# Initializing the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '420SWED69'

# Has to be defined in this file rather than functions file
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


tfidf = joblib.load("static/models/full_tfidf_2.pkl")

logreg_imdb = joblib.load("static/models/imdb_logreg_full.pkl")
logreg_rt = joblib.load("static/models/rt_logreg_full.pkl")
logreg_profit = joblib.load("static/models/profit_logreg_full.pkl")
xgbc_imdb = joblib.load("static/models/imdb_xgbc_full.pkl")
xgbc_rt = joblib.load("static/models/rt_xgbc_full.pkl")
xgbc_profit = joblib.load("static/models/profit_xgbc_full.pkl")

# s3 links
# Loading in the pickles
# tfidf = joblib.load(urlopen("https://gsbs.s3.us-east-2.amazonaws.com/full_tfidf_2.pkl"))

# logreg_imdb = joblib.load(urlopen("https://gsbs.s3.us-east-2.amazonaws.com/imdb_logreg_full.pkl"))
# logreg_rt = joblib.load(urlopen("https://gsbs.s3.us-east-2.amazonaws.com/rt_logreg_full.pkl"))
# logreg_profit = joblib.load(urlopen("https://gsbs.s3.us-east-2.amazonaws.com/profit_logreg_full.pkl"))
# xgbc_imdb = joblib.load(urlopen("https://gsbs.s3.us-east-2.amazonaws.com/imdb_xgbc_full.pkl"))
# xgbc_rt = joblib.load(urlopen("https://gsbs.s3.us-east-2.amazonaws.com/rt_xgbc_full.pkl"))
# xgbc_profit = joblib.load(urlopen("https://gsbs.s3.us-east-2.amazonaws.com/profit_xgbc_full.pkl"))
 

# Home page
@app.route("/")
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template('home.html')

# Home page
@app.route("/info", methods=["GET", "POST"])
def info():
    return render_template('info.html')

# Submit page
@app.route("/submit", methods=["GET", "POST"])
def submit():
    # Initialize form
    form = Script_Submit()
    # Condition for valid submition
    if form.validate_on_submit():
        # Flash message 
        #try:
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

        return redirect(url_for('results'))
        # except:
        #     return redirect(url_for('error_page'))
    return render_template('submit.html', title='Script Submit', form=form)

# Results page
@app.route('/results', methods=["GET", "POST"])
def results():
    try:
        y = pd.read_csv('static/y_wt.csv')
        scores = [logreg_imdb.predict_proba(df)[0] * 100,
                    logreg_rt.predict_proba(df)[0] * 100,
                    logreg_profit.predict_proba(df)[0] * 100,
                    xgbc_imdb.predict_proba(df)[0] * 100,
                    xgbc_rt.predict_proba(df)[0] * 100,
                    xgbc_profit.predict_proba(df)[0] * 100]
        scores_c = []
        real_scores = []
        acc = []
        verifier = 0
        for i in scores:
            if i[0] > i[1]:
                scores_c.append(['BAD!', round(i[0])])
            else:
                scores_c.append(['GOOD!', round(i[1])])

        for i in y['titles']:
            if i == title:
                verifier += 1

                imdb_real = float(y[y['titles'] == title]['IMDb_score']) * 100
                rt_real = float(y[y['titles'] == title]['RT_score']) * 100
                profit_real = int(y[y['titles'] == title]['Per_Profit'])
                real_scores.append(imdb_real)
                real_scores.append(rt_real)
                real_scores.append(profit_real)

                for i in [scores_c[0], scores[3]]:
                    if (i[0] == "GOOD!") & (imdb_real >= 70):
                        acc.append('Predicted: CORRECT!')
                    elif (i[0] == "BAD!") & (imdb_real < 70):
                        acc.append('Predicted: CORRECT!')
                    else:
                        acc.append('Predicted: WRONG!')
                
                for i in [scores_c[1], scores[4]]:
                    if (i[0] == "GOOD!") & (rt_real >= 80):
                        acc.append('Predicted: CORRECT!')
                    elif (i[0] == "BAD!") & (rt_real < 80):
                        acc.append('Predicted: CORRECT!')
                    else:
                        acc.append('Predicted: WRONG!')
                
                for i in [scores_c[2], scores[5]]:
                    if (i[0] == "GOOD!") & (imdb_real >= 200):
                        acc.append('Predicted: CORRECT!')
                    elif (i[0] == "BAD!") & (imdb_real < 200):
                        acc.append('Predicted: CORRECT!')
                    else:
                        acc.append('Predicted: WRONG!')

        if verifier == 0:
            acc.append(['','','','','',''])
            real_scores.append(['','','','','',''])
            
        return render_template('results.html', title='Results Page', stitle=title, scores_c=scores_c, real_scores=real_scores, acc=acc)

    except:
        return render_template('error.html', title='Error')

# error page
@app.route('/error', methods=["GET", "POST"])
def error_page():
    return render_template('error.html', title='Error')

if __name__ == '__main__':
    app.run(debug=True)





#############################################
# Threading code, also not working right now
#############################################


# def load_pickles():
#     global tfidf, logreg_imdb, logreg_rt, logreg_profit, xgbc_imdb, xgbc_rt, xgbc_profit

#Thread(target=load_pickles).start()
#load_pickles()

# thread = Thread(target=load_pickles, args=())
# thread.daemon = True
# thread.start()




######################################
# DATABASE CODE - UNUSED AT THE MOMENT
######################################

#from flask_sqlalchemy import SQLAlchemy


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


        # Sending the data to a database
        # Not implemented yet
        # post = Script_Data(genre1=form.genre1.data,
        #                    genre2=form.genre2.data,
        #                    title=form.title.data,
        #                    script=form.script.data)
        # db.session.add(post)
        # db.session.commit()

    # db.drop_all() 
    # db.create_all()


