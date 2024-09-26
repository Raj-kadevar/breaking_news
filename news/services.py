import requests

from news.models import NewsData


class NewsServices:
    URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=2552632e5d2e4237868e6453a039a2c5'
    def get(self, urls):
        news = requests.get(urls).json()
        articles = []

        for articles_data in news['articles']:
            name = articles_data['source']['name'],
            title = articles_data['title'],
            image = articles_data['urlToImage'],
            content = articles_data['content'],
            time = articles_data['publishedAt']
            if not NewsData.objects.filter(image=image[0], time=time[0]).exists():
                article = NewsData(name=name[0], title=title[0], image=image[0], content=content[0], time=time[0])
                articles.append(article)

        return articles
    def get_response_of_news(self):
        return self.get(self.URL)
