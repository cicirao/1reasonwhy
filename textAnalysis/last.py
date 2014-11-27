# Purpose:
# Author: 
import json
import os

data = []
path = 'last-week/'
alltweets = 0
rawtweets = 0
c = open('lastweek.txt', 'w+')

# Main Funtion: Go through all files in the directory
for file in os.listdir(path): 
  f = open(path + file, 'r')
  # Iterate in one file
  for line in f:
    # Just need lines with tweets info
    if len(line) > 200 and line.startswith('{\"id\":'):
      rawtweets += 1
      t = json.loads(line)
      # Drop not #1reasonwhy or #1reasontobe. To do this, check if either of the phrases is in the hashtags.
      hashtags = []
      for i in t['twitter_entities']['hashtags']:
        hashtags.append(i['text'].lower())
      if any('1reasonwhy' == s for s in hashtags):
        alltweets += 1
        # print 'Matched! The id is {id} '.format(id=t['id'])
        # getString(t) 
        if t['object']['objectType'] == 'note':
          text = t['object']['summary']
        elif t['object']['objectType'] == 'activity':
          text = t['object']['body']
        print text
        data.append(text)
        
      else:
        # print 'Not match hashtag'
        continue    
  # Write data to curation file after read each f file.
  # In case of overflow, clear data variable and close file each time after write.
  # data = []
  f.close()

print '\n'.join(data).encode('utf-8')
# curatedTweets.append(data)
c.write('\n'.join(data).encode('utf-8'))

# t = str(curatedTweets)
# print t 
# c = open('curation.json', 'w+')
# c.write(t + '\n')

print 'All ' + str(alltweets) + ' tweets'
print 'Raw ' + str(rawtweets) + ' tweets'
print 'Accuracy: ' + str(float(alltweets) / float(rawtweets))
c.close()