from django.urls import path
from .views import topHeadlinesFrom, businessArticles,allAboutThis,topHeadlinesFromBBC,predictNews

urlpatterns = [
    path('businessArticles/<country>/',businessArticles),
    path('allAbout/<subject>/',allAboutThis),
    path('topsFrom/<country>/',topHeadlinesFrom),
    path('topsFromBBC/',topHeadlinesFromBBC),
    path('predict/',predictNews)

    
]
