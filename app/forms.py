from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from app.models import User

class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    email = StringField("email",validators=[DataRequired(),Email()])
    first_name = StringField("First Name",validators=[DataRequired()])
    last_name = StringField("Last Name")
    password = PasswordField("Password",validators=[DataRequired()])
    password2 = PasswordField("Re-Enter Password",validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField("Register")

    def validate_email(self,email):
        u = User.query.filter_by(id=email.data).first()
        if u is not None:
           raise ValidationError("Duplicate email")
    