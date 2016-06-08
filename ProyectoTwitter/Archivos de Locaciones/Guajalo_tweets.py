
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "aHmGvTR6AzNeoXo5RN9UGoShq"
csecret = "tyVumwHS6ShYkWNOX7SFTDAVLVXWOAptdv8QzPaTivVIU02S1Z"
atoken = "600356069-YWtbeIFn5S4PgRcq7BfKy5VC1no6KvXqQGojX5q0"
asecret = "zvYNiNZ3RHX16S60T2uAlNbTCiWF2OIAOTvUqxP9WiNhk"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('guajalo')
except:
    db = server['guajalo']
    
'''===============LOCATIONS=============='''    

twitterStream.filter(locations=[-78.538492,-0.290943,-78.504996,-0.263456])  #MELBOURNE EAST