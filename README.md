# GOSH-FHIRworks2020-Letter-AutoCreator
The users add criteria to filter patients and input a sample letter with variables replaced with patient data stored in the FHIR records, to auto-create tailored letters to patients.

## Video of project
[![Image of FHIRDemo](https://github.com/karunya30/GOSH-FHIRworks2020-Letter-AutoCreator/blob/master/FHIR.JPG)](https://youtu.be/inKUyaiKJlU)

Youtube Link: https://youtu.be/inKUyaiKJlU

## How to set up Project

Make sure to run python 3.7
Python libraries that will be needed: FHIR-Parser, json, django, django rest framework, requests, urllib.parse, json, docx, dateutil

### To set this project up:
Make sure to run 'dotnet run' --> this allows access to the server where all the patient data is

Within the command line, direct your to inside the myapi directory first (../GOSH-FHIRworks2020-Karunya-Selvaratnam/myapi/)
Next make sure to run the command 'python manage.py runserver' (preferrably 'py -3.7 manage.py runserver')

Then open another command line and direct your way to the mysite directory(../GOSH-FHIRworks2020-Karunya-Selvaratnam/mysite/)
Run the command 'python manage.py runserver 7000' (preferrably 'py -3.7 manage.py runserver 7000')

## Secret Key
In the settings.py file, line 23, in both myapi and mysite, uncomment the line and store django secret key in that variable. 

#### IMPORTANT:
Make sure that myapi is on port 8000 and mysite is on a different port 

------------------------------------------------------------------------------
Then open the following URL and follow instructions:
http://127.0.0.1:7000/letterreader/


#### Side note:
The API is written within the myapi folder
The demo that shows the API working is within the mysite folder
