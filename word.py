import os
import numpy as np
import platform

class Word:

    @staticmethod
    def get_the_dictionary_for_words() -> dict:
        """The purpose of this method is to load words to dictionary with key of first letter
         PARAMETERS:
             None

         RETURNS:
             loaded_dictionary: dict
                It returns dict with key as a single letter and value is a list of words starting with this letter"""
        loaded_dictionary = {}
        for i in range(65, 91):
            letter = "{}".format(chr(i))
            try:
                loaded_dictionary.update({letter: np.genfromtxt(Word.get_path_for_divided(chr(i)), dtype=str)})
            except Exception as e:
                print("{}.txt doesn't exist in this directory".format(chr(i)))

        return loaded_dictionary

    @staticmethod
    def check_validity_of_word(word: str, loaded_dictionary: dict) -> bool:
        word = word.upper()
        letter = word[0]
        # print(os.getcwd())
        if word in loaded_dictionary.get(letter):
            return True

        else:
            return False

    # It is the path to the specific file depending on the first letter of the word
    @staticmethod
    def get_path_for_divided(starting_letter: str) -> str:
        # print(os.getcwd())
        _platform = platform.system()
        if _platform == "Windows":
            path_of_main_dict = "{}{}".format(os.getcwd(), "\\dict_for_game")
            return "".join([path_of_main_dict, "\\divided_dict", "\\", starting_letter, ".txt"])
        elif _platform == "Darwin":
            path_of_main_dict = "{}{}".format(os.getcwd(), "/dict_for_game")
            return "".join([path_of_main_dict, "/divided_dict", "/", starting_letter, ".txt"])
