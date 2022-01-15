from django.http.response import Http404, HttpResponse
import requests,os
from decouple import config
from rest_framework.response import Response
from rest_framework.decorators import api_view
from FakeNews.MLModel.fakeNewsModel import Predict

key=config('KEY')

@api_view(('GET',))
def businessArticles(request,country):  
        requestURL="https://newsapi.org/v2/top-headlines?country={}&category=business&apiKey={}".format(country,key)
        res=requests.get(requestURL).json()
        data=res['articles'] 
        if(not data):
            return Response(status=404)
        return Response(data,status=200)

@api_view(('GET',))
def allAboutThis(request,subject):
        requestURL="https://newsapi.org/v2/everything?q={}&from=2021-12-10&sortBy=publishedAt&apiKey={}".format(subject,key)
        res=requests.get(requestURL).json()
        data=res['articles'] 
        if(not data):
            return Response(status=404)
        return Response(data,status=200)

@api_view(('GET',))
def topHeadlinesFrom(request,country):
        requestURL="https://newsapi.org/v2/top-headlines?country={}&apiKey={}".format(country,key)
        res=requests.get(requestURL).json()
        data=res['articles'] 
        if(not data):
            return Response(status=404)
        return Response(data,status=200)
@api_view(('GET',))
def topHeadlinesFromBBC(request):
        requestURL="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}".format(key)
        res=requests.get(requestURL).jsonx()
        data=res['articles'] 
        if(not data):
            return Response(status=404)
        return Response(data,status=200)

@api_view(('GET','POST'))
def predictNews(request):
    news= request.POST.get("news")
    try:
       res = Predict(news).predict()
       return Response(res,status=200)
    except:
        return Response("Internal Error....please Try again ", status=500)
   
    


