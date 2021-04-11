#import Flask dependencies
from flask import Flask

#Crete new Flask App Instance
app = Flask(__name__)

#Create Flask Routes
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/Pashmina')
def name():
    return (f'Pashmina Sangani')

