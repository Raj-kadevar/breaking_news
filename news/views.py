from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView, DeleteView
from news.forms import UpdateNewsForm
from news.models import NewsData
from news.services import NewsServices


class IndexView(View):
    def get(self, request, *args, **kwargs):
        try:
            articles = NewsServices().get_response_of_news()
            NewsData.objects.bulk_create(articles)
            all_news = NewsData.objects.all().order_by('-id')
            return render(request, "news/index.html", {"news": all_news})
        except Exception as error:
            return HttpResponse(f"error = {error}")


class UpdateNews(UpdateView):
    form_class = UpdateNewsForm
    template_name = "news/update.html"
    success_url = reverse_lazy("home")
    queryset = NewsData.objects.all()


class DeleteNews(DeleteView):
    def get(self, *args, **kwargs):
        try:
            NewsData.objects.get(id=kwargs.get("pk")).delete()
            return redirect("home")
        except ObjectDoesNotExist:
            return HttpResponse("<h2>Object not fount pls go back</h2>")