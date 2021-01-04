'''
Make a program that has some sentence (a string) on input and returns a dict containing all 
unique words as keys and the number of occurrences as values. 
'''

from string import punctuation
punctuation_dict = {key: '' for (key, ) in punctuation}

def generate_unique_words_dictionary(words):
    unique_words = {}

    for item in words:
        if item not in unique_words:
            unique_words[item] = 1
        else:
            unique_words[item] += 1
    return unique_words

if __name__ == '__main__':
    user_input = input("Enter a sentence: ")
    words = user_input.translate(str.maketrans(punctuation_dict)).split()
    print(generate_unique_words_dictionary(words))