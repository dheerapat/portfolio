import os
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
imgs = os.listdir('static/img')
imgs = ['img/' + file for file in imgs]
rights = os.listdir('static/right')
rights = ['right/' + file for file in rights]

@app.route('/')
def index():
	return render_template('index.html', imgs=imgs, rights=rights)
	
if __name__=='__main__':
	app.run(debug=True)
