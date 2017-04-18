Exercise 2

Execution Instructions:

1) Be sure you have both python packages psychopg2.6.2 and Tweepy installed and postgres running on your system before executing
2) Run setup_and_launch.sh to create the postgres database and launch the topology
3) Once the topology has launched and has run for a few minutes ingesting tweets hit Ctrl-C to stop it
4) We now have a populated database we can extract results from using the python scripts finalresults.py and histogram.py
5) Use command "python finalresults.py word" to find the count for a given word
6) Use command "python histogram.py min max" to find all words within the given count range
