# test script to see if your app has credentials to get twitter data
import tweepy

# your twitter app credentials
CONSUMER_KEY = <YOUR CONSUMER KEY>
CONSUMER_SECRET = <YOUR CONSUMER SECRET>
ACCESS_TOKEN = <YOUR ACCESS TOKEN>
ACCESS_SECRET = <YOUR ACCESS SECRET>

# create twitter api object with your credentials using tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# test to verify your credentials, should return a user object with all your account information
verify = api.verify_credentials()
print(verify)