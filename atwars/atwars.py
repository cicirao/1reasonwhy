# Purpose: At Wars, to find the number of user mentions in tweets
# Author: Mike
import json
import os

mentionCount = 0
path = 'test/'
alltweets = 0
rawtweets = 0



#checks tweet and sees if there is a user mentioned
def yesMention(tweet):
  t = json.loads(tweet)
  if t['tweet']['userMentions']:
    return True

def main():
  f = open(path + 'curation0.json', 'r')
  atCount = 0
  totalCount = 0
  for line in f:
    if yesMention(line):
      atCount += 1
      totalCount += 1
    else:
      totalCount += 1
  f.close()
  print "%s users mentioned" % (atCount)
  print "%s total tweets" % (totalCount)
  return atCount




# Call the main function
if __name__ == '__main__' :
    main()

