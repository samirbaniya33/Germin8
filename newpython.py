import sys
import tweepy

def twitter_auth():
    consumer_key="jFblJSUeQzxB31mAscQc0fSLF"
    consumer_secret_key="bM4h1BfCUG4jAyZxQxZDNFskQO8RxY91sfuvYrFEUJ0fxKcubo"
    access_token="363665587-uVBket9Ah9HZCSECVrgYeuDwoVqk8nff11rzLaCD"
    access_secret_token="E00i3GjbniuJMBYAGjiA7kWBuy3O2gZeD5CWNCblC3SA5"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_secret_token)
    return auth

def get_twitter_client():
    auth=twitter_auth()
    client=tweepy.API(auth)
    return client


if __name__ =='main':
    user=input("Enter username: ")
    client = get_twitter_client()
    for status in tweepy.Cursor(client.home_timeline, screen_name=user).items(100):
        print(status.id)
        print(status.likes_count)
        print(status.retweet_count)