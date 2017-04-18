import psycopg2
import sys

def finalresults():

# Query to pull all words when none is specified
	if len(sys.argv) == 1:
		conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
		cur = conn.cursor()
		cur.execute("SELECT word, count FROM tweetwordcount ORDER BY word ASC;")

		results = cur.fetchall()

		conn.commit()
		conn.close()

		for rec in results:
			print rec

# Query to pull specific word count when one is specified
	else:
		word = sys.argv[1].lower()

		conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
		cur = conn.cursor()
		cur.execute("SELECT count FROM tweetwordcount WHERE word=%s;", (word, ))

		if cur.rowcount == 0:
			uCount = 0
		else:
			uCount = cur.fetchall()[0]
			uCount = uCount[0]

		conn.commit()
		conn.close()

		print "Total number of occurrences of \"" + word + "\": " + str(uCount)

finalresults()