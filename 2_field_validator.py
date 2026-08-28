from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]

    @field_validator('email')        # field_validator is used to apply rules and regulation
    @classmethod

    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']
        domain_name = str(value).split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()


    @field_validator('age', mode='after')  # mode operates in before and after. after is dafult value, mode is used for the type conversion
    @classmethod
    def validate_age(cls,value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError('Age should be in between 0 to 100')        

def update_patient_data(patient: Patient):
    print(patient.name)    
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

Patient_info = {'name': 'nitish','email' : 'abc@hdfc.com', 'linkedin_url' : 'http://linked//1234' , 'age' : 30, 'weight' :67.9, 'married' : True,  'contact_details' : {'phone' : '2353462'}}
# if any field is left then it got error
Patient1 = Patient(**Patient_info)

update_patient_data(Patient1)      