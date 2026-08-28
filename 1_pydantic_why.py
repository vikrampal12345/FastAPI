
# Pydantic

# 1. Define a pydantic model that represents the ideal schema of the data
# * This includes the expected fields, their types, and any validation constraints (eg. gt = 0 for positive numbers).

# 2. Instantiate the model with raw input data (usually a dictionary or JSON-like structure).
# * Pydantic will outomatically validate the data and coerce it into the correct Python types (if possible)
# * if the data doesn't meet the model's requirements, Pydantic raises a ValidationError.

# 3. Pass the validated model object to functions or use it throughout your codebase.
# * This ensures that every part of your program works with clean, type-safe, and logically valid data.

# def insert_patient_data(name: str, age: int): # here the problem we not follow the strict rule for the input same datatype
#     print(name)
#     print(age)
#     print('inserted into database')

# insert_patient_data("vikram", '30')

# def insert_patient_data(name: str, age: int): # here we fix with the using logic but it is not scalable
    
#     if type(name) == str and type(age) == int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect data type')    

# insert_patient_data("vikram", 30)

from pydantic import BaseModel, EmailStr, AnyUrl, Field  # EmailStr use for the email verify, and AnyUrl is used for the verify and type of url
from typing import List, Dict, Optional, Annotated  # Optional give the the option to fill or not and it gives default values.

class Patient(BaseModel):

    name : Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 chars', examples=['Nitish', 'Amit'])]  # Annoted used to attach meta data
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt=0, lt = 60)   # Field used for the adjust in between the value like 0 to 60 year
    weight : Annotated[float, Field(gt=0, strict=True)]  # strict used for the only pass the those datatypes      
    married : Annotated[bool, Field(default = None, description='Is the patient married or not')]  # default values
    allergies : Annotated[Optional[List[str]], Field(default=None, max_length=5)]   # use this 'List' instead of this 'list' because it verify it list and their inside string avaliable
    contact_details : Dict[str, str]  # same with this 


def insert_patient_data(patient: Patient):

    print(patient.name)
    print(patient.age)
    print('Inserted')

def update_patient_data(patient: Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

    print('update')

Patient_info = {'name': 'nitish','email' : 'abc@gmail.com', 'linkedin_url' : 'http://linked//1234' , 'age' : 30, 'weight' :67.9, 'married' : True,  'contact_details' : {'email' : 'abc@gmail.com',  'phone' : '2353462'}}
# if any field is left then it got error
Patient1 = Patient(**Patient_info)

update_patient_data(Patient1)

