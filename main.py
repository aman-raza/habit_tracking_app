import requests
from datetime import date

USERNAME = "amanraza"
TOKEN = "buiqw987celan"

# user creation

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# addition of graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "gym",
    "unit": "days",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# adding data to the graph

add_pixel_endpoint = f"{graph_endpoint}/graph1"

current_date = str(date.today())
date_string = "".join(current_date.split("-"))
print(date_string)

graph_body = {
    "date": date_string,
    "quantity": "1"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=add_pixel_endpoint, json=graph_body, headers=headers)
print(response.text)

# update the date

update_endpoint = f"{add_pixel_endpoint}/{date_string}"

new_data = {
    "quantity": "2"
}

response = requests.put(url=update_endpoint, json=new_data, headers=headers)
print(response.text)
