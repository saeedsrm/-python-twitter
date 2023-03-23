# !git clone --depth=1 https://github.com/twintproject/twint.git
# !cd /content/twint && pip3 install . -r requirements.txt
# !pip3 install -qq twint
# !pip install -qq whatthelang
import twint
import pandas 
import datetime
import csv
import os


current_date = datetime.datetime(2020,7,1)
current_end_date = current_date + datetime.timedelta(days=1)
end_date = datetime.datetime(2021,12,10)
while (current_date != end_date):
    c = twint.Config()
    c.Debug = True
    c.Search = 'lang:en sinopharm'
    #c.Lang = "en"
    #c.Pandas = True
    #c.Store_csv = True
    #c.Format = "ID {id} | Username {username}"
    c.Custom["tweet"] = ["id", "username", "date", "time", "hashtags", "tweet"]
    c.Output = 'reaction5.csv'
    #c.Custom = ['id', 'created_at', 'user_id', 'username', 'tweet', 'hashtags']
    c.Store_csv = True
    #c.Output = os.path.join(tw_path, csv_name)
    c.Since = current_date.strftime("%Y-%m-%d")
    c.Until = current_end_date.strftime("%Y-%m-%d")
    c.debug = True
    twint.run.Search(c)
    #df = twint.storage.panda.Tweets_df
    #print(df)
    #df.info()
    #df.sample(5)
    current_date = current_end_date
    current_end_date += datetime.timedelta(days=1)
    print(current_date != end_date)


import tweepy as tw
import pandas as pd
# your Twitter API key and API secret
my_api_key = "MINE"
my_api_secret = "MINE"
# authenticate
auth = tw.OAuthHandler(my_api_key, my_api_secret)
api = tw.API(auth, wait_on_rate_limit=True)

search_query = "#blm OR blm -filter:retweets"

# get tweets from the API
tweets = tw.Cursor(api.search,
              q=search_query,
              lang="en",
              since="2020-05-24",
              until="2020-12-01",
              exclude_replies=False,
                   tweet_mode='extended').items()


# store the API responses in a list
tweets_copy = []
for tweet in tweets:
    tweets_copy.append(tweet)
    
print("Total Tweets fetched:", len(tweets_copy))