from dateutil.relativedelta import relativedelta
from fhir_parser import FHIR
import datetime
fhir = FHIR()
patients = fhir.get_all_patients()
patients.pop(0)

import json

#This function takes the template letter and fills in the blank details
def write_letter(letter, patient, criteria):
    letterContent = []
    name = patient.name.full_name

    #parses the text to find the text that represents the correct format
    for line in letter:
        words = line.split()
        #SUPPORTS CRITERIA, ADDRESS, NAME
        for x in words:
            toreplace = x
            if x[:2] == "^^" and x[-2:] == "^^":
                lookup = x[2:-2].lower()
                if lookup == "name":
                    toreplace = name
                if lookup == "full_address":
                    toreplace  = patient.addresses[0].full_address
                if lookup == "criteria":
                    sentence = ""
                    for i in criteria:
                        s=" ".join(i)                        
                        sentence += s + "\n"
                    toreplace = sentence
            
            letterContent.append(toreplace)
        letterContent.append("\n")

    finalLetterContent = " ".join(letterContent)
    jsonString ={"name" :  name  ,  "letter" :  finalLetterContent }
    return jsonString


#Function that does the boolean operation depending on what the user selected
def boolean_operator(patient_data, operator, conditionData):
    if operator == ">":
        if patient_data > conditionData:
            return True
        else:
            return False
    elif operator == "<":
        if patient_data < conditionData:
            return True
        else:
            return False
    elif operator == "<=":
        if patient_data <= conditionData:
            return True
        else:
            return False
    elif operator == ">=":
        if patient_data >= conditionData:
            return True
        else:
            return False
    elif operator == "==":
        if patient_data == conditionData:
            return True
        else:
            return False
    elif operator == "!=":
        if patient_data != conditionData:
            return True
        else:
            return False


#Function that goes through all the patients list and filters them out according to the conditions
def letterWriter(letter, conditionList):
    correctPatients = patients
    temp=set([])
    
    for condition in conditionList:
        print(len(correctPatients))
        if condition[0] == "Age":
            for patient in correctPatients:
                birthday = patient.birth_date
                today = datetime.date.today()
                age = relativedelta(today, birthday).years
                if boolean_operator(age, condition[1], int(condition[2])):
                    temp.add(patient)
        
        elif condition[0] == "Gender":
            n=0
            for patient in correctPatients:
                gender = patient.gender
                n+=1
                if boolean_operator(gender, "==", condition[2]):
                    temp.add(patient)
        else:
            for patient in correctPatients:
                observations = fhir.get_patient_observations(patient.uuid)
                for observation in observations:
                    for component in observation.components:
                        if component.display == condition[0]:
                            if boolean_operator(float(component.value), condition[1], float(condition[2])):
                                temp.add(patient)
                            
                            
            
        correctPatients = []
        correctPatients = temp
        temp = set([])
    
    #creates a json formatted string to send as a result of calling the api
    jsonString= ""

    jsonString = []
    for patientToBeGivenLetter in correctPatients:
       jsonString.append(write_letter(letter, patientToBeGivenLetter, conditionList))
 
    return (jsonString)
    
    
