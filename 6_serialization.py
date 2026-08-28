from pydantic import BaseModel

class Address(BaseModel):  # nested class
    city : str
    state : str
    pin : str



class Patient(BaseModel):

    name : str
    gender : str
    age : int
    address : Address

address_dict = {'city' : 'gurgaon', 'state' : 'haryana', 'pin' : '122001' }

address1 = Address(**address_dict)
patient_dict = {'name' : 'Vikram', 'gender' : 'male', 'age' : 34, 'address': address1}
patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)

temp = patient1.model_dump(include=['name']  ) # return dictionary formate data

print(temp)
print(type(temp))
temp = patient1.model_dump_json(exclude = {'address' : ['state']})  # exclude_unset = True means those are not presnt in the patient list they are not print

print(temp)
print(type(temp))