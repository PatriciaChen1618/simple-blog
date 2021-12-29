from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    uid = StringField('User ID', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 64)])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('log in')


class RegisterForm(FlaskForm):
    uid = StringField('User ID', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired(), Length(1, 64)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField('log in')

    def validate_uid(self, field):
        pass
