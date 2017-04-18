from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt
import psycopg2


class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()

    def process(self, tup):
        word = tup.values[0]
        uWord = str(word).lower()

        # Write codes to increment the word count in Postgres
        # Use psycopg to interact with Postgres
        # Database name: Tcount 
        # Table name: Tweetwordcount 
        # you need to create both the database and the table in advance.
        
        # First open a connection to the database
        conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

        # If the word is already in the list, update the count, otherwise insert a new record
        
        cur = conn.cursor()
        cur.execute("SELECT count FROM tweetwordcount WHERE word=%s;", (uWord, ))

        if cur.rowcount == 0:
            cur = conn.cursor()
            cur.execute("INSERT INTO tweetwordcount (word,count) VALUES (%s, %s);", (uWord, 1))
            conn.commit()
        else:
            uCount = cur.fetchall()[0]
            uCount = uCount[0] + 1
            conn.commit()

            cur = conn.cursor()
            cur.execute("UPDATE tweetwordcount SET count=%s WHERE word=%s;", (uCount, uWord))
            conn.commit()

        conn.close()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
