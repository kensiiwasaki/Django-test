from django.shortcuts import render
from django.http import HttpResponse   #追加
 
# Create your views here.
###以下追加###
def index(request):
    html = "<h1>myappのウェルカムページです</h1>"
    return HttpResponse(html)
 
def foo(request):
    html = "<h1>fooが指定されたときのページです</h1>"
    return HttpResponse(html)
