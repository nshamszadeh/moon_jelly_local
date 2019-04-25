from flask import Flask, render_template
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = '    postgres://wktppibqpzzfnv:9986d2db122c2b8209aca8b727ac9cace056f68c08e3f6169caca7a773820cef@ec2-50-17-227-28.compute-1.amazonaws.com:5432/d54m05ksh0rmq4'
db = SQLAlchemy(app)

# Reusable Web Form
class ReusableForm(Form):
  name = TextField('Name:', validators =  [validators.required()])


# Create our database model
class User(db.Model):
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)

def __init__(self, email):
  self.email = email

def __repr__(self):
  return '<E-mail %r>' % self.email

@app.route('/', methods = ['GET', 'POST'])
def homepage():
  form = ReusableForm(request.form)
  the_time = datetime.now().strftime("%A, %d %b %Y %I:%M %p")
  print (form.errors)
  if request.method == 'POST':
    name = request.form['name']
    print (name)


# add html file here
  return render_template('index.html', time=the_time, form = form)


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
