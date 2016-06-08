
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "ypYsm0ZWZe4OmmbtgTGb7Npwd"
csecret = "4g8x8ZrwIAhBmSDI4pIBnLhhk906byA8AvbjwpTPBlBoS8UD2g"
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
    db = server.create('sanbartolo')
except:
    db = server['sanbartolo']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-78.589006,-0.294214,-78.552826,-0.274252])  #MELBOURNE EAST