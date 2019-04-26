from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectField

# some web forms and what not

class UserForm(FlaskForm):
	specialties = [ ('Pediatrician', 'Pediatrician'), ('Cardiologist', 'Cardiologist'), 
	('General Surgeon', 'General Surgeon'), ('Other', 'Other') ]
	first_name = StringField('First Name', [validators.DataRequired(message = 'Please Enter Something')])
	last_name = StringField('Last Name', [validators.DataRequired(message = 'Please Enter Something')])
	email = StringField('Email', [validators.Email(message = 'Please Enter A Valid Email')])
	specialty = SelectField('Specialty', choices = specialties)