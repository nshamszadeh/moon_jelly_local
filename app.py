from flask import Flask
from datetime import datetime
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ricculxqdypnfh:d8283cc0c6d1c05d5874a972d5176b29c24751188711916086c6e4537f035274@ec2-23-21-136-232.compute-1.amazonaws.com:5432/dfuo44q4pq80o6'
db = SQLAlchemy(app)

# Create our database model
"""
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email
"""
@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %I:%M %p")

# add html code here
    return """
    <h1>Hello heroku</h1>
    <p> Visit the <a href="http://moon-jelly-test.herokuapp.com/grid">Grid</a>?<br />
    </p>
    <p>It is currently {time}.</p>
    
    """.format(time=the_time)

@app.route('/grid')
def grid():

# add html code here
    return """
    <title>Example</title>
	<style>
	#grid { 
  		display: grid;
  		grid-template-rows: 1fr 1fr 1fr;
  		grid-template-columns: 1fr 1fr 1fr;
  		grid-gap: 2vw;
  	}
	#grid > div {
  		font-size: 5vw;
  		padding: .5em;
  		background: gold;
  		text-align: center;
	}
	</style>
	<div id="grid">
  		<div>1</div>
  		<div>2</div>
  		<div>3</div>
  		<div>4</div>
  		<div>5</div>
  		<div>6</div>
  		<div>7</div>
  		<div>8</div>
  		<div>9</div>
	</div>
"""

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
