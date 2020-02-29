import os
import random
from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

imgs = os.listdir('static/img')
imgs = ['img/' + file for file in imgs]
rights = os.listdir('static/right')
rights = ['right/' + file for file in rights]

nunals = os.listdir('static/album/nuna/nunaleft')
nunals = ['nunaleft/' + file for file in nunals]

nunars = os.listdir('static/album/nuna/nunaright')
nunars = ['nunaright/' + file for file in nunars]

kaewls = os.listdir('static/album/kaew/kaewleft')
kaewls = ['kaewleft/' + file for file in kaewls]

kaewrs = os.listdir('static/album/kaew/kaewright')
kaewrs = ['kaewright/' + file for file in kaewrs]

@app.route('/')
def index():
	imgrand = random.sample(imgs,k=5)
	rightrand = random.sample(rights,k=5)
	return render_template('index.html', imgrand=imgrand, rightrand=rightrand)

@app.route('/album')
def album():
	return render_template('album.html')

@app.route('/kaew')
def kaew():
	return render_template('kaew.html', kaewrs=kaewrs, kaewls=kaewls)

@app.route('/nuna')
def nuna():
	return render_template('nuna.html', nunars=nunars, nunals=nunals)

@app.route('/learn')
def learn():
	return render_template('learn.html')

if __name__=='__main__':
	app.run(debug=True)
