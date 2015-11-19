
import tweepy
import sentiment

CONSUMER_KEY = 'ncMZ2CP7YmScHkLYwmfCYaTZz'
CONSUMER_SECRET = 'ZkFEJXxXEOUlqkhrJ14kzWakrXjqIe11de7ks28DyC79P31t9q'
ACCESS_KEY = '1157786504-XB3DXGrMmhvM1PAb6aeys3LJFYI9Y3LzS6veRHj'
ACCESS_SECRET = '8w69uDRm9PPA9iv3fNtkHPKP4FIq5SFtVbcE28wtcY5qx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def get_by_hashtag(hashtag):
    print hashtag
    tweets = api.search(hashtag, count=5)
    tweets = [tweet.text for tweet in tweets]
    scores = sentiment.sentiment_scores_of_tweets(tweets)
    print scores
    res = {}
    if tweets:
        res['status'] = 0
        res['items'] = tweets
        res['scores'] = scores
    return res
    pass

if __name__ == '__main__':
    get_by_hashtag(hashtag)