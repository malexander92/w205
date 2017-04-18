import psycopg2
import sys
import matplotlib.pyplot as plt

def plot_top():

	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT word, count FROM tweetwordcount ORDER BY count DESC LIMIT 20;")

	results = cur.fetchall()

	conn.commit()
	conn.close()

	words = results[:][0]
	counts = results[:][1]

	plt.bar(words, counts, align='center', alpha=0.5)
	plt.xticks(words, words)
	plt.ylabel('Count')
	plt.title('Tweet Word Counts')
	savefig('Plot.png', bbox_inches='tight')

plot_top()