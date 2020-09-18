from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
import urllib.parse
import json
import docx

global names
names = []

#calls the user input page
def home(request):
    return render(request, 'webapp/home.html')

#parses url and calls api. Gets the json results and then creates word
#docs 
def results(request):
    ###################    API  URL IS HERE (CHANGE LATER WHEN PUBLISHED) 
    beginning = "http://127.0.0.1:8000/letterAPI/?letter="
    url = ""
    letters = request.GET['letter']
    
    url+=urllib.parse.quote_plus(letters) + "&"
    dataPoints = ["category", "bool", "val"]
    allCriteria = []
    first = True
    for x in range (5):
        individual = []
        for data in dataPoints:
            if (first):
                url+= data+str(x+1)+ "="
                url+=request.GET[data+str(x+1)]
                first = False
            else:
                url+= "&"+ data+str(x+1)+ "="
                url+=request.GET[data+str(x+1)]
            
        if(request.GET["bool"+str(x+1)]!="none"):
            for data in dataPoints:
                individual.append(request.GET[data+str(x+1)])
            allCriteria.append(individual)
    
    
    url2 = beginning + url
    response = requests.get(url2)
    #creates word documents
    for x in json.loads(response.text):
        name = x['name']
        letter = x['letter']
        doc =docx.Document()
        doc.add_paragraph(letter)
        doc.save("webapp/static/webapp/files/"+ name+ ".docx")
        names.append(name)
    
    return render(request, 'webapp/result.html')


#creates html code within the function which is then rendered on the acc page
def downloadPage(request):
    message = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Project</title>
</head>
<body bgcolor="LightGray">
    Successfully made the letters <br>
    
    """
    end="""
    </form>
</body>
</html>"""

    #html code to attach all the newly created word documents
    for name in names:
        message+= """<a href="static/webapp/files/"""+name+""".docx" download>"""+name+""".docx</a><br>"""
    names.clear
    message += end
    return HttpResponse(message)