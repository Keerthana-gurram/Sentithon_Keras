import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "(from:#DigitalIndia) until:2022-12-03 since:2015-08-03"
tweets = []
limit = 10000


for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])
        
df = pd.DataFrame(tweets, columns=['Date', 'User', 'Tweet'])
print(df)

# to save to csv
df.to_csv('tweets.csv')
