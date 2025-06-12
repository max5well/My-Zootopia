import requests
animal_name = input("Enter animal's name: ")
API_KEY = 'rLTeXYU0+WOouTvDsPzTtQ==ID4hu39rnko8WJmi'
URL = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)

response = requests.get(URL, headers={'X-Api-Key': API_KEY})
if response.status_code == requests.codes.ok:
    print(response.json())
else:
    print("Error:", response.status_code, response.text)