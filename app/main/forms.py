from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField


class NameForm(FlaskForm):
    name = StringField('What\'s your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    body = PageDownField('Notes', validators=[DataRequired()])
    submit = SubmitField('Submit')