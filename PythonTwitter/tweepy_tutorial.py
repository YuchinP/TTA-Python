from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'pOCoOGUHGsQ9PJVqwiJvIybYI'
csecret = 'DpMrcgEKZvfroNOb8mkE23VJOy0VhVShohjuoxEoc9c1Jl7itX'
atoken = '2153953951-ahtMwYIdkquqf3SeJrI3bpMJhgSl2S1z4OTZqNz'
asecret = 'obOLOIyrOtlLAdkaCJryPQKUOv8EX3WR43ummaEesRUuS'


class listener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
