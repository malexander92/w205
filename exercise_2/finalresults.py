import psycopg2

def finalresults(word):
	word = word.lower()

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

	print "Total number of occurrences of " + word + ": " + str(uCount)