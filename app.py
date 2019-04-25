from flask import Flask
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wktppibqpzzfnv:9986d2db122c2b8209aca8b727ac9cace056f68c08e3f6169caca7a773820cef@ec2-50-17-227-28.compute-1.amazonaws.com:5432/d54m05ksh0rmq4'
db = SQLAlchemy(app)

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, email):
        self.email = email

    def __repr__(self):
        return '<E-mail %r>' % self.email

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
