import psycopg2
import sys
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

def plot_top():

	conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
	cur = conn.cursor()
	cur.execute("SELECT word, count FROM tweetwordcount ORDER BY count DESC LIMIT 20;")

	results = cur.fetchall()

	conn.commit()
	conn.close()

	words = [x[0] for x in results]
	counts = [x[1] for x in results]
	y_pos = np.arrange(len(words))

	plt.bar(y_pos, counts, align='center', color=blue, alpha=0.5)
	plt.xticks(y_pos, words)
	plt.ylabel('Count')
	plt.xlabel('Top 20 Words')
	plt.title('Tweet Word Counts')
	savefig('Plot.png', bbox_inches='tight')

plot_top()