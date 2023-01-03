from django.shortcuts import render
from django.http import HttpResponse
 
# Create your views here.
###以下追加###
def index(request):
    html = "<h1>練習問題です</h1>"
    return HttpResponse(html)
