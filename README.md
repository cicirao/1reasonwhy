\#1ReasonWhy
==========

Analysis of three-month #1reasonwhy Tweets

* This repository only include all Python codes, not any data.
* The raw data comes from [GNIP](http://gnip.com/) Twitter data.

'1ReasonWhy' is a Twitter hashtag created by people who care about the unfair treatment to women in the game industry. According to our current research, people’s focus has been expanded to not only women in the game industry but also all women gamers. This project is aiming at analyzing three-month tweets with #1ReasonWhy in order to understand the humanities knowledge behind.    
(see initial propose [here](https://medium.com/research-methods-in-digital-humanities/project-1reasonwhy-17022abf3bd9))

##Curation
The Curation code parsed the raw data from GNIP and output the clean data with new schema. The output is one json file of all data with one tweet object per line. Each further research was based on the clean data.    
GNIP has a huge [documentation](http://support.gnip.com/sources/twitter/data_format.html), sometimes it causes confusion.    

##Tweets-Authors
This piece goes through all clean data and generates 25 top retweeted tweets as well as their authors.    
The outputs are two json files.   
25 top tweets: include top 25 tweets objects.
Authors: include a list of author objects who created the top 25 retweeted tweets.    
See more about this part [here](https://medium.com/@CiciRaoXi/1reasonwhy-authority-f1ce39ac6ec).

This is our clean data(in JSON):

<pre><code>
{
  "tweet": {
    "rtCount": 864,
    "postTime": "2012-12-19T14:17:10.000Z",
    "text": "For a look into why women are still underrepresented in game design, check out the #1reasonwhy hashtag. The sexism of tech industry exposed.",
    "id": "tag:search.twitter.com,2005:281402802222284801",
    "userMentions": [
      {
        "handle": "labcoatman",
        "id": "16915437"
      }
    ],
    "originId": "object:search.twitter.com,2005:273225382998712320",
    "objectType": "activity"
  },
  "twitterEntity": {
    "hashtag": [
      {
        "hash": "1reasonwhy"
      }
    ]
  },
  "author": {
    "handle": "GamerFems",
    "id": "id:twitter.com:997296812"
  }
}
</code></pre>

####Data Format    
<table>
    <tr>
        <td><code>rtCount</code></td>
        <td>The retweeted number of this tweet. Int. </td>
    </tr>
    <tr>
        <td><code>postTime</code></td>
        <td>The datetime that this tweet was posted. String.</td>
    </tr>
    <tr>
        <td><code>text</code></td>
        <td>The retweeted number of this tweet. String.</td>
    </tr>
    <tr>
        <td><code>id</code></td>
        <td>The id of this tweet. String.</td>
    </tr>
    <tr>
        <td><code>userMentions</code></td>
        <td>Any '@' or 'RT' users in this tweet. A list of objects; each object includes a handle and an id of a person. </td>
    </tr>
    <tr>
        <td><code>originId</code></td>
        <td>If this tweet is a retweet, then the originId is the one that has been retweeted; If this tweet is not a retweet, then the originId is the same with id. </td>
    </tr>
    <tr>
        <td><code>objectType</code></td>
        <td>objectType can be either note or activity. note represents an original tweet; activity represents a retweet. String. </td>
    </tr>
    <tr>
        <td><code>hashtag</code></td>
        <td>All hashtags that has been mentioned in this tweet. A list of object; each object includes a value of hashtag. </td>
    </tr>
    <tr>
        <td><code>author</code></td>
        <td>The author of this tweet. An object with two properties: handle and id. </td>
    </tr>    

