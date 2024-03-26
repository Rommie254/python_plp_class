'''
create a program that automates searching for a word definition in a dictionary.
1. load json data into a python dictionary
2. Create a function that returns a definition of a word
3. Make your dictionary program more intelligent to give spelling suggestions using difflib library.
'''

import json
import difflib


def load_data (json_file_path):
    '''
    Load JSON data from a file into a Python dictionary
    '''

    with open (json_file_path, 'r') as file:
        dictionary_data = json.load(file)

    return dictionary_data

def get_definition(word, dictionary_data):
    '''
    Retrieve the definition of a word from the dictionary data
    '''
    #Convert the word to lowercase to make the search case-insensitive
    word = word.lower()

    # Check if the word exists in the dictionary
    if word in dictionary_data:
        return dictionary_data[word]
    
    else:
        # If the word is not found, try to find similar words
        similar_word = difflib.get_close_matches(word,dictionary_data.keys())
        if similar_word:
            suggestion = similar_word[0]
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return f"No definition found for '{word}'"

# Path to the JSON data file
json_file_path = r"C:\Users\sharo\Desktop\PLP\python_plp_class\Dictionary Project\data.json"

# Load the dictionary data
dictionary_data = load_data(json_file_path)

# Get word from user
word = input("Enter a word to get its definition: ")
definition = get_definition(word, dictionary_data)
print(definition)

