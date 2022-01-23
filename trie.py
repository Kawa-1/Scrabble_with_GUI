from __future__ import annotations
from tile import Tile
import platform
import os

class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # points for word
        self.points = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}



class Trie(object):
    """The trie object"""

    def __init__(self):
        """
        The trie has at least the root node.
        The root node does not store any character
        """
        self.root = TrieNode("")

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True
        node.points = sum([Tile.values_of_letters.get(c) for c in word])
        # Increment the counter to indicate that we see this word once more
        # node.points = sum([Tile.values_of_letters.get(c) for c in word])

    def get_word(self, word: str) -> (str, int):

        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]

            else:
                return ("", 0)

        if node.is_end is True:
            return (word, node.points)
        #return (word, sum([Tile.values_of_letters.get(c) for c in word]))
        else:
            return ("", 0)

    def word_delete(self, word: str):

        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]

        if node.is_end is True:
            node.is_end = False

    @staticmethod
    def load_lexicon(trie: Trie):
        _platform = platform.system()
        path_of_dict = ""
        if _platform == "Windows":
            path_of_dict = "{}{}".format(os.getcwd(), "\\dict_for_game\\Collins.txt")


        elif _platform == "Darwin":
            path_of_dict = "{}{}".format(os.getcwd(), "/dict_for_game/Collins.txt")

        with open(path_of_dict, mode='r') as f:
            for word in f:
                word = word.strip('\n')
                trie.insert(word)

        return trie
