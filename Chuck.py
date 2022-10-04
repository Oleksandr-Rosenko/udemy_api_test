import requests

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(result.text)
assert 200 == result.status_code
if  result.status_code == 200 :
    print("Successful")
else:
    print("Fail")
result.encoding = 'utf-8'
print("Status Code:" + str(result.status_code))

