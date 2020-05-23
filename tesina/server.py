from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app = Flask(__name__)

@app.route("/")

    return render_template("index.html")

@app.route("/allbooks",methods=['GET', 'POST')
def visualizzaTutto()
    name=#read from db sqlite
    render_template("visualizza.html",nomeLibro=name,autore=autore,annoPubblicazione=anno)

if __name__ == "__main__":
    app.run()