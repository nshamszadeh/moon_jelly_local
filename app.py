from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from forms import UserForm

# Some boilerplate setup stuff.

app = Flask(__name__)

# URL should be whatever database URL is being used (if testing on your own use a database different from the team's )
app.config['SQLALCHEMY_DATABASE_URI'] = '    postgres://wktppibqpzzfnv:9986d2db122c2b8209aca8b727ac9cace056f68c08e3f6169caca7a773820cef@ec2-50-17-227-28.compute-1.amazonaws.com:5432/d54m05ksh0rmq4'
app.config['SECRET_KEY'] = 'mOon_jElLy wAs oRiGiNa11y g0nNa b3 SuP3r MaRi0 gAlAxY' # need to change later
# im not mocking Aidan, this key actually needs to be secure which is why it looks all crazy

db = SQLAlchemy(app) # wow we have a database

# Create our database model. 
class User(db.Model):

  __tablename__ = "users"

  # Each user (doctor) will have all these things attributed to him or her
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.Text, unique=True)
  first_name = db.Column(db.Text)
  last_name = db.Column(db.Text)
  specialty = db.Column(db.Text)

  # initialize the object
  def __init__(self, email, first_name, last_name, specialty):
    self.email = email
    self.first_name = first_name
    self.last_name = last_name
    self.specialty = specialty

# This is the main homepage for now. GET and POST are for web forms.
@app.route('/', methods = ['GET', 'POST'])
def homepage():
  
  # define a form object
  user_form = UserForm()

  # if we are posting a form, i.e. submitting a form, store all the info in these variables
  if request.method == 'POST':
    first_name = request.form['first_name'] 
    last_name = request.form['last_name']
    email = request.form['email']
    specialty = request.form['specialty']

    # if the inputs we're all validated by WTforms (improve validation later)
    if user_form.validate(): 
      # then store info in an initialized User object and store the object in the database
      new_user = User(email, first_name, last_name, specialty)
      db.session.add(new_user) # add to database
      db.session.commit() # for some reason we also need to commit it otherwise it won't add
    else:
      print("Invalid input(s)!")

  # add html file here
  return render_template('index.html', form = user_form)


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
