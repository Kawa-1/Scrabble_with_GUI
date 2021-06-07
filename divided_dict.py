import os

# Dictionary will be divided on .txt files which names will start from letter
# Of the word like: A.txt, B.txt... It will somehow optimize our research during the game
# Main OS was Windows during creating this game

# It may be used in future
def get_raw_bytes(passed_word: str) -> str:
    """Getting the raw bytes of string"""

    return r"{}".format(passed_word)

# Getting the path to create new .txt file with the name of individual letters
# UPDATE: actually just gettin the path
def get_path_for_divided(starting_letter) -> str:
    return "".join([path_of_main_dict, "\\divided_dict", "\\", starting_letter, ".txt"])

# Getting the path of our script
path_of_script = os.getcwd()

# This the path where our divided dictionary will be placed
path_of_divided_dict = "{}{}".format(path_of_script, "\\dict_for_game\\divided_dict")

# Path of dictionary which we are going divide into smaller .txt files
path_of_main_dict = "{}{}".format(os.getcwd(), "\\dict_for_game")

# If our folder doesn't exist... We just create it
if not os.path.exists(path_of_divided_dict):
    os.makedirs(path_of_divided_dict)

# Just defining the var which will be used during creating new .txt files
possible_starting_letter = tuple(map(lambda letter: chr(letter), [*range(65, 91)]))

# creating .txt files from our main dict which look like: A.txt, B.txt, etc.
if not os.listdir("".join([path_of_main_dict, "\\divided_dict"])):
    for index, letter in enumerate(possible_starting_letter):
        new_file = open(get_path_for_divided(letter), mode='w')
        new_file.close()

# Opening our main dict
with open(path_of_main_dict + "\\Collins.txt", mode='r') as reader:
    letter = possible_starting_letter[0]
    file_append = open(get_path_for_divided(letter), mode='a+')
    for line in reader:
        if line[0] == letter:
            file_append.write(line)

        else:
            file_append.close()
            # Another file to fill... A -> B -> C...
            file_append = open(get_path_for_divided(line[0]), mode='a+')
            file_append.write(line)

    file_append.close()
