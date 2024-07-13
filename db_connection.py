# db_connection.py
import pyodbc

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-J5I1AHU;'
        'DATABASE=twitterSentimiento;'
        'UID=sa;'
        'PWD=12345678'
    )
    return conn

def fetch_tweets():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT fecha, texto, sentimiento FROM TweetsSentiments")
    rows = cursor.fetchall()
    tweets = [{"fecha": row[0], "texto": row[1], "sentimiento": row[2]} for row in rows]
    conn.close()
    return tweets
