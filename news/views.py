import requests
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView
from news.forms import UpdateNewsForm
from news.models import NewsData


class IndexView(View):
    def get(self, request, *args, **kwargs):
        news = requests.get(
            'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=2552632e5d2e4237868e6453a039a2c5').json()
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

        NewsData.objects.bulk_create(articles)
        all_news = NewsData.objects.all().order_by('-id')
        return render(request, "news/index.html", {"news": all_news})


class UpdateNews(UpdateView):
    form_class = UpdateNewsForm
    template_name = "news/update.html"
    success_url = reverse_lazy("home")
    queryset = NewsData.objects.all()


class DeleteNews(DeleteView):
    def get(self, *args, **kwargs):
        NewsData.objects.get(id=kwargs.get("pk")).delete()
        return redirect("home")
