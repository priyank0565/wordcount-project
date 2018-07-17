from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html', {'code': 4212})


def about(request):
    return render(request, 'about.html')


def count(request):
    text = request.GET['word']
    wordlist = text.split()
    wordcounter = {}

    for x in wordlist:
        if x in wordcounter:
            wordcounter[x] += 1

        else:
            wordcounter[x] = 1

    sortedcounter = sorted(wordcounter.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext': text, 'wordcount': len(wordlist), 'sortedcounter': sortedcounter})

