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
    # hitting the url for calling api to fetch data from database
    r=requests.get(url = URL,data = json_data)
    # Converting the data into json format
    data = r.json()

    print(data)
    
# get_data()

# CREATE
def post_data():
    data = {
        'name':'usama',
        'roll':'106',
        'city':'karachi',
    }

    json_data = json.dumps(data)
    r=requests.post(url = URL,data = json_data)
    data = r.json()
    print(data)
#
# post_data()


# Update 
def update_data():
    data = {
        'id':2,
        'name':'shahzaib',
        'city':'Islamabad',
    }

    json_data = json.dumps(data)
    r=requests.put(url = URL,data = json_data)
    data = r.json()
    print(data)

# update_data()



# Delete
def delete_data():
    data = {
        'id':2
    }

    json_data = json.dumps(data)
    r=requests.delete(url = URL,data = json_data)
    data = r.json()
    print(data)


delete_data()