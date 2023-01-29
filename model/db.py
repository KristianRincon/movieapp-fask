from flask_mysqldb import MySQL
from application import app
from MySQLdb.cursors import Cursor

# Establecemos la coneccion a la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'coltis_movie_flask'
app.config['MYSQL_PORT'] = 3308
mysql = MySQL(app)

def execute(sql: str) -> Cursor:
    cursor = mysql.connection.cursor()
    cursor.execute(sql)
    return cursor

def commit() -> None:
    mysql.connection.commit()