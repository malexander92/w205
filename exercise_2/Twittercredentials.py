import tweepy

consumer_key = "jX1x7VBctOz5voSdPZprmgoSd";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "RBKp2OGD8NntAeN93ftVfpmv0G1KRII90fiPEdL79K5OCDq87Q";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "2827600059-SV4GzXzSMQmbiCrsLdigWbRjKPgsFDuRP9BY6Or";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "fQmZEYs7qNsyzUhQuYRIyNB55M76CePxFPW2xQyCqZvNr";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



