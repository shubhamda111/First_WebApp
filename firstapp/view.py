from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

def home(request):
    return render(request,'index.html',{'key1':'i am from python'})
def result(request):
    article = request.GET['article']
    var_dict,word_count=counter.count(article)
    return render(request,'result.html',{'article':article,'word_count':word_count,'dict_words':var_dict})

