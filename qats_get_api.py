
import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"
# posielame get request
response = requests.get(url)

assert response.status_code == 200

#parsovanie response do json formatu

json_response = json.loads(response.text)
#print(json_response)

# verifikacia total pages
total = jsonpath.jsonpath(json_response,'total')
assert total[0] == 12
print(total)

#

for i in range(0,6):
    last_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].last_name')
    print((last_name[0]))

result = total == i
print(result)
