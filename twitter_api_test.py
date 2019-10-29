# test script to see if your app has credentials to get twitter data
import twitter
import os

# your twitter app credentials
CONSUMER_KEY = <Your Consumer Key>
CONSUMER_SECRET = <Your Consumer Secret>
ACCESS_TOKEN = <Your Access Token>
ACCESS_SECRET = <Your Access Secret>

# create twitter api object with your credentials
twitter_api = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                access_token_key=ACCESS_TOKEN,
                access_token_secret=ACCESS_SECRET)

# test authentication
print(twitter_api.VerifyCredentials())

# function that takes in a keyword and retrieves 50 tweets with the keyword
def buildTestSet(search_keyword):
    try:
        tweets_fetched = twitter_api.GetSearch(search_keyword, count = 50)
        
        print("Fetched " + str(len(tweets_fetched)) + " tweets for the term " + search_keyword)
        
        return [{"text":status.text, "label":None} for status in tweets_fetched]
    except:
        print("Unfortunately, something went wrong..")
        return None

# driver code
search_term = input("Enter a search keyword:")
testDataSet = buildTestSet(search_term)

# print the first 5 tweets with the inputed keyword
print(testDataSet[0:4])