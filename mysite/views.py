#I have created this file-Aman
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index2.html')

##here we change default nature of method that is get to post to hide information from url and to clean our url too!!
def analyze(request):
    djtext=request.POST.get('text','default')
    print(djtext)
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    print(removepunc)
    print(fullcaps)
    if removepunc=='on':
        punctuations='''!()-[]{};:'"<>./?@&*%__-'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze2.html',params)
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'capitalization','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze2.html',params)

    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyzed=analyzed + char
        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}

    if(removepunc!='on' and fullcaps!='on' and newlineremover!='on'):
        return HttpResponse('Select atleast any one option')
    return render(request,'analyze2.html',params)











# def capfirst(request):
#     return HttpResponse("capitalize first")
