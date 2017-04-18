import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

#Connect and Create the Database
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

try:
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute("CREATE DATABASE tcount")
    cur.close()
    conn.close()
except:
    print "Could not create database"

#Connect to the new DB and Create the Table
conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

cur = conn.cursor()
cur.execute('''CREATE TABLE tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()