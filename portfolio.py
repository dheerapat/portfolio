import os
import random
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')
imgs = os.listdir('static/img')
imgs = ['img/' + file for file in imgs]
rights = os.listdir('static/right')
rights = ['right/' + file for file in rights]

@app.route('/')
def index():
	imgrand = random.sample(imgs,k=10)
	rightrand = random.sample(rights,k=10)
	return render_template('index.html', imgrand=imgrand, rightrand=rightrand)

@app.route('/album')
def album():

	return render_template('album.html')
	
if __name__=='__main__':
	app.run(debug=True)
