from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    url = "https://newsapi.org/v2/everything?q=world&apiKey=ae939bfa8a8e44259283dd51ca570247"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(title, desc, img)
    context = {'myList': myList}

    return render(request, 'index.html', context)

def microsoft(request):
    url = "https://newsapi.org/v2/everything?q=microsoft&apiKey=ae939bfa8a8e44259283dd51ca570247"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(title, desc, img)
    context = {'myList': myList}

    return render(request, 'microsoft.html', context)


def apple(request):
    url = "https://newsapi.org/v2/everything?q=apple&apiKey=ae939bfa8a8e44259283dd51ca570247"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(title, desc, img)
    context = {'myList': myList}

    return render(request, 'apple.html', context)

def gaming(request):
    url = "https://newsapi.org/v2/everything?q=gaming&apiKey=ae939bfa8a8e44259283dd51ca570247"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(title, desc, img)
    context = {'myList': myList}

    return render(request, 'gaming.html', context)

def world(request):
    url = "https://newsapi.org/v2/everything?q=world&apiKey=ae939bfa8a8e44259283dd51ca570247"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(title, desc, img)
    context = {'myList': myList}

    return render(request, 'world.html', context)

def samsung(request):
    url = "https://newsapi.org/v2/everything?q=samsung&apiKey=ae939bfa8a8e44259283dd51ca570247"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(title, desc, img)
    context = {'myList': myList}

    return render(request, 'samsung.html', context)


def sony(request):
    url = "https://newsapi.org/v2/everything?q=sony&apiKey=ae939bfa8a8e44259283dd51ca570247"
    cricket_news = requests.get(url).json()

    a = cricket_news['articles']
    desc = []
    title = []
    img = []

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])

    myList = zip(title, desc, img)
    context = {'myList': myList}

    return render(request, 'sony.html', context)