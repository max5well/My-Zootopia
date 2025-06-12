import requests

API_KEY = 'rLTeXYU0+WOouTvDsPzTtQ==ID4hu39rnko8WJmi'

def main():
    animal_name = input("Enter animal's name: ")
    fetch_data(animal_name)


def fetch_data(animal_name):
    url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    animal_raw_data = requests.get(url, headers={'X-Api-Key': API_KEY})
    if animal_raw_data.status_code == requests.codes.ok:
        return animal_raw_data.json()
    else:
        print("Error:", animal_raw_data.status_code, animal_raw_data.text)



if __name__ == '__main__':
    main()