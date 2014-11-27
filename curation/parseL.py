# Purpose:
# Author: 
import json
import os

data = ''
path = 'decompressed/'
alltweets = 0
rawtweets = 0

def setHashtagStr(hashtags):
  hashtagStr = ""
  # Generate hashtag string

  for t in hashtags:
    hashtagStr += '{\"hash\":\"' + t + '\"}, '
  hashtagStr = hashtagStr[:-2]
  return hashtagStr
  #"hashtags": [ "hash": "somestring", "hash": "somestring" ]
  
def setUserMentionStr(usermentions):
  mentionsStr = ""
  mentions = {}
  # Generate usermentions string
  for i in usermentions:
    mentions.update({i['screen_name']: i['id_str']})
  for key in mentions:
    mentionsStr += '{\"handle\":\"' + key + '\", \"id\" : \"' + mentions[key] + '\"}, '
  mentionsStr = mentionsStr[:-2]
  return mentionsStr
  #"userMentions": [{"user": "someString", "id": "someString"}, {"user": "someString","id": "someString"}]

def fetchData(tweet, hashtags, outputFile):
  # Fetch data and store in variables
  handle = tweet['actor']['preferredUsername']
  authorId = tweet['actor']['id']
  # hashtags = tweet['twitter_entities']['hashtags']
  hashtagStr = setHashtagStr(hashtags)
  # We will generate this later
  objectType = tweet['object']['objectType']
  tweetId = tweet['object']['id']
  # text = tweet['body']
  # summary = tweet['body'] 
  # I changed the tweet['object']['summary'] to this, because the object may not have a summary attibute.
  # So is the postTime. You can validate this by checking the last tweet in file 20121125-20130101_7xfsda5298_2012_11_27_20_30_activities.json
  postTime = tweet['postedTime']
  #? favCount = 0  No this attribute in raw data.
  rtCount = tweet['retweetCount']
  usermentions = tweet['twitter_entities']['user_mentions']
  mentionsStr = setUserMentionStr(usermentions)


  # We generate usermentions string later

  if tweet['object']['objectType'] == 'note':
    text = tweet['object']['summary']
    originId = tweetId
  elif tweet['object']['objectType'] == 'activity':
    text = tweet['object']['body']
    originId = tweet['object']['object']['id']
  
  text = json.dumps(text) # escape stuff JSON doesn't like
   
  # Create a schema that suits our data to store
  # data = '\"author\": {' + '\"handle\": {handle}, \"id\": {authorId} ' + '}, \"twitterEntity\": {\"hashtag\": [' + {hashtagStr} + '] },\"tweet\": {\"objectType\": {objectType},\"id\": {tweetId},\"text\": {text},\"summary\": {summary},\"postTime\": {postTime},\"rtCount\":  {rtCount},\"userMentions\": [' + {mentionsStr} + ']}'.format(handle=handle, authorId=authorId, hashtag=hashtagStr, objectType=objectType, tweetId=tweetId, text=text, summary=summary, postTime=postTime, rtCount=rtCount, userMentions=mentionsStr)
  data = '{\"author\": {\"handle\": \"' + handle + '\",\"id\": \"' + authorId + '\"},\"twitterEntity\": {\"hashtag\": [' + hashtagStr + ']},\"tweet\": {\"objectType\": \"' + objectType + '\",\"id\": \"' + tweetId + '\",\"text\": ' + text + ',\"originId\":\"' + originId + '\",\"postTime\":\"' + str(postTime) + '\",\"rtCount\":' + str(rtCount) + ',\"userMentions\": [' + mentionsStr + ']}}'

  print data
  print '\n'
  # curatedTweets.append(data)
  # return curatedTweets

  outputFile.write(data.encode("utf-8") + '\n')
    
def main():
  rawtweets = 0
  alltweets = 0
  # Main Funtion: Go through all files in the directory
  outputFile = open('curation0.json', 'w+')
  
  for file in os.listdir(path): 
    f = open(path + file, 'r')
    
    # Iterate in one file
    for line in f:
      # Just need lines with tweets info
      if line.startswith('{\"id\":'):
        rawtweets += 1
        t = json.loads(line)
        # Drop not #1reasonwhy or #1reasontobe. To do this, check if either of the phrases is in the hashtags.
        hashtags = []
        for i in t['twitter_entities']['hashtags']:
          hashtags.append(i['text'].lower())
        if any('1reasonwhy' == s for s in hashtags):
          alltweets += 1
          # print 'Matched! The id is {id} '.format(id=t['id'])
          # 1000 tweets in one file

          fetchData(t, hashtags, outputFile)  
        else:
          print 'Not match hashtag'
          continue 
      else:
        print line   
    # Write data to curation file after read each f file.
    # In case of overflow, clear data variable and close file each time after write.
    # data = []
    f.close()

  # t = str(curatedTweets)
  # print t 
  # c = open('curation.json', 'w+')
  # c.write(t + '\n')

  outputFile.close()
  print 'All ' + str(alltweets) + ' tweets'
  print 'Raw ' + str(rawtweets) + ' tweets'
  print 'Accuracy: ' + str(float(alltweets) / float(rawtweets))

  # end main function

# Call the main function
if __name__ == '__main__' :
    main()
