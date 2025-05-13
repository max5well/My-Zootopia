import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

for animal in range(len(animals_data)):
    try:
        print(f"Name: {animals_data[animal]['name']}")
        print(f"Location: {animals_data[animal]['locations'][0]}")
        print(f"Diet: {animals_data[animal]['characteristics']['diet']}")
        print(f"Type: {animals_data[animal]['characteristics']['type']}")
        print()
    except:
        print("")


