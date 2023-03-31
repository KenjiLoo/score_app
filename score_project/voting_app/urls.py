from .views import get_score
from django.contrib import admin
from django.urls import include, path
from .views import get_score, score_list

urlpatterns = [
    path('api/get_score/', get_score, name='get_score'),
    path('', score_list, name='score_list'),
    path('score_list/', score_list, name='score_list')
]