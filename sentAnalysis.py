from textblob import TextBlob                                                   
from pageScraper import *                                                       

def newsAnalysis(dataDiX):                                                     
    sent = []                                                                   
    sentVal = []
    for news in list(dataDiX.values()):
      analysis = TextBlob(news)
      sentiment = find_Sentiment(analysis.sentiment.polarity)
      qq = analysis.sentiment.polarity
      sentVal.append(qq)
      sent.append(sentiment)
    return sent, sentVal

def find_Sentiment(val):                                                                                                               
    if val<=0.0 and val>-0.0:
        return 'Neutral'
    elif val>0.0:
        return 'Positive'
    else:
        return 'Negative'

def listMaker(newsPaper, titles, sent, sentVal, lists):
  totalSent = 0
  for i in range(len(newsPaper)):
    sas = sent[i]+ ' : ' + str(sentVal[i])
    totalSent+=sentVal[i]
    lists.append(sas)
    lists= [x.replace('\n', '') for x in lists]
  return lists, totalSent
         
def sentimentAnalysis(newsPaper, titles, links):
  lists = []
  stories = newsStoryGrabber(links)
  newsPaper=dict(zip(titles,stories))
  sent, sentVal = newsAnalysis(newsPaper)
  lists, totalSent = listMaker(newsPaper, titles, sent, sentVal, lists)
  return lists

def avgSentiment(newsPaper, titles, links):
  lists = []
  stories = newsStoryGrabber(links)
  newsPaper=dict(zip(titles,stories))
  sent, sentVal = newsAnalysis(newsPaper)
  lists, totalSent = listMaker(newsPaper, titles, sent, sentVal, lists)

  avgSent = totalSent/len(titles)
  return avgSent


