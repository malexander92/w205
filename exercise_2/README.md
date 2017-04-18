Exercise 2

Description:

This application was created for my w205 exercise 2 project to stream tweets from twitter's api and count the occurences of all the words contained in them.  The first part of the application consists of a storm topology with a spout that streams tweets from twitter’s API, a first bolt that parses words from the tweets, and then a second bolt that records the word counts in a postgres data base.  The second part includes python scripts for querying the results from the database once it is populated.  More in-depth documentation can be found in the accompanying Architecture.pdf file.

Execution Instructions:

1) Be sure you have both python packages psychopg2.6.2 and Tweepy installed and postgres running on your system before executing
2) Run setup_and_launch.sh to create the postgres database and launch the topology
3) Once the topology has launched and has run for a few minutes ingesting tweets hit Ctrl-C to stop it
4) We now have a populated database we can extract results from using the python scripts finalresults.py and histogram.py
5) Use command "python finalresults.py word" to find the count for a given word
6) Use command "python histogram.py min max" to find all words within the given count range
