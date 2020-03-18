from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class Script_Submit(FlaskForm):
    # Genres
    genre1 = BooleanField('Action')
    genre2 = BooleanField('Comedy')
    # Title
    title = StringField('Title', validators=[DataRequired()])
    # Script
    script = TextAreaField('Script', validators=[DataRequired()])
    # Submit button
    submit = SubmitField('Abracadabra')