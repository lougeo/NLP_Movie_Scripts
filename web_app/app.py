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


if __name__ == '__main__':
    app.run(debug=True)