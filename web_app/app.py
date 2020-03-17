from flask import Flask, render_template, redirect, url_for, flash
from forms import InputScript
app = Flask(__name__)

app.config['SECRET_KEY'] = '420SWED69'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    form = InputScript()
    if form.validate_on_submit():
        flash('Script accepted', 'success')
        return redirect(url_for('home'))
    return render_template('submit.html', title='Script Submit', form=form)

@app.route('/predict/', methods=['POST'])
def predict_sentiment():
    input_json = request.get_json(force=True)
    print(f'Data sent in request:{input_json}')

    # Read the review data and apply preprocessing (vectorization)
    review_text = [input_json['review']]
    print('Vectorizing data')
    countvectorizer = joblib.load("models/count_vectorizer.pkl")    
    X_new = countvectorizer.transform(review_text)
    
    # Score the model
    print('Scoring...')
    sentiment_logit = joblib.load("models/sentiment_logit.pkl")
    sentiment_score = sentiment_logit.predict_proba(X_new)[0]
    print(sentiment_score)
    negative_score = sentiment_score[0]
    positive_score = sentiment_score[1]

    return jsonify({"positive":positive_score, "negative":negative_score})


if __name__ == '__main__':
    app.run(debug=True)