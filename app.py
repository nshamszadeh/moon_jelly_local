from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %I:%M %p")

# add html code here
    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)