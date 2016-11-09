from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import urllib
import urllib.request
from urllib.parse import quote

ckey = 'pOCoOGUHGsQ9PJVqwiJvIybYI'
csecret = 'DpMrcgEKZvfroNOb8mkE23VJOy0VhVShohjuoxEoc9c1Jl7itX'
atoken = '2153953951-ahtMwYIdkquqf3SeJrI3bpMJhgSl2S1z4OTZqNz'
asecret = 'obOLOIyrOtlLAdkaCJryPQKUOv8EX3WR43ummaEesRUuS'

######
sentdexAuth = ''





#This is the function
def sentimentAnalysis(text):
    encoded_text = urllib.parse.quote(text)
    API_Call = "http://sentdex.com/api/api.php?text="+encoded_text+'&auth='+sentdexAuth
    #These two lines are specific to sentdex if we
    #x = len(text)

    output = urllib.request.urlopen(API_Call).read()
    return output.decode('utf-8')
##    for output in urllib.request.AbstractBasicAuthHandler(API_Call).read():
##        return output.decode('utf-8')
class listener(StreamListener):

    def on_data(self, data):
        tweet = data.split(',"text":"')[1].split('","source')[0] #can be substituted for a JSON module
        sentimentRating = sentimentAnalysis(tweet)
        saveMe = tweet+'::'+sentimentRating+'\n'
        output = open('outputLoL.csv','a')
        output.write(saveMe)
        output.close()
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["elementalist lux"])
