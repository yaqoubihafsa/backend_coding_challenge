from django.shortcuts import render, redirect

from datetime import date, timedelta
import json 
import requests

# for API
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Repository
from .serializers import RepositorySerializer

from django.db.models import Count

# Create your views here.
# this method is written to get the data from the url then to store it in the DB through the model
def index(request):
    # check if the table has already records
    if(Repository.objects.all().count() == 0):
        # first, I get the date so it matches the day of last month (from now)
        one_month_ago = date.today() - timedelta(days = 30)
        print("One month's ago date:", one_month_ago)

        # format the url
        url = "https://api.github.com/search/repositories?q=created:>"+str(one_month_ago)+"&sort=stars&order=desc"

        # get the response from that url
        response = requests.get(url)

        # loop over the items so I can get the data I need to make the API 
        for item in response.json()['items']:
            values = {'name' : item['name'], 'language': item['language'], 'url': item['url']}
            serializer = RepositorySerializer(data=values)
            if serializer.is_valid():
                serializer.save()
    # once the loop is over, the user will be redirected to the page where all the repositories records 
    # will be listed, as JSON format
    return redirect('../repo/')



@api_view(['GET'])
def repo(request):
    
    if request.method == 'GET': # it means that user requesting data 
        # get all repositories
        snippets = Repository.objects.all()
        serializer = RepositorySerializer(snippets, many=True)
        return Response(serializer.data)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_list_repo_by_lang(request):
    
    if request.method == 'GET': 
        # create an empty dictionary
        list__ =  {}
        # get distinct languages used in the stored repositories
        languages = Repository.objects.values('language').distinct()

        # loop over the languages that I just get
        for x in range(0, len(languages)):
            # and then get the url's repositories which had been written in that language
            grp = Repository.objects.values('url').filter(language=languages[x]['language'])
            # finally append the result to the dictionnary I declared earlier
            list__[languages[x]['language']] = grp

        return Response(list__)  

@api_view(['GET'])
def get_count_by_lang(request):
    # make sure that the request type is GET
    if request.method == 'GET': 
        # this query is to count how many a language has been used, from the repositories 
        # that I stored earlier in the DB
        snippets = Repository.objects.values('language').annotate(dcount=Count('language'))
        # return the response
        return Response(snippets) 
