import psycopg2
import sys

def histogram(k1, k2):

	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT word, count FROM tweetwordcount ORDER BY count DESC \
		WHERE count >= %s AND count <= %s;", (k1, k2))

	results = cur.fetchall()

	conn.commit()
	conn.close()

	for rec in results:
		print rec

# Setting default values
k1_sys = sys.argv[1] or 5
k2_sys = sys.argv[2] or 15

histogram(k1_sys, k2_sys)