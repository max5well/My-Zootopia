import json

def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')
output = ''

for animal in animals_data:
    try:
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Location: {animal['locations'][0]}<br/>\n"
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += '</li>'

    except KeyError as e:
        print(f"Missing key: {e} in animal: {animal.get('name', 'Unknown')}")

with open('animals_template.html', 'r') as infile:
    html_code = infile.read()

# Step 3: Replace the placeholder
new_html = html_code.replace("__REPLACE_ANIMALS_INFO__", output)

# Step 4: Write to a new HTML file
with open('animals.html', 'w') as outfile:
    outfile.write(new_html)
