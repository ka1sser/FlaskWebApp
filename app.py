from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET KEY"] = "secret"

posts = [
    {"author": "Edward Elric",
     "title": "Jumpin' Fun!",
     "content": "Lots of frogs can leap more than 20 times their body length.",
     "date posted": "April 3, 2021"},
    {"author": "Alphonse Elric",
     "title": "Grizzly Jaw",
     "content": "The bite of a grizzly bear is  strong enough to crush a bowling bowl. Yikes!",
     "date posted": "April 24, 2021"}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/animal')
def animal():
    return render_template('animal.html', posts=posts, title="Fun Animal Facts")

