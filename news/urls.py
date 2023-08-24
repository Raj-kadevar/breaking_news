from django.urls import path

from news.views import IndexView, UpdateNews, DeleteNews

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
    path('update/<int:pk>/', UpdateNews.as_view(), name="update"),
    path('delete/<int:pk>/', DeleteNews.as_view(), name="delete")
]
