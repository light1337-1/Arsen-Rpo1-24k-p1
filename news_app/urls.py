from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('news/all/', views.all_news_page, name='all_news_page'),
path('news/read/<int:pk>/', views.read_news_page, name='read_news_page'),
path('search/news/', views.search_page, name='search_page'),
path('search/news/results', views.search_results, name='search_results'),

    path('news/categories/<int:pk>/', views.news_by_category, name='news_by_category'),
]