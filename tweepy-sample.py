# imports

import tweepy
import configparser
import pandas as pd

from datetime import date


def Verifing_credential():
    """
    Reading credential from config file
    """
    config = configparser.ConfigParser()
    #config.read(r'/home/legion/PycharmProjects/twitter/config.ini')
    config.read(r'/content/drive/MyDrive/config.ini')
    

    api_key = config['twitter']['api_key']
    api_key_secret = config['twitter']['api_key_secret']

    access_token = config['twitter']['access_token']

    access_token_secret = config['twitter']['access_token_secret']

    """
    authentication
    and instance creation of the API
    """

    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    return api


def scrape(api, search_query=[], count=50, item=10):
    """

        :param search_query: keyword to search for
        :param api: api instant
        :param count: number of tweets to collect
        :param item: it is user for pagination
        :return: tweets based on a keyword
        """
    for word in search_query:
        tweets = tweepy.Cursor(api.search,
                               q=word,
                               lang="en",
                               since=f"{startDate}",
                               until=f"{endDate}"
                               ).items(item)
        #tweets = api.search(q=word, tweet_mode="extended", lang="en", count=count) 
    #print("Total:", len(tweets))                    
    print("salaam")
    return tweets


def filtering_tweets(tweets, final_filtered_tweets=[]):
    """
    :param tweets: the cursor results
    :return: a list containing tweets for a specific date
    """
    # some of these attributes are commented
    # uncomment them if you need to fetch these features for each user
    for tweet in tweets:
        print("0")
        print(tweet.text)
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        # following = tweet.user.friends_count
        # followers = tweet.user.followers_count
        # totaltweets = tweet.user.statuses_count
        # retweetcount = tweet.user.retweet_count
        # hashtags = tweet.entities['hashtags']
        created_at = tweet.created_at
        extracted_date = created_at.date()
        #if extracted_date < endDate and extracted_date > startDate:
        final_filtered_tweets.append(
             {"username": username, "description": description, "location": location, 'created_at': extracted_date})
    return final_filtered_tweets


def dataframe_creation(final_filtered_tweets=[]):
    df = pd.DataFrame(final_filtered_tweets)
    csv = df.to_csv('tweets')
    return csv


if _name_ == "__main__":
    api = Verifing_credential()
    """
    defining dates for data collection
    by default this variable is set to be equal to the begining of pandecmic untill a year after 
    in order to collect tweets for just a year
    """
    startDate = date(2020, 1, 10)
    endDate = date(2022, 9, 17)

    """
    define a list of keywords
    this list has to be completed
    """
    final_filtered_tweets = []
    search_query = ["game"]
    tweets = scrape(api, search_query)
    for tweet in tweets:
      print(tweet.text)
      print(tweet.created_at)
      print(tweet.user.created_at)
    final_filtered_tweets = filtering_tweets(tweets, final_filtered_tweets)
    dataframe_creation(final_filtered_tweets)

