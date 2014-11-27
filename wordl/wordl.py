# Purpose: Parse tweet summary content from OneReasonWhy 6 week data curation files
# Author: 
import json
import os

data = []
#path = 'cleanData/'
alltweets = 0
rawtweets = 0
c = open('wordle.txt', 'w+')

# Main Function: Go through all files in the directory
#for file in os.listdir(path):
f = open('curation0.json', 'r')
# Iterate in one file
for line in f:
# Just need lines with tweets info
  rawtweets += 1
  t = json.loads(line)
    # Drop not #1reasonwhy or #1reasontobe. To do this, check if either of the phrases is in the hashtags.
#    hashtags = []
#    alltweets += 1
    # print 'Matched! The id is {id} '.format(id=t['id'])
    # getString(t)
  text = t['tweet']['text']
#  data.append(text)
  print text
  c.write(text.encode('utf-8'))
#  data = json.dumps(data)

# Write data to curation file after each f file
# In case of overflow, clear data variable and close file each time after write.
# data = []
f.close()

print data
#print '\n'.join(data).encode('utf-8')
# curatedTweets.append(data)
#c.write('\n'.join(data)).encode('utf-8')

# t = str(curateTweets)
# print t
# c = open('curation.json', 'w+')
#c.write(t + '\n')

#print 'All ' + str(alltweets) + ' tweets'
print 'Raw ' + str(rawtweets) + ' tweets'
#print 'Accuracy ' + str(float(alltweets) / float(rawtweets))
c.close()