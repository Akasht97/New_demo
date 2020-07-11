import tweepy

consumer_key = '***'
consumer_secret = '***'
access_token = '***'
access_token_secret = '***'

def Oauth():

    try:
        auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
        auth.set_access_token(access_token,access_token_secret)
        return auth

    except Exception as e:
        return none;

oath = Oauth()
api = tweepy.API(oath)

api.update_status('*')

print("tweet posted");
