from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email
from wtforms import TextField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField

class ContactForm(FlaskForm):
    name = TextField("Name", [InputRequired()])
    email = EmailField("Email", [InputRequired(), Email()])
    textarea = TextAreaField("Message", [InputRequired()])
    submit = SubmitField("Submit")