from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class InputScript(FlaskForm):
    genre1 = BooleanField('Action')
    genre2 = BooleanField('Comedy')

    script = StringField('Script', validators=[DataRequired()])
    submit = SubmitField('Abracadabra')