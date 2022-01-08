from __future__ import annotations
from itertools import chain
from word import Word
from collections import defaultdict
from player import Player
from tile import Tile
import copy



class Board:
    """This class implements all logic what happens on the board during the game"""

    # Standard ROW x COLUMNS scrabble's board. It is square.
    size_board = 15

    values_of_letters = Tile.values_of_letters

    def __init__(self):
        # "-" means empty field on the board
        self.actual_board = [['-' for i in range(Board.size_board)] for j in range(Board.size_board)]
        self.round = 1
        # "WORD": [[X,Y],[X1,Y1]...[X3,Y3]]
        self.checked_words = {}
        # It storages the possibilities of placing letters on the board \
        # 0 - not connected cell, 1 - Available cell to start a word, 2 - letter on board
        self.board_of_numbers = [[0 for i in range(15)] for j in range(15)]

        self.triple_word_score = [[0, 0], [7, 0], [14, 0], [0, 7], [14, 7], [0, 14], [7, 14], [14, 14]]

        self.double_word_score = [[1, 1], [2, 2], [3, 3], [4, 4], [1, 13], [2, 12], [3, 11], [4, 10], [13, 1],
                                  [12, 2], [11, 3], [10, 4], [13, 13], [12, 12], [11, 11], [10, 10]]

        self.triple_letter_score = [[1, 5], [1, 9], [5, 1], [5, 5], [5, 9], [5, 13], [9, 1], [9, 5],
                                    [9, 9], [9, 13], [13, 5], [13, 9]]

        self.double_letter_score = [
            [0, 3], [0, 11], [2, 6], [2, 8], [3, 0], [3, 7], [3, 14], [6, 2], [6, 6], [6, 8], [6, 12], [7, 3], [7, 11],
            [8, 2], [8, 6], [8, 8], [8, 12], [11, 0], [11, 7], [11, 14], [12, 6], [12, 8], [14, 3], [14, 11]]

    def get_copy_of_board(self) -> list_of_lists:
        """"""
        copy_board = copy.deepcopy(self.actual_board)
        return copy_board

    def remove_special_place_board(self, coords: list, type_of_bonus: list_of_lists) -> noReturn:
        type_of_bonus.remove(coords)

    # words_4_score = {"WORD": [[1,1],[1,2],[1,3],[1,4]], ...}
    def get_score(self, words_4_score: dict, copy_board: list_of_lists) -> int:
        total_score_round = 0

        for word in words_4_score:
            dws = False
            tws = False
            score_of_word = 0
            letters_of_word = [char for char in word]
            coords = words_4_score.get(word)
            # Here we iterate the coords
            for index, place in enumerate(coords):
                if place in self.double_letter_score:
                    score_of_word += self.values_of_letters.get(letters_of_word[index]) * 2
                    self.remove_special_place_board(place, self.double_letter_score)

                elif place in self.triple_letter_score:
                    score_of_word += self.values_of_letters.get(letters_of_word[index]) * 3
                    self.remove_special_place_board(place, self.triple_letter_score)

                elif place in self.double_word_score:
                    score_of_word += self.values_of_letters.get(letters_of_word[index])
                    dws = True
                    self.remove_special_place_board(place, self.double_word_score)

                elif place in self.triple_word_score:
                    score_of_word += self.values_of_letters.get(letters_of_word[index])
                    tws = True
                    self.remove_special_place_board(place, self.triple_word_score)

                else:
                    score_of_word += self.values_of_letters.get(letters_of_word[index])

            if dws is True:
                total_score_round += score_of_word * 2

            elif tws is True:
                total_score_round += score_of_word * 3

            else:
                total_score_round += score_of_word

        return total_score_round

    def place_letters(self, letters_put_by_player: list, coordinates: list_of_lists,
                      copy_board: list_of_lists) -> defaultdict(list):
        letter_coordinates = defaultdict(list)
        for index, letter in enumerate(letters_put_by_player):
            # index - Which in order coords of which letter, [0] - row , [1] - column \
            # and here we are initializing letters for our copy board
            copy_board[coordinates[index][0]][coordinates[index][1]] = letter
            letter_coordinates[letter].append(coordinates[index])

        return letter_coordinates


    def first_move(self, first_letters: list_of_lists, copy_board: list_of_lists, loaded_dictionary: dict) -> (
            bool, dict):

        if not [7, 7] in first_letters:
            return False, {}

        word_4_score = {}
        columns = list(zip(*copy_board))
        column_8th = columns[7]

        row_8th = copy_board[7]

        aux = False
        first_word = ""
        # False means we have not got, True means we have got our potential word on board \
        # with correct placement if we consider rules of first move in scrabble
        we_have_potential_word = False
        # Check 8th row
        for index, cell in enumerate(row_8th):
            # We enter this loop only once
            if cell != "-" and aux is False:
                # Coords of potential first word put on board
                potential_first_word = index
                first_word += row_8th[potential_first_word]
                while potential_first_word < 14:
                    # We have checked before if [7,7] is taken... So it can turn out that first word is put vertiacally
                    # but still we have to check if there is no other tiles in 8th row
                    if row_8th[potential_first_word + 1] == "-" and potential_first_word + 1 < 7:
                        # Letter is not connected with [7,7]
                        return False, {}

                    # We add another letter to the letter which has been found before and they are \
                    # continuous with each other on the 8th row
                    elif row_8th[potential_first_word + 1] != "-" and row_8th[potential_first_word] != "-":
                        first_word += row_8th[potential_first_word + 1]
                        potential_first_word += 1

                    elif row_8th[potential_first_word + 1] == "-" \
                            and len(first_word) >= 2 and we_have_potential_word is False:
                        # But still we have to check the rest of row...
                        we_have_potential_word = True
                        potential_first_word += 1
                        # So in next loops we are going to check if there are redundant tiles...

                    elif row_8th[potential_first_word + 1] != "-" and we_have_potential_word is True:
                        return False, {}

                    else:
                        potential_first_word += 1
                        if potential_first_word == 14:
                            aux = True

            elif cell == "-" and aux is True:
                break

        aux = False
        if we_have_potential_word is False:
            first_word = ""
            for index, cell in enumerate(column_8th):
                if cell != "-" and aux is False:
                    # Coords of potential first word put on board
                    potential_first_word = index
                    first_word += column_8th[potential_first_word]
                    while potential_first_word < 14:
                        # We have checked before if [7,7] is taken... So probably first word is put vertiacally \
                        # but still we have to check if there is no other tiles in 8th row
                        if column_8th[potential_first_word + 1] == "-" and potential_first_word + 1 < 7:
                            # Letter is not connected with [7,7]
                            return False, {}

                        # We add another letter to the letter which has been found before and they are \
                        # continuous with each other on the 8th row
                        elif column_8th[potential_first_word + 1] != "-" and column_8th[potential_first_word] != "-":
                            first_word += column_8th[potential_first_word + 1]
                            potential_first_word += 1

                        elif column_8th[potential_first_word + 1] == "-" \
                                and len(first_word) >= 2 and we_have_potential_word is False:
                            # But still we have to check the rest of row...
                            we_have_potential_word = True
                            potential_first_word += 1
                            # So in next loops we are going to check if there are redundant tiles...


                        elif column_8th[potential_first_word + 1] != "-" and we_have_potential_word is True:
                            return False, {}

                        else:
                            potential_first_word += 1
                            if potential_first_word == 14:
                                aux = True

                # Było elif cell != "-" and aux is True
                elif cell == "-" and aux is True:
                    break
        else:
            for index, cell in enumerate(column_8th):
                if cell != "-" and index != 7:
                    # inappropriately put letter on board
                    return False, {}

        # Check if we have got somewehre else a tile in spite of 8th row and 8th column
        for index_row in range(len(copy_board)):
            if index_row == 7:
                continue
            else:
                for index_column, cell in enumerate(copy_board[index_row]):
                    if index_column == 7:
                        continue
                    else:
                        if cell != "-":
                            # Because we can only put one word during the first move of first round...
                            return False, {}

        # Now we are checking correctness of the word
        correctness_of_word = Word.check_validity_of_word(first_word, loaded_dictionary)

        if correctness_of_word is True:

            # optional dk if it will work fine UPDATE: IT WORKS FINE 29.05.2021
            self.checked_words.update({first_word: first_letters})
            word_4_score.update({first_word: first_letters})
            return True, word_4_score

        else:
            return False, {}

    def create_sum_board_4_connection(self) -> noReturn:
        """
        2 - letter already accepted on the board
        1 - for future placement of letter
        0 - cell without connection
        """
        possible_moves_ones = ((-1, 0), (1, 0), (0, 1), (0, -1))

        # Setting ones
        for i in range(len(self.actual_board)):
            for j in range(len(self.actual_board)):

                if self.actual_board[i][j] != "-":

                    # Setting ones around letter
                    for cell in possible_moves_ones:

                        try:

                            self.board_of_numbers[i + cell[0]][j + cell[1]] = 1

                        except Exception as e:
                            print('Out of bound but dont worry this error has been handled :-) And we are still in:-)',
                                  e, i + cell[0], j + cell[1])

        # Setting 2 in place of letter
        for i in range(len(self.actual_board)):
            for j in range(len(self.actual_board)):

                if self.actual_board[i][j] != "-":
                    self.board_of_numbers[i][j] = 2

    # First in the use must be setting ones and twos
    def check_validity_placement_rows(self, copy_board: list_of_lists) -> bool:
        new_words = []
        buffer_word = ""
        row_col_buff = []
        # checking rows
        for i in range(len(copy_board)):
            for j in range(len(copy_board)):

                if j != 14:
                    # potential word
                    if copy_board[i][j] != "-" and len(buffer_word) == 0:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])

                    elif copy_board[i][j] != "-" and len(buffer_word) != 0:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])

                    elif copy_board[i][j] == "-" and len(buffer_word) == 1:
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    else:
                        continue

                else:

                    if copy_board[i][j] == "-" and len(buffer_word) <= 1:
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] != "-" and len(buffer_word) >= 1:
                        buffer_word += copy_board[i][j]
                        row_col_buff.append([self.board_of_numbers[i][j]])
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    elif copy_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, row_col_buff])
                        buffer_word = ""
                        row_col_buff = []

                    else:
                        buffer_word = ""
                        row_col_buff = []
                        # End of inside loop

        words_checked = list(self.checked_words.keys())
        for word in new_words:

            # word[1] looks like [[1],[0],[0],[1]]
            ones = [one[0] for one in word[1] if one[0] == 1]
            twos = [two[0] for two in word[1] if two[0] == 2]

            if word[0] not in words_checked:

                if len(ones) > 0:
                    print("There is at least one '1', ", word[0])

                elif len(twos) == len(word[0]):
                    print("Word has been already accepted, ", word[0])

                else:
                    print("So... Where is at least one '1' from sum_board?", word[0])
                    return False

        return True

    # This function is the copy of function above
    def check_validity_placement_columns(self, copy_board: list_of_lists) -> bool:

        # We tranpose our matrix rows to columns and columns to rows
        columns_board = list(zip(*copy_board))

        new_words = []
        buffer_word = ""
        sum_buff = []

        # i means column, j means row
        for i in range(len(columns_board)):
            for j in range(len(columns_board)):

                if j != 14:

                    if columns_board[i][j] != "-" and len(buffer_word) == 0:
                        buffer_word += columns_board[i][j]
                        sum_buff.append([self.board_of_numbers[j][i]])

                    elif columns_board[i][j] != "-" and len(buffer_word) != 0:
                        buffer_word += columns_board[i][j]
                        sum_buff.append([self.board_of_numbers[j][i]])

                    elif columns_board[i][j] == "-" and len(buffer_word) == 1:
                        buffer_word = ""
                        sum_buff = []

                    elif columns_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, sum_buff])
                        buffer_word = ""
                        sum_buff = []

                    else:
                        continue

                else:

                    if columns_board[i][j] == "-" and len(buffer_word) <= 1:
                        buffer_word = ""
                        sum_buff = []

                    elif columns_board[i][j] != "-" and len(buffer_word) >= 1:
                        buffer_word += columns_board[i][j]
                        sum_buff.append([self.board_of_numbers[j][i]])
                        new_words.append([buffer_word, sum_buff])
                        buffer_word = ""
                        sum_buff = []

                    elif columns_board[i][j] == "-" and len(buffer_word) > 1:
                        new_words.append([buffer_word, sum_buff])
                        buffer_word = ""
                        sum_buff = []

                    else:
                        buffer_word = ""
                        sum_buff = []
                        # End of inside loop

        # To check if actually put letters are in correct place
        words_checked = list(self.checked_words.keys())
        for word in new_words:
            ones = [one[0] for one in word[1] if one[0] == 1]
            twos = [two[0] for two in word[1] if two[0] == 2]

            if word[0] not in words_checked:

                if len(ones) > 0:
                    print("There is at least one '1', ", word[0])

                elif len(twos) == len(word[0]):
                    print("Word has been already accepted, ", word[0])

                else:
                    print("So... Where is at least one '1' from sum_board?", word[0])
                    return False

        return True

    # Ewentualnie mozemy zmodyfikować to pod kopie board'u
    def check_words_from_board(self, loaded_dictionary: dict, copy_board: list_of_lists) -> (bool, dict):
        # This dict holds new words put on board with their coordinates
        words_4_score = {}
        # list which holds new words put on board
        this_round_words = []
        # Transpose of our matrix
        count_words = []
        columns = list(zip(*copy_board))
        # check rows
        for index_row, row in enumerate(copy_board):
            word_buffer = ""
            word_coords_buffer = []
            i_column = 0
            while i_column < 14:
                word_buffer = ""
                word_coords_buffer = []
                if row[i_column] != '-' and row[i_column + 1] != '-':
                    while row[i_column] != '-':
                        word_buffer += row[i_column]
                        word_coords_buffer.append([index_row, i_column])
                        if i_column != 14:
                            i_column += 1
                        else:
                            break

                    if word_buffer not in self.checked_words.keys() and \
                            Word().check_validity_of_word(word_buffer, loaded_dictionary) is True:
                        # {WORD: [[[1,2],[3,4]]],...} len(WORD) == 1; len(WORD)[0] == 2;
                        self.checked_words.update({word_buffer: word_coords_buffer})
                        words_4_score.update({word_buffer: word_coords_buffer})
                        this_round_words.append(word_buffer)
                        print("Dodaje do checked_words ", word_buffer)


                    elif word_buffer in this_round_words and word_buffer in self.checked_words.keys():
                        print("Te słowo już było zagrane przez innego gracza ", word_buffer)
                        for word in this_round_words:
                            self.checked_words.pop(word)
                        return False, {}


                    elif word_buffer in this_round_words:
                        print("Nie można zagrać dwóch tych samych słów w jednej rundzie ", word_buffer)
                        for word in this_round_words:
                            self.checked_words.pop(word)
                        return False, {}

                    elif word_buffer in self.checked_words.keys():
                        print("Było już sprawdzone ", word_buffer)
                        # Te linie zostały dodane w przypadku gdy dodamy drugie takie same słowo, ale i nowe dobre
                        # screen tej sytuacji u mnie(Kamil) na pulpicie
                        if word_buffer not in count_words:
                            count_words.append(word_buffer)
                        else:
                            for word in this_round_words:
                                self.checked_words.pop(word)
                            return False, {}

                    else:
                        print("The word hasn't been found in dictionary ", word_buffer)
                        for word in this_round_words:
                            self.checked_words.pop(word)
                        return False, {}

                else:
                    i_column += 1

        for index_column, column in enumerate(columns):
            word_buffer = ""
            word_coords_buffer = []
            i_row = 0
            while i_row < 14:
                word_buffer = ""
                word_coords_buffer = []
                if column[i_row] != '-' and column[i_row + 1] != '-':
                    while column[i_row] != '-':
                        word_buffer += column[i_row]
                        word_coords_buffer.append([i_row, index_column])
                        if i_row != 14:
                            i_row += 1
                        else:
                            break

                    if word_buffer not in self.checked_words.keys() and \
                            Word().check_validity_of_word(word_buffer, loaded_dictionary) == True:
                        print("Dodaje do checked_words...: ", word_buffer)
                        self.checked_words.update({word_buffer: word_coords_buffer})
                        words_4_score.update({word_buffer: word_coords_buffer})
                        this_round_words.append(word_buffer)

                    elif word_buffer in this_round_words and word_buffer in self.checked_words.keys():
                        print("Te słowo już było zagrane przez innego gracza ", word_buffer)
                        for word in this_round_words:
                            self.checked_words.pop(word)
                        return False, {}

                    elif word_buffer in this_round_words:
                        print("Nie można zagrać dwóch tych samych słów w jednej rundzie ", word_buffer)
                        for word in this_round_words:
                            self.checked_words.pop(word)
                        return False, {}


                    elif word_buffer in self.checked_words.keys():
                        print("Było już sprawdzone ", word_buffer)
                        if word_buffer not in count_words:
                            count_words.append(word_buffer)
                        else:
                            for word in this_round_words:
                                print("Pop i false ", word_buffer)
                                self.checked_words.pop(word)
                            return False, {}

                    else:
                        print("The word hasn't been found in dictionary ", word_buffer)
                        for word in this_round_words:
                            self.checked_words.pop(word)
                        return False, {}
                else:
                    i_row += 1

        if words_4_score != {}:
            return True, words_4_score
        else:
            for word in this_round_words:
                self.checked_words.pop(word)
                print("Weszliśmy do pętli gdzie usuwamy slowa uzyte, dodane, ale jednak nie zatwierdzone")

            return False, {}
