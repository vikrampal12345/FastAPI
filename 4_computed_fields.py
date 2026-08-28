from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator, computed_field
from typing import List, Dict, Optional, Annotated


class Patient(BaseModel):

    name : str
    email : EmailStr
    age : int
    weight : float
    height : float
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]
    
    @computed_field
    @property 
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi   
       

def update_patient_data(patient: Patient):
    print(patient.name)    
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print('BMI', patient.bmi)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

Patient_info = {'name': 'nitish','email' : 'abc@hdfc.com', 'linkedin_url' : 'http://linked//1234' , 'age' : 40, 'weight' :67.9, 'height' : 1.2 , 'married' : True,  'contact_details' : {'phone' : '2353462'}}
# if any field is left then it got error
Patient1 = Patient(**Patient_info)

update_patient_data(Patient1)      