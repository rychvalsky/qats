import jsonpath
import requests
import json


url = "https://reqres.in/api/users"

file = open('C:\\Users\\< meno uzivatela >\\Desktop\\qats_post_api.json','r')
json_input = file.read()
request_json = json.loads(json_input)


response = requests.post(url,request_json)

print(response.elapsed.total_seconds())
print(response)
assert response.status_code == 201
assert response.elapsed.total_seconds() != 0.1






response_json = json.loads(response.text)
id = jsonpath.jsonpath(response_json,'id')
createdAt = jsonpath.jsonpath(response_json,'createdAt')

print(id[0],createdAt[0])






