from flask import Flask, render_template, redirect, url_for, request,jsonify
from flask_bootstrap import Bootstrap
import sqlite3
import webbrowser

app = Flask(__name__)
Bootstrap(app)
db='data.db'

@app.route("/",methods=['GET', 'POST'])
def home():
  return render_template("index.html")
 
@app.route("/allbooks",methods=['GET', 'POST'])
def visualizzaTutto():
  conn=sqlite3.connect(db)
  c=conn.cursor()
  c.execute("SELECT * FROM Libri")
  rows = c.fetchall()
  c.close()
  conn.close()
  #  name=#read from db sqlite
  print(rows)
  return jsonify(rows)
   # return render_template("visualizza.html",nomeLibro=name,autore=autore,annoPubblicazione=anno)

@app.route('/addbook',methods=['GET','POST'])
def aggiungi():
  return "<p>va libro</p>"  #render_template("agglibro.html")

'''
@app.route('/research',methods=['GET','POST'])
def ricerca():

  return 
'''
if __name__ == "__main__":
  app.run()



