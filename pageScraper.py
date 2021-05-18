import requests  
# bs4 helps decode and search through page.                                            
from bs4 import BeautifulSoup as bs                                         

# The User-Agent request header contains a characteristic string 
# that allows the network protocol peers to identify the application type, 
# operating system, and software version of the requesting software user agent.
# needed for google search
u_agnt = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
} #write: 'my user agent' in browser to get your browser user agent details

# For making individual page URLS


# Create Soup object with bs4
def soupee(url):          
  response = requests.get(url, headers=u_agnt)  
  html = response.text #To get actual result i.e. to read the html data in text mode                                                
  soup = bs(html, 'html.parser')
  return soup

# Parse page and create two lists of the titles and link
# to each news of title
def parser(soup):                                                          
  titles = []                                                               
  links = []
  for news in soup.find_all('div', class_='story-card-news'):
    try:
      title = news.h3.text
    except:
      title = news.h2.text  
    link = news.find_all('a')
    titles.append(title)
    links.append(link[2]['href'])
  return  titles, links

# Use the Links list to goto the site and get the first two
# paragraphs of the new and return a story list.
def newsStoryGrabber(links):                                                
  data=[]                                                                   
  for i in range(len(links)):
    url = links[i]
    response = requests.get(url, headers=u_agnt)  
    html = response.text #To get actual result i.e. to read the html data in text mode                                                
    soup = bs(html, 'html.parser')
    aa = soup.find('div', class_='article')
    bb = aa.find_all('p')
    cc = bb[1].text + bb[2].text
    data.append(cc)
  return data

 # Show each story with title as the indices of each correspond 
 # correctly, i.e. index zero of both are for same News.
def seeNews(titles,links):                                                 
  stories = newsStoryGrabber(links)     
  return stories,titles                                    

