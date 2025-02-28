from trieclass import *
wordlist = set({})
with open('/Users/Ben/Downloads/wordlist.txt', 'r') as file:# Read the file content
    words = file.read().splitlines()
    for index,word in enumerate(words):
        if len(word) > 2 and len(word)<17:
            wordlist.add(word)
word_trie = Trie()
for word in wordlist:
    word_trie.insert(word)
