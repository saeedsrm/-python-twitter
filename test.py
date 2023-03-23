import twint
import pandas as pd

# Configure
usernames = ["elonmusk", "BarackObama", "CathieDWood"]
dataframes = []


# def extractByDate(date , lastDate):
def extractByDate():
    date='2023-01-01'
    for username in usernames:
        config = twint.Config()
        config.Since = date

        config.Until = '2023-03-01'
        config.Pandas = True
        config.Store_csv = True
        config.Lang = 'en'
        config.To = username
        # config.Username = username
        # Run
        twint.run.Search(config)

        df = twint.storage.panda.Tweets_df

        # Add the DataFrame to the list
        dataframes.append(df)

    # Concatenate the DataFrames for each account into a single DataFrame
    all_tweets_df = pd.concat(dataframes, ignore_index=True)

    # Export the combined DataFrame to a CSV file
    all_tweets_df.to_csv("all_replies_tweets1.csv", index=False)


# Configure
usernames = ["elonmusk", "BarackObama","cathiedwood"]
dataframes = []

for i in range(26, 31, 2):
    for username in usernames:
        config = twint.Config()
        # config.Limit = 10
        config.Since = '2023-02-'+str(i)
        config.Until= '2023-02-'+str(i+1)
        # config.Popular_tweets = True
        config.Pandas = True
        config.Store_csv = True
        config.Lang = 'en'
        # config.Output = "replies.csv"
        config.To = username
        # config.Username = username
        # Run
        twint.run.Search(config)

        df = twint.storage.panda.Tweets_df
        print(df)
        # Read the tweets from the CSV file into a DataFrame
        # df = pd.read_csv(f"{username}_tweets.csv", header=None, names=["id", "conversation_id", "created_at", "date", "timezone", "user_id", "username", "name", "place", "tweet", "mentions", "urls", "photos", "replies_count", "retweets_count", "likes_count", "hashtags", "cashtags", "link", "retweet", "quote_url", "video", "thumbnail", "near", "geo", "source", "user_rt_id", "user_rt", "retweet_id", "reply_to", "retweet_date"])

        # Add the DataFrame to the list
        dataframes.append(df)

    # Concatenate the DataFrames for each account into a single DataFrame
    all_tweets_df = pd.concat(dataframes, ignore_index=True)

    # Export the combined DataFrame to a CSV file
    all_tweets_df.to_csv("all_replies_tweets_Feb"+str(i)+".csv", index=False)