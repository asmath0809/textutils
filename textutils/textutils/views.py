# i have created this file - Asmath
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('<a href="https://www.google.com">google</a><br> <a href="https://www.facebook.com">facebook</a> <br><a href="https://www.youtube.com">u tube</a><br> <a href="https://www.instagram.com">instagram</a><br><a href="https://www.snapchat.com">snap</a>' )

# def about(request):
#     return HttpResponse('about asmath')
def index(request):
    
    return render(request,'index.html')
def analyze(request):
    djtext=request.GET.get('text','default')
    #check checkbox value
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineRemover=request.GET.get('newlineRemover','off')
    spaceRemover=request.GET.get('spaceRemover','off')
    charCount=request.GET.get('charCount','off')
    extraspaceRemover=request.GET.get('extraspaceRemover','off')
    #check which check box is on
    if removepunc=="on":
        analyzed=''
        punctuations='''!()-[]{},;:'"\,<>|@#$%^&*'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuations','analyzed_text':analyzed} 
    
        return render(request,'analyze.html',params)
    elif fullcaps=='on':
        analyzed=''
        for char in djtext:
            analyzed=analyzed+char.upper()
            params={'purpose':'change to uppercase','analyzed_text':analyzed} 
    
        return render(request,'analyze.html',params)
    elif newlineRemover=='on':
        analyzed=''
        for char in djtext:
            if char !="\n":
                analyzed=analyzed+char
                params={'purpose':'remove newlines','analyzed_text':analyzed} 

    
        return render(request,'analyze.html',params)
    elif spaceRemover =='on':
        analyzed=''
        for char in djtext:
            if char !=" ":
                analyzed=analyzed+char
                params={'purpose':'remove space','analyzed_text':analyzed} 

    
        return render(request,'analyze.html',params)
    elif charCount =='on':
        count=0
        for char in djtext:
                count=count+1  
                params={'purpose':'count charectors','analyzed_text':count} 
        return render(request,'analyze.html',params)
    elif extraspaceRemover =='on':
        analyzed=''
        for index,char in enumerate (djtext):
            if not (djtext[index]==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char
                params={'purpose':' remove extraspace','analyzed_text':analyzed} 
        return render(request,'analyze.html',params)
    else:
        return HttpResponse("error please turn on remove puctuations before submiting button")
# def capfirst(request):
#     return HttpResponse('capfirst <button type="button" value="Back"><a href="http://127.0.0.1:8000/removepunc">BACK</button>')
# def newlineremove(request):
#     return HttpResponse('remove newline <button type="button" value="Back"><a href="http://127.0.0.1:8000/capfirst">BACK</button>')
# def spaceremove(request):
#     return HttpResponse('space remove <button type="button" value="Back"><a href="http://127.0.0.1:8000/newlineremove">BACK</button>')
def home(request):
     return render(request,'home.html')
#     return HttpResponse('char count <button type="button" value="Back"><a href="http://127.0.0.1:8000/spaceremove">BACK</button>')
def about(request):
     return render(request,'about.html')
def contact(request):
     return render(request,'contact.html')