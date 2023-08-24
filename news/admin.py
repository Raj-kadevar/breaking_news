from django.contrib import admin

from news.models import NewsData


@admin.register(NewsData)
class NewsInfo(admin.ModelAdmin):
    list_display = ["name", "title", "image", "time"]
