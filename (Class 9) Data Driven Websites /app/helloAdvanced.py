
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

visitor_counter = 0 # set a variable used to track visitors to our URL

def get_time_message():
    datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%H:%M:%S')
    message = "The date is {d} and the time is {t}"
    return message.format(d=date, t=time)

@app.route("/")
def home():
    message = get_time_message()
    return render_template("index.html")

@app.route("/hello")
def hello_visitor():
    global visitor_counter # global gets updated each time someone visits /hello
    visitor_counter += 1
    return "<H1> Hello! You are visitor #{i}</H1>".format(i=visitor_counter)

app.run(host='0.0.0.0',port=5000,debug=True)
