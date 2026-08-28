from fastapi import FastAPI, Path, HTTPException, Query
import json

# Path() function is used for the metadata, validation rules, 
# and documentation hints for the path parameters in your API endpoints.
# for example - description, ge, gt, le, It, Min_lengh, Max_length, regex

# -----------------------------------------------------------#

# HTTPException - is a special built-in exception in FastAPI used to return custom HTTP error 
# responses when something goes wrong in your API.

# -----------------------------------------------------------#


# Query Parameter
# Query parameter are optional key-value pairs appended to the end of a URL, used to pass additional
# data to the server in an HTTP request. They arg typically employed for the operations like filtering,
# sorting, searching, and pagination, without altering the endpoint path itself.
# ? - marks the start for the query parameters.
# Each parameter is a key-value pair: key=value
# Multiple parameters are separated by &

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data    

@app.get("/")
def hello():
    return {'message': 'Hello world'}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage your patient records"} 

@app.get("/view")
def view():
    data = load_data()
    
    return data


@app.get("/patient/{patient_id}")
def view_patient(patient_id : str = Path(..., description = "Id of the patient in the DB", example = "P001" )): # first three dots means required 
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail = 'Patient not found')    


@app.get('/sort')
def sort_patients(sort_by:str = Query(..., description = 'Sort on the basis of the height, weight or bmi'), order: str = Query('asc', description='sort in asc or desc order')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select between asc and desc')


    data = load_data()

    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)   

    return sorted_data