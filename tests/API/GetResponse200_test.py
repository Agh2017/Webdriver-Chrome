import requests

response = requests.get('https://google.com')
print(response.status_code)
assert response.status_code == 200, "response is wrong"
#print(response.text)
