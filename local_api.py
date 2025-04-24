import json

import requests

# TODO: send a GET using the URL http://127.0.0.1:8000
url = "http://127.0.0.1:8000"
get_response = requests.get(url)
print(f"Get Status: {get_response.status_code}")
print(f"Get Message: {get_response.json()}")

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
post_response = requests.post(f"{url}/data/", json=data)
print(f"POST Status: {post_response.status_code}")
try:
    print(f"Prediction: {post_response.json()}")
except Exception:
    print("Server response (raw):", post_response.text)