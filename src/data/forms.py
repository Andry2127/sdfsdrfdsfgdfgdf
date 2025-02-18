from flask_wtf import FlaskForm
import wtforms


class SignUpForm(FlaskForm):
    first_name = wtforms.StringField("Enter your name")
    last_name = wtforms.StringField("Enter your last name")
    email = wtforms.EmailField("Email", validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    password = wtforms.PasswordField("Password", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Sing up")



class LogInForm(FlaskForm):
    email = wtforms.EmailField("Email", validators=[wtforms.validators.DataRequired(), wtforms.validators.Email()])
    password = wtforms.PasswordField("Password", validators=[wtforms.validators.length(6)])
    submit = wtforms.SubmitField("Log in")

