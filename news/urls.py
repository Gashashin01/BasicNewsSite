from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name = 'home'),
    path('', HomeNews.as_view(), name = 'home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('post/<int:news_id>/', get_post, name='post'),
    path('news/add-news/', add_news, name='add_news'),
]
