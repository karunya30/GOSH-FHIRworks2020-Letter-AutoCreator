from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.letter import letterWriter as ltr



class LetterList(APIView):
    #When get request is called, parses the url and gets all the variables
    #to pass to the function written by me in letter.py
    def get(self,request):
        letter = request.GET['letter']
        dataPoints = ["category", "bool", "val"]
        allCriteria = []
        for x in range (5):
            individual = []
            if(request.GET["bool"+str(x+1)]!="none"):
                for data in dataPoints:
                    individual.append(request.GET[data+str(x+1)])
                allCriteria.append(individual)
        
        letter = letter.split("\n")
        
        json = ltr(letter, allCriteria)        
        return Response(json)





