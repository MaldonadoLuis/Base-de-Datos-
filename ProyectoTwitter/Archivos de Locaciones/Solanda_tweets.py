
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "8P0zDhmWgwgjDzgGDsmn5dIK8"
csecret = "dQeOe3TSPfL90qxCgqVezsdxAj7i3lZIW1m18OTesHVn1QNenU"
atoken = "735575569509781504-eYENHDdmTA4GhuC7wkNh4igvSRcGEVg"
asecret = "EGAOQhlS1GRauK6sM3ButrynMDIcolFtXqXNz5qfs5qMb"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print "SAVED" + str(doc) +"=>" + str(data)
        except:
            print "Already exists"
            pass
        return True
    
    def on_error(self, status):
        print status
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('solanda')
except:
    db = server['solanda']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-78.548856,-0.27662,-78.532226,-0.262405])  #MELBOURNE EAST