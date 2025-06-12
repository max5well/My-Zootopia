import data_fetcher

TEMPLATE_PATH = 'animals_template.html'
NEW_FILE_PATH = 'animals.html'

def serialize_animal(data):
    name = data.get('name', 'Unknown')
    location = data.get('locations', ['Unknown'])[0]
    characteristics = data.get('characteristics', {})
    diet = characteristics.get('diet', 'Unknown')
    threat = characteristics.get('biggest_threat', 'Unknown')
    animal_type = characteristics.get('type', 'Unknown')

    output = '<li class="cards__item">\n'
    output += f"  <div class='card__title'>{name}</div>\n"
    output += '  <p class="card__text">\n'
    output += f"    <strong>Location:</strong> {location}<br/>\n"
    output += f"    <strong>Diet:</strong> {diet}<br/>\n"
    output += f"    <strong>Type:</strong> {animal_type}<br/>\n"
    output += f"    <strong>Biggest threat:</strong> {threat}<br/>\n"
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
    animal_name = input("Please enter an animal: ")
    data = data_fetcher.fetch_data(animal_name)
    print(data)
    output = create_animal_content(data)
    generate_html(TEMPLATE_PATH, output, NEW_FILE_PATH)


if __name__ == "__main__":
    main()