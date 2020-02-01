import itertools
from collections import OrderedDict 

def split(word):
    return [char for char in word]

def wordChecker(wordList, valid_words):
    checked_words = []
    for i in range(len(wordList)):
        if valid_words.count(wordList[i]) > 0:
                checked_words.append(wordList[i])
    
    return checked_words
    
def wordLengths (wordList):
    wordLengths = []
    for i in range(len(wordList)):
        if wordLengths.count(len(wordList[i])) == 0:
            wordLengths.append(len(wordList[i]))

    return wordLengths


def load_words():
    with open('C:/Users/Will/Desktop/wordgenerator/words.txt') as word_file:
        valid_words = word_file.read().split()

    return valid_words

def generateWords(letters):
    words = []
    word = ""
    wordsize = len(letters)
    for i in range(3, wordsize+1):
        for x in itertools.permutations(letters, i):
            words.append(word.join(x))
    return list(OrderedDict.fromkeys(words))

user_input = input("Enter at least three letters to generate words: ")
number_of_letters = len(user_input)

letters = split(user_input)

words_generated = generateWords(user_input)

output_words = wordChecker(words_generated, load_words())

wordLengths = wordLengths(output_words)

for i in range(len(wordLengths)):
    print("Words of length", wordLengths[i])
    for j in range(len(output_words)):
        if len(output_words[j]) == wordLengths[i]:
            print(output_words[j])
