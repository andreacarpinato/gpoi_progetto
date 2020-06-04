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
  error=None
  if request.method == 'POST':
    titolo=request.form['titolo']
    autore=request.form['autore']
    anno=request.form['anno']
    genere=request.form['genere']
    conn=sqlite3.connect(db)
    c=conn.cursor()
    #print(f'INSERT INTO Libri("title","author","year_published") VALUES ("{title}", "{author}","{year}")')
    c.execute(f'INSERT INTO Libri("titolo","autore","anno","genere") VALUES ("{titolo}", "{autore}","{anno}","{genere}")')
    c.execute('commit') #salva modifiche db
    c.close()
    conn.close()
    return render_template('index.html')
  else :
    return render_template("agglibro.html")


@app.route('/research',methods=['GET'])
def ricerca():
  error=None
  print('ciao1')
  if request.method == 'GET':
    print('ciao2')
    conn=sqlite3.connect(db)
    c=conn.cursor()  
    print('ciao3')
    ricerca=request.form['ricerca']
    c.execute(f"SELECT * FROM Libri where titolo={ricerca}")
    ris = c.fetchall()
    c.close()
    conn.close()
    return jsonify(ris)
  else:
    return render_template("ricerca.html")
    

  #return render_template("ricerca.html")




















if __name__ == "__main__":
  app.run()



