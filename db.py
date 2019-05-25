def config(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'url'

def get_db(mysql):
    conn = mysql.connect()
    cursor = conn.cursor()

    return conn, cursor

import random
def get_numeros():
    for x in range(1):
        y = random.randint(10000, 99999)
        return y

def inurl(cursor, conn, idurl, url ):
    cursor.execute(f'insert into urls (idurls, url) values("{idurl}", "{url}")')
    conn.commit()

def site(cursor, url):
    cursor.execute(f'SELECT url FROM urls WHERE idurls = {url}')
    site = cursor.fetchone()
    return site

def contador(cursor):
    cursor.execute(f'SELECT idurls, soma FROM urls order by soma desc')
    ordenar = cursor.fetchall()
    return ordenar


