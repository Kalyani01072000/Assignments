import json

# Create a dictionary of Indian states and their capitals
states_capitals = {
    'Andhra Pradesh': 'Amaravati',
    'Assam': 'Dispur',
    'Bihar': 'Patna',
    'Gujarat': 'Gandhinagar',
    'Karnataka': 'Bengaluru',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur'
}

# Write the dictionary to a JSON file
with open('states_capitals.json', 'w') as json_file:
    json.dump(states_capitals, json_file)

print("JSON file 'states_capitals.json' created successfully.")


# Load the JSON data from the file
with open('states_capitals.json', 'r') as json_file:
    data = json.load(json_file)

# Access the dictionary using keys
state = 'Maharashtra'
capital = data[state]

# Print the capital of Maharashtra
print(f"The capital of {state} is {capital}")

