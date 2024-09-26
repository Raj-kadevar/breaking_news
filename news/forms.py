from django import forms
from news.models import NewsData

class UpdateNewsForm(forms.ModelForm):
    class Meta:
        model = NewsData
        fields = ["name", "title", "image", "content", "time"]