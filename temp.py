import requests, json


url = "http://127.0.0.1:8000/snippets/"
url2='http://127.0.0.1:8000/api-auth/login/'
body = {"code":"hhh"}
headers = {'Content-Type': 'application/json', 'charset': 'UTF-8', 'Accept': '*/*'}
response = requests.post(url, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
print(response)

body = {"username": "admin",
"password": "11111"}
response = requests.get(url2, headers=headers, data=json.dumps(body, ensure_ascii=False, indent="\t"))
print(response.text)
