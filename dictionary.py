import json
import difflib

with open ('data.json', 'r') as file:
    data = json.load(file)

def get_definition(word):
    word = word.lower()

    if word in data:
        return data[word]
    else:
        closest_match = difflib.get_close_matches(word, data.keys(), n=1, cutoff=0.8)
        if closest_match:
            return f"Word not found. Did you mean '{closest_match[0]}'?"
        else:
            return "Word not found."


while True:
    word = input("Enter a word (or type 'exit' to quit): ")
    if word.lower() == 'exit':
        break


    definition = get_definition(word)
    print(definition)