from trieclass import *
import os

# This code runs through a list of all english words, wordlist.txt, and adds the words between 2 and 17 characters in length to a Trie.

wordlist = set({}) # makes an empty set wordList
with open(os.getcwd()+'/data/wordlist.txt', 'r') as file: # Read the file content
    words = file.read().splitlines() # Makes a list of all words
    for index,word in enumerate(words):
        if len(word) > 2 and len(word)<17:
            wordlist.add(word) # adds words with length between 2 and 17 into the wordlist set.
word_trie = Trie() # Create empty Trie
for word in wordlist:
    word_trie.insert(word) # Creates a Trie with all the words in wordlist

