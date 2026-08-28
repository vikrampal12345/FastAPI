from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model    
       

def update_patient_data(patient: Patient):
    print(patient.name)    
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

Patient_info = {'name': 'nitish','email' : 'abc@hdfc.com', 'linkedin_url' : 'http://linked//1234' , 'age' : 40, 'weight' :67.9, 'married' : True,  'contact_details' : {'phone' : '2353462'}}
# if any field is left then it got error
Patient1 = Patient(**Patient_info)

update_patient_data(Patient1)      