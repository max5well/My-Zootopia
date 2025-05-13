import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')
output = ""

for animal in animals_data:
    try:
        output += '<li class="cards__item">'
        output += f"<div class='card__title'>{animal['name']}</div>"
        output += '<p class="card__text">'
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
        output += f"<strong>Diet:</strong>: {animal['characteristics']['diet']}<br/>\n"
        output += f"<strong>Type:</strong>: {animal['characteristics']['type']}<br/>\n"



    except KeyError as e:
        print(f"Missing key: {e} in animal: {animal.get('name', 'Unknown')}")

with open('animals_template.html', 'r') as infile:
    html_code = infile.read()

# Step 3: Replace the placeholder
new_html = html_code.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 4: Write to a new HTML file
with open('animals.html', 'w') as outfile:
    outfile.write(new_html)
