#i have created this file- Bunny

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("hello bunny")

# def index(request):
#     return HttpResponse("""<a href=https://www.facebook.com/>Facebook</a><br><a href=https://www.google.com/>Google</a><br><a href=https://getbootstrap.com/>Bootstrap</a><br><a href=https://www.cricbuzz.com/>cricbuzz</a><br><a href=https://timesofindia.indiatimes.com/>TOI</a>""")
#
# def about(request):
#     return HttpResponse("about hello bunny")


# def bootstrap(request):
#     return HttpResponse(""""<a href=https://getbootstrap.com/>Bootstrap</a>""")
#
# def cricbuzz(request):
#     return HttpResponse("""<a href=https://www.cricbuzz.com/>cricbuzz</a>""")
#
# def toi(request):
#     return HttpResponse("""<a href=https://timesofindia.indiatimes.com/>TOI</a>""")

def index(request):

    return render(request,'index.html')
    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    #Check the checkbox value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # charactercounter = request.POST.get('charactercounter', 'off')

    #check which checkbox is on
    if removepunc=="on":

        #analyzed=djtext

        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
        # return HttpResponse("remove punc <br><a href='/'>Back</a>")
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed + char.upper()
        params={'purpose':'changed to uppercase', 'analyzed_text':analyzed}
        #Analyze the text
        djtext = analyzed
        # return render(request,'analyze.html',params)

    # elif(charactercounter=="on"):
    #     analyzed=""
    #     for char in djtext:
    #         analyzed=analyzed + char
    #     print(len(djtext))
    #     params={'purpose':'no of characters', 'analyzed_text':analyzed}
    #     #Analyze the text
    #     return render(request,'analyze.html',params)

    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]== " " and djtext[index+1]==" "):
                analyzed=analyzed+char

        params={'purpose':'changed to uppercase', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)


    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed=analyzed + char
        params={'purpose':'Removed NewLines', 'analyzed_text':analyzed}
        #Analyze the text
        djtext = analyzed
    return render(request,'analyze.html',params)
    # else:
    #     return HttpResponse("Error")


# def removepunc(request):
#     #Get the text
#     djtext = request.GET.get('text', 'default')
#     print(djtext)
#     #Analyze the text
#     return HttpResponse("remove punc <br><a href='/'>Back</a>")
#
# def capfirst(request):
#     return HttpResponse("capitalize first <br><a href='/'>Back</a>")
#
# def newlineremove(request):
#     return HttpResponse("new line remover <br><a href='/'>Back</a>")
#
# def spaceremove(request):
#     return HttpResponse("space remover <br><a href='/'>Back</a>")
#
# def charcount(request):
#     return HttpResponse("char counter <br><a href='/'>Back</a>")