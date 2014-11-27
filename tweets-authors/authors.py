# Purpose: Find the authors of top 25 retweeted tweets. 
#          The outputs are top 25 tweets and a list of their authors
# Author: Xi Rao & Bing Xue
import json
import os

path = 'Curation/'

def compareTweets(tweet, topTweets): # tweet structure: (rtCount, originId, tweetObject)

  if tweet[0] > topTweets[0][0]:  # Compare new rtCount with first one in list

    if tweet[1] in [x[1] for x in topTweets]: # check if the id already exist in the list
      sameId = tweet[1]
      sameTweets = [t for t in topTweets if t[1] == sameId] # list of same id tweets

      if tweet[0] > min(sameTweets[0]): # check if new rtCount larger than min in the list of same id
        sameId = tweet[1]    # replace the last
        minIndex = ([t[1] for t in topTweets].index(sameId)) # get the index of the min
        topTweets[minIndex] = tweet    # replace min 
        topTweets = sorted(topTweets, key=lambda t:t[0])   # sort top list
      # else: # not larger, drop it

    else: # new id, 
      topTweets[0] = tweet  # replace the first, since the list is ordered by rtCount
      topTweets = sorted(topTweets, key=lambda t:t[0]) # sort top list

  # else: # if new tweet rtCount is not larger than the min in the list, drop it
  # for t in topTweets:  # test in terminal
  #   print t[0]

  return topTweets
  # End compareTweet funtion


def findTopTweets(tweets):
  topTweets = []

  for tweet in tweets[:25]:    # set first 25 tweets as the original value of topTweets list
    tweet = (tweet['tweet']['rtCount'], tweet['tweet']['originId'], tweet)  # OMG tuple data structure is so fancy!
    topTweets.append(tweet)
  # print topTweets
  topTweets = sorted(topTweets, key=lambda t:t[0])  # Sort the topTweets by rtCount, the first is the least 
 
  parsedTweet = 0
  for tweet in tweets: # Go throught the whole list 
    parsedTweet += 1 # Just count for sure
    tweet = (tweet['tweet']['rtCount'], tweet['tweet']['originId'], tweet) # create tuple list
    # print tweet
    topTweets = compareTweets(tweet, topTweets)  # compare with top list  
  # End the loop

  # print topTweets
  topTweets = [x[2] for x in topTweets]
  t = json.dumps(topTweets)

  topTweetsFile = open('topTweetsFile.json', 'w+')  # write to topTweetsFile.json
  topTweetsFile.write(t)
  topTweetsFile.close()

  print 'parsed tweets:' + str(parsedTweet)
  return topTweets
  # End findTopTweets function


def findAuthors(tweets):
  topTweets = findTopTweets(tweets) # To get authors, first get the tweets
  authors = [x['author'] for x in topTweets] # get authors
  print len(authors)
  authors = [dict(a) for a in set([tuple(d.items()) for d in authors])] # remove duplicates
  print 'Unique authors: ' + str(len(authors)) # check if removed
  # print authors
  
  a = json.dumps(authors)
  authorsFile = open('authorsFile.json', 'w+')
  authorsFile.write(a)  # write authors to authorFile.json
  authorsFile.close()

  # End findAuthors funtion


def main():
  data = []
  with open(path + 'curation0.json') as f:
    for line in f:
      data.append(json.loads(line))

  findAuthors(data) # call find authors funtion
  f.close()
  # End main funtion  


# Call main function
if __name__ == '__main__' :
  main()