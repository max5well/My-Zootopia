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

def generate_html(template_path, content, output_path):
    with open(template_path, 'r') as infile:
        html_code = infile.read()
    new_html = html_code.replace("__REPLACE_ANIMALS_INFO__", content)
    with open(output_path, 'w') as outfile:
        outfile.write(new_html)


def main():
    animal_name = input("Enter animal name: ").strip()
    api_data = data_fetcher.fetch_data(animal_name)

    if api_data and len(api_data) > 0:
        html_content = ""
        for animal in api_data:
            html_content += serialize_animal(animal) + "<hr>"  # Optional: Trenner zwischen Tieren
        print("Website was successfully generated to the file animals.html.")
    else:
        html_content = f'<h2>The animal "{animal_name}" doesn\'t exist or data could not be loaded.</h2>'
        print("Website was not successfully generated.")

    generate_html(TEMPLATE_PATH, html_content, NEW_FILE_PATH)


if __name__ == "__main__":
    main()
