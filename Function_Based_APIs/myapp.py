import requests
import json

URL = "http://127.0.0.1:8000/curdapi/"

# Read
# Function to get data by hitting the api and print it
def get_data(id = None):
    # initialize and empty dictionary
    data = {}
    # Check if the id is not none
    if id is not None:
        # storing the id into data variavble
        data = {'id': id}
    # After getting the id we have to convert it into json format
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}

    # hitting the url for calling api to fetch data from database
    r=requests.get(url = URL,headers=headers,data = json_data)
    # Converting the data into json format
    data = r.json()

    print(data)
    
# get_data(1)

# CREATE
def post_data():
    data = {
        'name':'huzaifa',
        'roll':'196',
        'city':'karachi',
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r=requests.post(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

# post_data()


# Update 
def update_data():
    data = {
        'id':13,
        'name':'Azhar',
        'roll':'190',
        'city':'karachi',
    }
    headers = {'content-Type':'application/json'}


    json_data = json.dumps(data)
    r=requests.put(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)

# update_data()



# Delete
def delete_data():
    data = {
        'id':13
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r=requests.delete(url = URL,headers=headers,data = json_data)
    data = r.json()
    print(data)


delete_data()