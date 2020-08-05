from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length


# Creamos los formularios en clases que heredan el modulo FlaskForm
class SignupForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired(), Length(max=64)])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Registrar')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recuerdame')
    submit = SubmitField('Login')
