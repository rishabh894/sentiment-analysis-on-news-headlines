from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from textblob import TextBlob
from pageScraper import *
from sentAnalysis import *

app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/nationalnews',methods=['GET'])
@cross_origin()
def nationalnews():
    url = 'https://www.thehindu.com/news/national/?page='
    newsPaper={}
    soup = soupee(url)
    titles, links = parser(soup)
    stories,heading = seeNews(titles,links)
    lists = sentimentAnalysis(newsPaper, titles, links)
    avgSentVal = avgSentiment(newsPaper, titles, links)
    AvgSentiment = find_Sentiment(avgSentVal)
    return render_template("news.html",news = "National",len = len(heading),stories=stories,heading=heading,lists=lists,AvgSentiment=AvgSentiment)

    


@app.route('/international',methods=['GET'])
@cross_origin()
def international():
    url = 'https://www.thehindu.com/news/international/?page='
    newsPaper={}
    soup = soupee(url)
    titles, links = parser(soup)
    stories,heading = seeNews(titles,links)
    lists = sentimentAnalysis(newsPaper, titles, links)
    avgSentVal = avgSentiment(newsPaper, titles, links)
    AvgSentiment = find_Sentiment(avgSentVal)
    return render_template("news.html",news = "International",len = len(heading),stories=stories,heading=heading,lists=lists,AvgSentiment=AvgSentiment)

@app.route('/science',methods=['GET'])
@cross_origin()
def science():
    url = 'https://www.thehindu.com/sci-tech/science/?page='
    newsPaper={}
    soup = soupee(url)
    titles, links = parser(soup)
    stories,heading = seeNews(titles,links)
    lists = sentimentAnalysis(newsPaper, titles, links)
    avgSentVal = avgSentiment(newsPaper, titles, links)
    AvgSentiment = find_Sentiment(avgSentVal)
    return render_template("news.html",news = "Science",len = len(heading),stories=stories,heading=heading,lists=lists,AvgSentiment=AvgSentiment)

@app.route('/business',methods=['GET'])
@cross_origin()
def business():
    url = 'https://www.thehindu.com/business/?page='
    newsPaper={}
    soup = soupee(url)
    titles, links = parser(soup)
    stories,heading = seeNews(titles,links)
    lists = sentimentAnalysis(newsPaper, titles, links)
    avgSentVal = avgSentiment(newsPaper, titles, links)
    AvgSentiment = find_Sentiment(avgSentVal)
    return render_template("news.html",news = "Business",len = len(heading),stories=stories,heading=heading,lists=lists,AvgSentiment=AvgSentiment)

@app.route('/sports',methods=['GET'])
@cross_origin()
def sports():
    url = 'https://www.thehindu.com/sport/?page='
    newsPaper={}
    soup = soupee(url)
    titles, links = parser(soup)
    stories,heading = seeNews(titles,links)
    lists = sentimentAnalysis(newsPaper, titles, links)
    avgSentVal = avgSentiment(newsPaper, titles, links)
    AvgSentiment = find_Sentiment(avgSentVal)
    return render_template("news.html",news = "Sports",len = len(heading),stories=stories,heading=heading,lists=lists,AvgSentiment=AvgSentiment)


if __name__ == "__main__":
    app.run(debug=True)  # running the app
