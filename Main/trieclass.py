#  Create a prefix tree data structure (Trie) from the word list that allows
#  the program to more easily identify prefixes in words and completed words.

# Node setup, starting by making an empty node.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Trie Data Structure

class Trie():
    def __init__(self):
        self.root = TrieNode()

    # When inserting a word in the Trie, you parse through the word,
    # if a letter is already a children of the root node, then move down the tree, else, create a new child node.
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Check if the given prefix is a valid prefix in the Trie. When it is, it returns True
    def has_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    # Checks if a word is in the Trie.
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word



