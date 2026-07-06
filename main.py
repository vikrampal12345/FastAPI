from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # take the request

def hello():
    return {'message': 'Hello World'} # perform logic from your request

@app.get('/about')
def about():
    return {'message': 'Campusx is an education platform where you learn AI'}