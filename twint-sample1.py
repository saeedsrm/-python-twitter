import twint
import pandas 
import datetime
import csv
import os
"""t = twint.Config()
#t.Username = "xxx"
t.Search = '#ActuallyAutistic'
#t.Since = '2017-01-01'
t.Until = '2021-05-01'
#t.Limit = 20
#t.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet}"
t.Store_object = True



twint.run.Search(t)

#tlist = t.search_tweet_list

#print(tlist)"""

current_date = datetime.datetime(2017,7,1)
current_end_date = current_date + datetime.timedelta(days=1)
end_date = datetime.datetime(2021,12,10)
while (current_date != end_date):
    c = twint.Config()
    c.Debug = True
    c.Search = 'lang:en'
    #c.Lang = "en"
    #c.Pandas = True
    #c.Store_csv = True
    #c.Format = "ID {id} | Username {username}"
    c.Custom["tweet"] = ["id", "username", "date", "time", "hashtags", "tweet"]
    c.Output = 'ASDuser.csv'
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