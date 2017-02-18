from string import punctuation
from re import split, search, sub

# Constants
VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
PUNCTUATIONS = set(punctuation)

def to_pig_latin(text):
    pig_latin_words = []
    for word in split_words(text):
        if not search('[a-zA-Z]', word):
            pig_latin_words.append(word)
            continue

        trimmed_word = trim_punctuation(word)
        if len(trimmed_word) == 0:
            pig_latin_words.append(word)
            continue

        converted_word = word.replace(trimmed_word, convert_word(trimmed_word))
        pig_latin_words.append(converted_word)

    return ''.join(pig_latin_words)

def convert_word(word):
    first_vowel_index = -1
    for i in range(len(word)):
        if word[i] in VOWELS:
            first_vowel_index = i
            break

    if first_vowel_index == -1: # If no vowel in the word
        converted_word = word + 'ay'
    elif first_vowel_index == 0: # Start with vowel
        converted_word = word + 'yay'
    else:
        converted_word = word[first_vowel_index:] + word[:first_vowel_index] + 'ay'

    return fix_title_case(converted_word, word)


def split_words(text):
    # Returns a list, which includes the whitespace delimiters.
    return split('(\s+)', text)

def trim_punctuation(word):
    # Trim punctuation from the start or end of a word.
    return word.strip(''.join(PUNCTUATIONS))

def fix_title_case(word, original_word):

    original_word = sub('[^a-zA-Z]', '', original_word)  # Remove all non-letters from the original word, e.g. We're
    if original_word.istitle():
        return word[0].upper() + word[1:].lower()
    return word

if __name__=="__main__":
    text = input('Enter a string:')
    print to_pig_latin(text)