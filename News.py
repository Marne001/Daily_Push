from newsapi.newsapi_client import NewsApiClient


class News:
    def getNews():
        news = ''

        newsapi = NewsApiClient(api_key='c2cca8b3de6844e3a0e789acf524f939')

        top_headlines = newsapi.get_top_headlines(q='', language='en', sources='business-insider, Mybroadband.co.za, Ewn.co.za')

        for article in top_headlines['articles']:
            newsTitle = article['title']
            newsDescription = article['description']
            newsUrl = article['url']
            #print('Title: ', article['title'])
            #print('Description: ', article['description'],'\n\n')
            #print(news)
            break
        return('Title: ' + newsTitle + '\nDescription: ' + newsDescription + '\n' + newsUrl)
