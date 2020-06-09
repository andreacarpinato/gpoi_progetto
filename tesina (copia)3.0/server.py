from flask import Flask, render_template, redirect, url_for, request,jsonify
from flask_bootstrap import Bootstrap
import sqlite3


app = Flask(__name__)
Bootstrap(app)
db='data.db'

@app.route("/",methods=['GET', 'POST'])
def home():
  return render_template("index.html")
 
@app.route("/allbooksJson",methods=['GET', 'POST'])
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

def linkgenerator(id):
  id=str(id)
  url="http://127.0.0.1:5000/book?id="+id
  return url

@app.route('/book',methods=['GET'])
def api_id():
  if 'id' in request.args:
    id = int(request.args['id'])
  else:
    return "Error: No id field provided. Please specify an id."
  conn=sqlite3.connect(db)
  c=conn.cursor()
  c.execute(f'SELECT titolo FROM Libri WHERE idL={id}')
  title=c.fetchall()
  t=title[0][0]
  print(t)
  c.execute(f'SELECT testo FROM Commenti WHERE idLibro={id}')
  rows = c.fetchall()
  c.close()
  conn.close()
  return render_template("libro.html",results=rows,title=t)
  

@app.route('/viewbooks',methods=['GET'])
def vedilibri():
  conn=sqlite3.connect(db)
  c=conn.cursor()
  c.execute("SELECT * FROM Libri")
  rows = c.fetchall()
  c.close()
  conn.close()
  for c in range(0,len(rows)):
    url=linkgenerator(rows[c][0])
    x=rows[c][0]
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute(f'UPDATE Libri SET link ="{url}" WHERE idL={x}')
    c.execute('commit')
    c.close()
    conn.close()
    print(url)
    
    #rows[c][5]=url
  conn=sqlite3.connect(db)
  c=conn.cursor()
  c.execute("SELECT * FROM Libri")
  rows = c.fetchall()
  c.close()
  conn.close()
  print(rows)

  return render_template("libri.html",results=rows)


@app.route('/addcommento',methods=['GET','POST'])
def aggcommento():
  conn=sqlite3.connect(db)
  c=conn.cursor()
  c.execute("Select idL,titolo from Libri")
  titoli=c.fetchall()
  c.close()
  conn.close()
  print(titoli)
  print(len(titoli))
  print(titoli[2])
  print(titoli[2][1])
  for result in titoli :
    #<option  value="{{ result.idLibro }}">{{ result.titolo }}</option>
    print(result[0])
    print(result[1])
  
  '''
  title=[] 
  for c in range(0,len(titoli)):
    title.append(titoli[c][0])
  print(title)
  '''
  error=None
  
  if request.method=='POST':
    print("if request.method=='POST':")
    idLibro=request.form['idLibroComment']
   # print("Il titolo e' "+titolo)
    commento=request.form['comment']
    conn=sqlite3.connect(db)
    c=conn.cursor()
    print('ciao')
  #  c.execute(f'Select idL from Libri where idL="{idLibro}"')
   # idlibro=c.fetchall()
    #idlibro=int(idlibro)
    c.execute(f'INSERT INTO Commenti("idLibro","testo") VALUES("{idLibro}","{commento}")')
    c.execute('commit')
    c.close()
    conn.close()
    return redirect(url_for('/'))
  
  return render_template("addcommento.html",results=titoli)  #trasforma titoli in array
  

@app.route('/recensioni',methods=['GET','POST'])
def visualizzaRecensioni():
  #titolo="Pensieri"
  conn=sqlite3.connect(db)
  c=conn.cursor()    #Libri.titolo="{titolo}" AND
  c.execute(f'Select idL,titolo,testo from Commenti,Libri WHERE Commenti.idLibro=Libri.idL ORDER BY Titolo desc')
  libriRecensiti=c.fetchall()
  c.close()
  conn.close()
  recensioni=[]
  for c in range(0,len(libriRecensiti)):
    #recensioni.append(libriRecensiti[c][0])
    print(libriRecensiti[c][0])
    print(libriRecensiti[c][1])
    print(libriRecensiti[c][2])
  return render_template('recensioni.html',results=libriRecensiti)

'''
@app.route('/recensionilibro',methods=['GET','POST'])
def ricercaRecensioni():
  titolo="Pensieri"
  conn=sqlite3.connect(db)
  c=conn.cursor()
  c.execute("Select titolo from Libri")
  titoli=c.fetchall()
  c.close()
  conn.close()
  title=[]
  titolo=request.form['risultato']
  for c in range(0,len(titoli)):
    title.append(titoli[c][0])
  #redirect
  return render_template('ricercarec.html',risultati=title)

'''
#

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

'''
@app.route('/research',methods=['GET'])
def ricerca():
  error=None
  print('ciao1')
  cont=0
  if request.method == 'GET':
  
    print('ciao2')
    conn=sqlite3.connect(db)
    c=conn.cursor()  
    print('ciao3')
    #ricerca=request.form['ricerca']
    ricerca='Pensieri'
    print('ciao4')
    cont=cont+1
    c.execute(f'SELECT * FROM Libri WHERE Libri.titolo="{ricerca}"')
    ris = c.fetchall()
    c.close()
    conn.close()
    if cont>1:
      return jsonify(ris)
    else:
      return render_template('ricerca.html',results=ris)
  else :
    return render_template('ricerca.html',results=ris
    

  return render_template("ricerca.html")

'''


















if __name__ == "__main__":
  app.run()



