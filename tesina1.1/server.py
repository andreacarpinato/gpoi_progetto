from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import sqlite3

app = Flask(__name__)
Bootstrap(app)

@app.route("/",methods=['GET', 'POST'])
def home():
    return render_template("index.html")
'''
@app.route("/allbooks",methods=['GET', 'POST'])
def visualizzaTutto():
  #  name=#read from db sqlite

    return render_template("visualizza.html",nomeLibro=name,autore=autore,annoPubblicazione=anno)

@app.route('/addbook',methods=['GET','POST'])
def aggiungi(name,author,)

'''
if __name__ == "__main__":
    app.run()



