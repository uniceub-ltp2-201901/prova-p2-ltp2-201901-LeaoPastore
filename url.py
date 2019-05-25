#Gabriel Leão Pastore
#RA: 21805090

from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL
from db import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)
config(app)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/numero', methods=['GET', 'POST'])
def numero():
    if request.method == 'POST':

        url = request.form.get('url')
        idurl = get_numeros()

        conn = mysql.connect()
        cursor = conn.cursor()


        inurl(cursor, conn, idurl, url)

        cursor.close()
        conn.close()

        url = str(idurl)
        return render_template('gerada.html', url=url)

    else:
        principal()

@app.route('/gerada')
def gerada():
    return render_template('gerada.html')

@app.route('/<url>')
def redire(url):
    conn, cursor = get_db(mysql)

    redi = site(cursor, url)

    cursor.close()
    conn.close()
    if redi is None:
        return render_template('index.html', erro='URL Incorreta! Tente uma url válida.')
    else:
        red = str(redi[0])
        return redirect(red)

@app.route('/ranking')
def ranking():
    conn = mysql.connect()
    cursor = conn.cursor()

    ordem = contador(cursor)

    cursor.close()
    conn.close()

    return render_template('relatorio.html', rank=ordem)


if __name__ == '__main__':
    app.run(debug=True)
