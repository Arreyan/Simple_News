from django.shortcuts import render
from django.shortcuts import render
from newsapi import NewsApiClient


# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key='2de7cc28c3bf42a48219f900a14a5daa')
    top = newsapi.get_top_headlines(sources='new-scientist')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'index.html', context={"mylist": mylist})
