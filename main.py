import string

def wordcount(file_contents: str) -> int:
    return len(file_contents.split())

def char_occurences(file_contents: str) -> dict:
    chars = {}
    for character in file_contents:
        charstr = str(character).lower()
        if charstr not in chars:
            chars[charstr] = 1
        else:
            chars[charstr] += 1
    return chars

def main():
    filepath = "books/frankenstein.txt"
    with open(filepath) as f:
        file_contents = f.read()
        characters = char_occurences(file_contents)
        console_output = f"--- Begin report of {filepath} ---\n"
        console_output += f"{wordcount(file_contents)} words found in the document\n\n"

        for letter in string.ascii_lowercase:
            console_output += f"The '{letter}' character was found {characters[str(letter)]} times\n"
        console_output += "--- End report ---"
        print(console_output)
        
main()