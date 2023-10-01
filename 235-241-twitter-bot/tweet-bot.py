import tweepy

auth = tweepy.OAuthHandler('uAqc1SNgYFkoM1IColX2j2Pi2', 'IyatfoEakdKncJQSOQxeiWj8SOb3lcdgRmDqDxFC0nA3zL1uVY')
auth.set_access_token('1212878194891608064-FWmioaECfuGutPdwZx14Xqol9MfLVG', 'N6GMCPbj2iop3ZnAh47PfOBX2kCXI4RN1MXxqA1f76uu9')

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)