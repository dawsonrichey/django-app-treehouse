from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html', {'hithere':'This is me'})

def about(request):
    return render(request, 'about.html')

def eggs(request):
    return HttpResponse('Eggs are great!!!!')


def count(request):
    user_storage = {}
    fulltext = request.GET['fulltext']
    passw = request.GET['passw']
    username= request.GET['username']
    user_storage.update([('username', username) , ('password', passw)] )
    # user_storage += {'user':username, 'pass':passw}
    # print(fulltext)
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1


    def storage(request):
        passw = request.GET['passw']
        username = request.GET['username']
        user_storage.update({'username':username, 'password':passw})

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html',{'user_storage':user_storage,'fulltext':fulltext,'passw':passw,'username':username,'count':len(wordlist),'sortedwords':sortedwords})