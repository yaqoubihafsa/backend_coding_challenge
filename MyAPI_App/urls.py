from django.urls import path, include
from . import views

urlpatterns = [
    # call this url if the Repository table is with 0 records
    path('index/', views.index, name='index'),
    # this one is to list the records from the table
    path('repo/', views.repo, name='repo'),
    # and this is to count the number of repositories for each language
    path('repo/get_count_by_lang', views.get_count_by_lang, name='get-lang'),
    # finally this one is to list, for each language, the url of repositories
    path('repo/get_list_repo_by_lang', views.get_list_repo_by_lang, name='get-list')
]
