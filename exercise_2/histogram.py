import psycopg2
import sys

def histogram(k1, k2):

	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT word, count FROM tweetwordcount \
		WHERE count >= %s AND count <= %s ORDER BY count DESC;", (k1, k2))

	results = cur.fetchall()

	conn.commit()
	conn.close()

	for rec in results:
		print rec

# Setting default values
if len(sys.argv) == 1:
	k1_sys = 5
	k2_sys = 15
else if len(sys.argv) == 2:
	k1_sys = sys.argv[1]
	k2_sys = 15
else:
	k1_sys = sys.argv[1]
	k2_sys = sys.argv[2]

histogram(k1_sys, k2_sys)