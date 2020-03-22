from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired

class Script_Submit(FlaskForm):
    # Genres
    genre1 = BooleanField('Action', description='Action')
    genre2 = BooleanField('Adventure', description='Adventure')
    genre3 = BooleanField('Animation', description='Animation')
    genre4 = BooleanField('Biography', description='Biography')
    genre5 = BooleanField('Comedy', description='Comedy')
    genre6 = BooleanField('Crime', description='Crime')
    genre7 = BooleanField('Drama', description='Drama')
    genre8 = BooleanField('Family', description='Family')
    genre9 = BooleanField('Fantasy', description='Fantasy')
    genre10 = BooleanField('FilmNoir', description='FilmNoir')
    genre11 = BooleanField('History', description='History')
    genre12 = BooleanField('Horror', description='Horror')
    genre13 = BooleanField('HorrorMystery', description='HorrorMystery')
    genre14 = BooleanField('Music', description='Music')
    genre15 = BooleanField('Musical', description='Musical')
    genre16 = BooleanField('Mystery', description='Mystery')
    genre17 = BooleanField('Romance', description='Romance')
    genre18 = BooleanField('SciFi', description='SciFi')
    genre19 = BooleanField('Sport', description='Sport')
    genre20 = BooleanField('Thriller', description='Thriller')
    genre21 = BooleanField('War', description='War')
    genre22 = BooleanField('Western', description='Western')
    
    # Title
    title = StringField('Title', validators=[DataRequired()])
    # Script
    script = TextAreaField('Script', validators=[DataRequired()])
    # Submit button
    submit = SubmitField('Abracadabra')
