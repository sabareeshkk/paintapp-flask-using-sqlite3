from flask import Flask,request,render_template,redirect,request,send_from_directory,session,flash,g,url_for
import sqlite3
import os
import json

#creating app

app = Flask(__name__)

#setting the secret key
app.secret_key = "sabareeshk"

#database connection every request
@app.before_request
def before_request():
    g.db = sqlite3.connect("pics.db")

#database close after response
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
#go to the home page 
@app.route('/')
def home():
	return render_template('paintnew.html')

#to add the favicon in the bar
@app.route('/favicon.ico')
def favicon():
	 return send_from_directory(os.path.join(app.root_path, 'static'),'favcon.ico', mimetype='image/vnd.microsoft.icon')

#go the gallery of images
@app.route('/gallery/<filename>',methods=['GET'])
def load(filename=None):
	cur = g.db.execute("SELECT * FROM paintstore WHERE title=(?)",[filename])	
	posts=[dict(id=i[0],title=i[1],imagedata=i[2]) for i in cur.fetchall()]
	return render_template('picload.html',posts=posts)

@app.route('/<filename>',methods=['POST'])
def save(filename=None):
	cur = g.db.execute("INSERT INTO paintstore (title,imagedata) VALUES (?,?)",[request.form['name'],request.form['data']])
	g.db.commit()
	#conn.close()
	return render_template('paintnew.html')

@app.route('/gallery')
def gallery():
	cur = g.db.execute("SELECT * FROM paintstore ORDER BY id desc")
	posts=[dict(id=i[0],title=i[1]) for i in cur.fetchall()]	
	return render_template('gallery.html',posts=posts)

if __name__ == '__main__':
	app.run(debug = True)
