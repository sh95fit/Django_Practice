import requests
from info import id, pw

url = 'http://127.0.0.1:8000/api/auth'

response = requests.post(url, data={'username':id,'password':pw})

# print(response.text)

myToken = response.json()

# print(myToken['token'])


header = {'Authorization' : 'Token ' + myToken['token']}
response = requests.get('http://127.0.0.1:8000/api/student_list', headers=header)
print(response.text)