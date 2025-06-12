import json

TEMPLATE_PATH = 'animals_template.html'
ANIMALS_DATA_PATH = 'animals_data.json'
NEW_FILE_PATH = 'animals.html'

def load_data(ANIMALS_DATA_PATH):
    with open(ANIMALS_DATA_PATH, "r") as handle:
        content = json.load(handle)
        return content


def serialize_animal(animal):
    '''
    Creating the HTML tags with the animal data.
    '''
    name = animal.get('name', 'Unknown')
    location = animal.get('locations', ['Unknown'])[0]
    characteristics = animal.get('characteristics', {})
    diet = characteristics.get('diet', 'Unknown')
    animal_type = characteristics.get('type', 'Unknown')

    output = '<li class="cards__item">\n'
    output += f"  <div class='card__title'>{name}</div>\n"
    output += '  <p class="card__text">\n'
    output += f"    <strong>Location:</strong> {location}<br/>\n"
    output += f"    <strong>Diet:</strong> {diet}<br/>\n"
    output += f"    <strong>Type:</strong> {animal_type}<br/>\n"
    output += '  </p>\n'
    output += '</li>\n'
    return output


def create_animal_content(content):
    output = ''
    for animal_obj in content:
        try:
            output += serialize_animal(animal_obj)
        except KeyError as e:
            print(f"Missing key: {e} in animal: {animal_obj.get('name', 'Unknown')}")
    return output

#Reading the existing template and replace the placeholder text with the animal data.
def generate_html(TEMPLATE_PATH, output, NEW_FILE_PATH):
    with open(TEMPLATE_PATH, 'r') as infile:
        html_code = infile.read()

    new_html = html_code.replace("__REPLACE_ANIMALS_INFO__", output)

    with open(NEW_FILE_PATH, 'w') as outfile:
        outfile.write(new_html)


def main():
    content = load_data(ANIMALS_DATA_PATH)
    output = create_animal_content(content)
    generate_html(TEMPLATE_PATH, output, NEW_FILE_PATH)


if __name__ == "__main__":
    main()
