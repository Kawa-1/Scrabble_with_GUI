from __future__ import annotations
from trie import TrieNode, Trie
from tile import Tile
from word import Word
from numpy import nditer
from string import ascii_uppercase
from collections import defaultdict
import copy
import random
import time


class BotAI:


    @staticmethod
    def ai_first_move_easy(loaded_dictionary: dict, rack: list):
        start = time.perf_counter()
        found_words = []

        words_4_score = {}

        # Choose if we are going to put oloaded_dictionaryur word vertically or in horizontally
        # 0 - horizontally; 1 - vertically
        hor_or_vert = random.randint(0, 1)

        # Let's change the order
        random.shuffle(rack)

        for letter in rack:
            if len(found_words) > 10:
                break
            dictionary_np = loaded_dictionary.get(letter)
            for word in nditer(dictionary_np):
                word = str(word)
                word_chars = list(word)
                moving_rack = copy.deepcopy(rack)
                lack_of_letter = False
                for char in word_chars:
                    if char not in moving_rack:
                        lack_of_letter = True
                        break

                    else:
                        moving_rack.remove(char)

                if lack_of_letter is False:
                    found_words.append(word)

                else:
                    continue

        choose_word = random.randint(0, len(found_words) - 1)
        choose_word = found_words[choose_word]
        length_chosen = len(choose_word)

        start_of_word = 7 - random.randint(0, length_chosen - 1)

        coords = []
        # means horizontally
        if hor_or_vert == 0:
            # adding coords of next letters
            for i in range(0, length_chosen):
                coords.append([7, start_of_word + i])

            words_4_score.update({choose_word: coords})

        else:
            # adding coords of next letters
            for i in range(0, length_chosen):
                coords.append([start_of_word + i, 7])

            words_4_score.update({choose_word: coords})

        # print(words_4_score)
        end = time.perf_counter()
        print(end - start)
        for letter in choose_word:
            rack.remove(letter)

        return True, words_4_score, rack


    @staticmethod
    def ai_first_move_hard(loaded_dictionary: dict, rack: list):
        start = time.perf_counter()
        found_words = set()

        words_4_score = {}

        # Choose if we are going to put oloaded_dictionaryur word vertically or in horizontally
        # 0 - horizontally; 1 - vertically
        hor_or_vert = random.randint(0, 1)

        # Let's change the order
        random.shuffle(rack)

        for letter in rack:
            #if len(found_words) > 10:
            #   break
            dictionary_np = loaded_dictionary.get(letter)
            # print(letter, dictionary_np)
            for word in nditer(dictionary_np):
                word = str(word)
                word_chars = list(word)
                moving_rack = copy.deepcopy(rack)
                lack_of_letter = False
                for char in word_chars:
                    if char not in moving_rack:
                        lack_of_letter = True
                        break

                    else:
                        moving_rack.remove(char)

                if lack_of_letter is False:
                    found_words.add(word)

                else:
                    continue

        print(found_words)
        choose_word = BotAI.find_best_word(found_words)
        length_chosen = len(choose_word)

        start_of_word = 7 - random.randint(0, length_chosen - 1)

        coords = []
        # means horizontally
        if hor_or_vert == 0:
            # adding coords of next letters
            for i in range(0, length_chosen):
                coords.append([7, start_of_word + i])

            words_4_score.update({choose_word: coords})

        else:
            # adding coords of next letters
            for i in range(0, length_chosen):
                coords.append([start_of_word + i, 7])

            words_4_score.update({choose_word: coords})

        # print(words_4_score)
        end = time.perf_counter()
        print(end - start)
        for letter in choose_word:
            rack.remove(letter)

        return True, words_4_score, rack

    @staticmethod
    def find_best_word(found_words: set) -> list:

        word_with_points = []

        for word in found_words:
            points = 0
            word_chars = list(word)
            for char in word_chars:
                points += Tile.values_of_letters.get(char)

            if word_with_points == []:
                word_with_points.clear()
                word_with_points.append(word)
                word_with_points.append(points)

            elif points > word_with_points[1]:
                word_with_points.clear()
                word_with_points.append(word)
                word_with_points.append(points)

            else:
                continue
        #print(word_with_points[1])
        return word_with_points[0]


    @staticmethod
    def get_anchors(board: list_of_lists) -> list_of_lists:
        """ Used to find tiles on the board which potentially may help us
                to form a new word with our tiles on the rack """

        # anchors = [[1,2],[4,5]...]
        anchors = []

        for i in range(len(board)):
            for j in range(len(board)):
                if (board[i][j] != "-"):

                    if (i + 1 < 15 and board[i + 1][j] == '-'):
                        anchors.append([i + 1, j])

                    if (i - 1 > 0 and board[i - 1][j] == '-'):
                        anchors.append([i - 1, j])

                    if (j + 1 < 15 and board[i][j + 1]) == "-":
                        anchors.append([i, j + 1])

                    if (j - 1 > 0 and board[i][j - 1] == '-'):
                        anchors.append([i, j - 1])

        return anchors


    # return: [[set(), set(), {'A', 'X', ...}, ...]]
    @staticmethod
    def get_cross_checks(t: Trie, board: list_of_lists, used_words) -> list_of_lists:
        """Possible letters for crossed words up&down"""
        def get_between_cross_checks(t: Trie, board: list_of_lists, used_words, row: int, column: int):
            """Need to get cross checks in the same dimension; case: 'M','E','-','I','C','O'; assuming that ICO as a word
                exists, the only letter which would be possible to place between 'E' and 'I' is 'X'"""
            pass

        cross_checks = [[set() for row in range(len(board))] for col in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board)):
                # Purpose of this var: To distinguish situation if allowed_letters are set() because we didn't find letter downwards or it is impossible to create word downwards
                found_downards = False

                # check downwards e.g. [X]BUS perpendicular
                if (i + 1 < 15 and board[i][j] == "-" and board[i + 1][j] != "-"):
                    found_downards = True
                    allowed_letters = set()
                    coord_tile = i + 1
                    word = ""

                    while (coord_tile < 15 and board[coord_tile][j] != "-"):
                        word += board[coord_tile][j]
                        coord_tile += 1

                    if len(word) > 0:
                        for letter in set(ascii_uppercase):
                            potential_word = letter + word

                            if t.get_word(potential_word)[0] != "" and potential_word not in used_words:
                                allowed_letters.add(letter)
                            else:
                                pass

                        # IF allowed_letters is empty, means it is impossible to create word downwards
                        if allowed_letters == set():
                            cross_checks[i][j].add("!")

                        else:
                            cross_checks[i][j] = allowed_letters

                # check upwards e.g. BUS[X] perpendicular
                if (i - 1 > - 1 and board[i][j] == "-" and board[i - 1][j] != "-" and "!" not in cross_checks[i][j]):
                    allowed_letters = set()
                    coord_tile = i - 1
                    word = ""

                    while (coord_tile > -1 and board[coord_tile][j] != "-"):
                        word += board[coord_tile][j]
                        coord_tile -= 1

                    if len(word) > 0:
                        # we need to reverse variable word as we are cheking upwards
                        word = "".join(word[::-1])
                        for letter in set(ascii_uppercase):
                            # potential_word = letter + word
                            potential_word = word + letter

                            if t.get_word(potential_word)[0] != "" and potential_word not in used_words:
                                allowed_letters.add(letter)

                            else:
                                pass

                        if "!" in cross_checks[i][j]:
                            cross_checks[i][j] = {"!"}
                        else:

                            if found_downards is True:
                                # Intersection because in previous case we were checking downwards! the same coord; Now we are checking upwards
                                cross_checks[i][j] = cross_checks[i][j] & allowed_letters
                                if cross_checks[i][j] == set():
                                    cross_checks[i][j].add("!")

                            elif found_downards is False:
                                if allowed_letters == set():
                                    cross_checks[i][j].add("!")
                                else:
                                    cross_checks[i][j] = allowed_letters

        # Check Cross-like in the same row/i : 'M','E','-','I','C','O' (assuming that ICO as a word exists...)
        for i in range(len(board)):
            for j in range(len(board)):
                if cross_checks[i][j] == {"!"}:
                    continue
                if j-1 > -1 and board[i][j - 1] != "-" and  j+1 < 15 and board[i][j + 1] != "-":
                    allowed_letters = set()
                    row = i
                    col = j
                    left_word_part = ""
                    right_word_part = ""
                    while col - 1> -1 and board[row][col - 1] != "-":
                        left_word_part += board[row][col - 1]
                        col -= 1

                    col = i
                    while col + 1 < 15 and board[row][col + 1] != "-":
                        right_word_part += board[row][col + 1]
                        col += 1

                    for letter in set(ascii_uppercase):
                        potential_word = f"{left_word_part}{letter}{right_word_part}"
                        if t.get_word(potential_word)[0] != "" and potential_word not in used_words:
                            allowed_letters.add(letter)

                    if allowed_letters == set():
                        cross_checks[i][j] == {'!'}

                    # Case cross_checks[i][j] != {'!'} was checked before
                    elif cross_checks[i][j] != set():
                        cross_checks[i][j] = cross_checks[i][j] & allowed_letters
                        if cross_checks[i][j] == set():
                            cross_checks[i][j] = {"!"}

                    else:
                        cross_checks[i][j] = allowed_letters


        return cross_checks


    @staticmethod
    def get_count_empty_left(board: list_of_lists, row: int, column: int) -> int:
        """Checking backwards how many tiles we are able to put before the anchor of an another tile on the leftside
            e.g. ---X so the result will be 3"""

        if board[row][column-1] != "-":
            return 0
        # Case where there can't be empty fields on the left to fill
        if (column == 0):
            return 0

        # (place + 1) because range is [0, x)
        for place in range(0, column + 1):
            if (board[row][column - place - 1] != "-"):
                if (place == 1 and column - place - 2 > 0):
                    return 0

                return place - 1

        return place


    @staticmethod
    def left_part(partial_word: str, node: TrieNode, limit: int, anchor_square: list, board: list_of_lists, rack,
            used_words: set, cross_checks: list(list(set())), potential_words: list):

        # The purpose of this IF is to add the letter preceeding an anchor
        if limit == 0 and board[anchor_square[0]][anchor_square[1]-1] != "-":
            letter_preceeding_anchor = board[anchor_square[0]][anchor_square[1] - 1]
            coords_of_preceeding = (anchor_square[0], anchor_square[1] - 1)
            if board[coords_of_preceeding[0]][coords_of_preceeding[1] - 1] == "-":
                BotAI.extend_right_part(board[anchor_square[0]][anchor_square[1] - 1],
                                        node.children.get(board[anchor_square[0]][anchor_square[1] - 1]),
                                        anchor_square[0], anchor_square[1],
                                        board, rack, used_words, cross_checks, potential_words)

            else:
                # Getting the word on the left from the anchor
                left_word = ''
                row = coords_of_preceeding[0]
                column = coords_of_preceeding[1]
                # i guess 'column > -1' is not necessary
                while column > - 1 and board[row][column] != '-':
                    left_word += board[row][column]
                    column -= 1

                # We need to reverse that word as we were backtracking the row
                left_word = left_word[::-1]
                # Set actual node in trie
                for char in left_word:
                    node = node.children[char]

                BotAI.extend_right_part(left_word, node, anchor_square[0], anchor_square[1], board, rack, used_words,
                                        cross_checks, potential_words)

        elif limit >= 0:
            BotAI.extend_right_part(partial_word, node, anchor_square[0], anchor_square[1], board, rack, used_words,
                              cross_checks, potential_words)

            if limit > 0:
                for letter in set(ascii_uppercase):
                    if node.children.get(letter) is not None:
                        if letter in rack:
                            rack.remove(letter)
                            BotAI.left_part(partial_word + letter, node, limit - 1, anchor_square, board, rack,
                                      used_words, cross_checks, potential_words)


    @staticmethod
    def extend_right_part(partial_word: str, node: TrieNode, row: int, column: int, board: list_of_lists, rack: list,
                          used_words: set, cross_checks: list_of_lists, potential_words: list):

        def get_coords_helper(word: str, row: int, column: int, cross_checks: list_of_lists,
                              board: list_of_lists) -> tuple_of_tuples:            # Will be changed into tuple
            """The MAIN purpose of this function is to get coords of possible crosses as well as
                get COORDS of put letters (one word)"""

            coords = []
            cross_words = []
            #put_tiles = ""

            for i in range(0, len(word)):
                column -= 1
                coords.append((row, column))
                #if board[row][column] == "-":
                #    put_tiles += partial_word[i]

                if (row - 1 > -1 and board[row - 1][column] != "-") or (row + 1 < 15 and board[row + 1][column] != "-"):
                    if cross_checks[row][column] != set() and board[row][column] == "-":
                        cross_words.append((row, column))

            return coords[::-1], cross_words[::-1]
            #return coords[::-1], cross_words[::-1], list(put_tiles)


        if row < 15 and column < 15:
            if board[row][column] == "-":
                if node.is_end is True and partial_word not in used_words:
                    # coords of word and coords where we can find crossed words
                    coords, possible_crosses = get_coords_helper(partial_word, row, column, cross_checks, board)
                    potential_words.append((partial_word, coords, possible_crosses, node.points))
                    #coords, possible_crosses, used_tiles = get_coords_helper(partial_word, row, column, cross_checks, board)
                    #potential_words.append((partial_word, coords, possible_crosses, node.points, used_tiles))

                for letter in set(ascii_uppercase):
                    if node.children.get(letter) is not None:
                        if letter in rack:
                            # check if it is possible to use this letter
                            if cross_checks[row][column] == set() or letter in cross_checks[row][column]:
                                rack.remove(letter)
                                BotAI.extend_right_part(partial_word + letter, node.children.get(letter), row, column+1, board, rack,
                                    used_words, cross_checks, potential_words)

            else:
                if node.children.get(board[row][column]) is not None:
                    BotAI.extend_right_part(partial_word + board[row][column], node.children.get(board[row][column]), row, column+1, board,
                                      rack, used_words, cross_checks, potential_words)

    def find_cross_words(tuple_word: tuple, used_words: set, board: list_of_lists, transposed: bool) -> (int, set):
        # passing everything transposed or make a logic about it && board.get_score should be implemented
        #       at returns
        # gdzieś jeszcze trzeba literki z rack'ów usuwać i pzdr do przodu done
        def swap_coords_if_trans(crossed_words: dict) -> dict:
            for key, value in crossed_words.items():
                # [10, 9] will be now [9, 10]
                swap = list(map(lambda x: x[::-1], value))
                crossed_words[key] = swap
            return crossed_words

        if transposed is True:
            board = list(zip(*board))

        if tuple_word[2] == []:
            used_words.add(tuple_word[0])
            # from board
            print("Should be handled before entering this function... And i guess it is")
            return {tuple_word[0]: tuple_word[1]}, used_words

        else:
            coords_cross_words = tuple_word[2]
            cross_words_found = {}
            new_words = []
            coords_new_words = defaultdict(list)

            for index, coord in enumerate(coords_cross_words):
                letter_crossed = ""

                for i in range(len(tuple_word[0])):
                    if tuple_word[1][i] == coord:
                        letter_crossed = tuple_word[0][i]
                        break

                # row_init - letter which has been put by AI
                if transposed is True:
                    coord[0], coord[1] = coord[1], coord[0]
                row_init = coord[0]
                row = coord[0]
                column = coord[1]

                if row - 1 > -1 and row + 1 < 15 and board[row + 1][column] != "-" and board[row - 1][column] != "-":
                    # Firstly we have to go upwards to check where is the first letter of word
                    while row - 1 > -1 and board[row - 1][column] != "-":
                        row -= 1

                    word = ""
                    # while (row + 1 < 15 and board[row + 1][column] != "-"):
                    while (row + 1 < 15 and board[row][column] != "-") or row == row_init:
                        # Valid situation when we cross letter put by us (This letter is not init on board yet)
                        if row == row_init:
                            word += letter_crossed
                            coords_new_words[index].append([row, column])
                            row += 1
                        else:
                            word += board[row][column]
                            coords_new_words[index].append([row, column])
                            row += 1

                    if word in used_words or word in cross_words_found or word == tuple_word[0]:
                        return {}

                    else:
                        cross_words_found[word] = coords_new_words[index]

                # Taking into consideration letter added at the end of the word
                elif row - 1 > -1 and board[row - 1][column] != "-":
                    while row - 1 > -1 and board[row - 1][column] != "-":
                        row -= 1

                    word = ""
                    # while row + 1 < 15 and board[row + 1][column] != "-": #UPDATE#!
                    while row < 15 and board[row][column] != "-":
                        word += board[row][column]
                        coords_new_words[index].append([row, column])
                        row += 1

                    # Situation when our word will have 2 letters only, including added one | due to the UPDATE#! it may be unnecessary
                    if len(word) == 0:
                        word += board[row][column]
                        coords_new_words[index].append([row, column])

                    word += letter_crossed
                    coords_new_words[index].append([row_init, column])

                    if word in used_words or word in cross_words_found or word == tuple_word[0]:
                        return {}

                    else:
                        cross_words_found[word] = coords_new_words[index]

                # Taking into consideration letter added at the beginning of the word
                elif row + 1 < 15 and board[row + 1][column] != "-":
                    word = letter_crossed
                    coords_new_words[index].append([row_init, column])
                    while row + 1 < 15 and board[row + 1][column] != "-":
                        row += 1
                        word += board[row][column]
                        coords_new_words[index].append([row, column])

                    if word in used_words or word in cross_words_found or word == tuple_word[0]:
                        return {}

                    else:
                        cross_words_found[word] = coords_new_words[index]

            if transposed is True:
                cross_words_found = swap_coords_if_trans(cross_words_found)
                board = list(map(lambda y: list(y), list(zip(*board))))

            return cross_words_found


    @staticmethod
    def make_hard_move(t: Trie, rack: list, board: list_of_lists, checked_words: dict) -> (bool, dict, list):
        used_words = set(checked_words)
        #used_words = {"ZEBU", "BACKUP", "PERCHED", "EAX", "EXIST", "HOTDOG", "TOGAE", "MINKE", "EAGLES", "MINIM"}
        matrix = copy.deepcopy(board)
        anchors = BotAI.get_anchors(matrix)
        cross_checks = BotAI.get_cross_checks(t, matrix, used_words)
        potential_words = []

        transposed = False
        for square in anchors:
            rack_pass = rack.copy()
            BotAI.left_part("", t.root, BotAI.get_count_empty_left(matrix, square[0], square[1]), square, matrix, rack_pass, used_words,
                      cross_checks, potential_words)

        matrix = list(zip(*matrix))
        anchors = BotAI.get_anchors(matrix)
        cross_checks = BotAI.get_cross_checks(t, matrix, used_words)

        potential_words_transposed = []
        transposed = True
        for square in anchors:
            rack_pass = rack.copy()
            BotAI.left_part("", t.root, BotAI.get_count_empty_left(matrix, square[0], square[1]), square, matrix, rack_pass, used_words,
                      cross_checks, potential_words_transposed)

        # back home; not transposed board/board
        matrix = list(map(lambda x: list(x), list(zip(*matrix))))
        transposed = False

        # INIT those vars To omit __exception__ involved with lack of words in potential...
        best_transposed = []
        best = []
        if len(potential_words) == 0 and len(potential_words_transposed) == 0:
            return False, {}, rack

        elif len(potential_words) == 0:
            best_transposed = sorted(potential_words_transposed, key=lambda x: (len(x[2]), x[3]), reverse=True)[0]
            best = [best_transposed[0], list(map(lambda y: list(y)[::-1], best_transposed[1])),
                    list(map(lambda y: list(y)[::-1], best_transposed[2])), best_transposed[3]]
            transposed = True

        elif len(potential_words_transposed) == 0:
            best = sorted(potential_words, key=lambda x: (len(x[2]), x[3]), reverse=True)[0]
            best_transposed = [0, 0, 0, 0]

        else:
            best = sorted(potential_words, key=lambda x: (len(x[2]), x[3]), reverse=True)[0]
            best_transposed = sorted(potential_words_transposed, key=lambda x: (len(x[2]), x[3]), reverse=True)[0]

        if best_transposed[3] > best[3]:
            best = [best_transposed[0], list(map(lambda y: list(y)[::-1], best_transposed[1])),
                    list(map(lambda y: list(y)[::-1], best_transposed[2])), best_transposed[3]]
            transposed = True

        print(potential_words)
        print(potential_words_transposed)
        print(best)
        print(best_transposed)

        if best[2] != []:
            crossed = BotAI.find_cross_words(tuple(best), used_words, matrix, transposed)
        else:
            # "!" means we do not count crossed words
            crossed = {"!"}

        # Rarely; it is the case when we didn't check the word which is going to be init on the board by AI
        if crossed == {} and transposed is True:
            print("AI DID WRONG MOVE!! :))))")
            matrix = list(map(lambda y: list(y), list(zip(*matrix))))
            transposed = False
            return False, {}, rack

        elif crossed == {}:
            print("ai did wrong move!! :DD")
            return False, {}, rack

        print(rack)
        for index, coords in enumerate(best[1]):
            if board[coords[0]][coords[1]] == "-":
                rack.remove(best[0][index])

        # format var best for method get_score from board module
        if crossed != {"!"}:
            best = {best[0]: best[1]}
            best.update(crossed)
        else:
            best = {best[0]: best[1]}

        # Very Rarely; If AI make wrong move involved with correctness of word
        # I think it is actually impossible because actually we are "deleting" words in the TRIE
        for word in best:
            if t.get_word(word)[0] == "":
                print("AI used word which doesn't exist :D")
                return False, {}, rack

        return True, best, rack

    @staticmethod
    def make_easy_move(t: Trie, rack: list, board: list_of_lists, checked_words: dict) -> (bool, dict, list):
        used_words = set(checked_words)
        # used_words = {"ZEBU", "BACKUP", "PERCHED", "EAX", "EXIST", "HOTDOG", "TOGAE", "MINKE", "EAGLES", "MINIM"}
        matrix = copy.deepcopy(board)
        anchors = BotAI.get_anchors(matrix)
        cross_checks = BotAI.get_cross_checks(t, matrix, used_words)
        potential_words = []

        transposed = False
        for square in anchors:
            rack_pass = rack.copy()
            BotAI.left_part("", t.root, BotAI.get_count_empty_left(matrix, square[0], square[1]), square, matrix,
                            rack_pass, used_words,
                            cross_checks, potential_words)

        matrix = list(zip(*matrix))
        anchors = BotAI.get_anchors(matrix)
        cross_checks = BotAI.get_cross_checks(t, matrix, used_words)

        potential_words_transposed = []
        transposed = True
        for square in anchors:
            rack_pass = rack.copy()
            BotAI.left_part("", t.root, BotAI.get_count_empty_left(matrix, square[0], square[1]), square, matrix,
                            rack_pass, used_words,
                            cross_checks, potential_words_transposed)

        # back home; not transposed board/matrix
        matrix = list(map(lambda x: list(x), list(zip(*matrix))))
        transposed = False

        worst_transposed = []
        worst = []
        if len(potential_words) == 0 and len(potential_words_transposed) == 0:
            return False, {}, rack

        elif len(potential_words) == 0:
            worst_transposed = sorted(potential_words_transposed, key=lambda x: (-x[3], -len(x[2])), reverse=True)[0]
            worst = [worst_transposed[0], list(map(lambda y: list(y)[::-1], worst_transposed[1])),
                    list(map(lambda y: list(y)[::-1], worst_transposed[2])), worst_transposed[3]]
            transposed = True

        elif len(potential_words_transposed) == 0:
            worst = sorted(potential_words, key=lambda x: (-x[3], -len(x[2])), reverse=True)[0]
            # Temporary solution...
            worst_transposed = [99999, 99999, 99999, 99999]

        else:
            worst = sorted(potential_words, key=lambda x: (-x[3], -len(x[2])), reverse=True)[0]
            worst_transposed = sorted(potential_words_transposed, key=lambda x: (len(x[2]), x[3]), reverse=True)[0]

        worst = sorted(potential_words, key=lambda x: (-x[3], -len(x[2])), reverse=True)[0]
        worst_transposed = sorted(potential_words_transposed, key=lambda x: (-x[3], -len(x[2])), reverse=True)[0]

        if worst_transposed[3] < worst[3]:
            worst = [worst_transposed[0], list(map(lambda y: list(y)[::-1], worst_transposed[1])),
                    list(map(lambda y: list(y)[::-1], worst_transposed[2])), worst_transposed[3]]
            transposed = True

        if worst[2] != []:
            crossed = BotAI.find_cross_words(tuple(worst), used_words, matrix, transposed)
        else:
            # "!" means we do not count crossed words | lack of them
            crossed = {"!"}

        # Rarely; it is the case when we didn't check the word which is going to be init on the board by AI
        if crossed == {} and transposed is True:
            print("AI DID WRONG MOVE!! :))))")
            matrix = list(map(lambda y: list(y), list(zip(*matrix))))
            transposed = False
            return False, {}, rack

        elif crossed == {}:
            print("ai did wrong move!! :DD")
            return False, {}, rack

        print(rack)
        for index, coords in enumerate(worst[1]):
            if board[coords[0]][coords[1]] == "-":
                rack.remove(worst[0][index])

        # format var worst for method get_score from board module
        if crossed != {"!"}:
            worst = {worst[0]: worst[1]}
            worst.update(crossed)
        else:
            worst = {worst[0]: worst[1]}

        # Rarely; If AI make wrong move involved with correctness of word
        for word in worst:
            if t.get_word(word)[0] == "":
                print("AI used word which doesn't exist :D")
                return False, {}, rack

        print(worst)
        return True, worst, rack

if __name__ == "__main__":
    t = Trie()
    with open("dict_for_game\\Collins.txt", mode='r') as f:
        for word in f:
            word = word.strip('\n')
            t.insert(word)

    board = [['-', '-', '-', '-', 'Z', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', 'E', '-', '-', '-', '-', '-', 'M', 'I', 'N', 'I', 'M'],
              ['-', '-', '-', '-', 'B', '-', '-', '-', '-', '-', 'I', '-', '-', '-', '-'],
              ['B', 'A', 'C', 'K', 'U', 'P', '-', 'E', 'V', 'E', 'N', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', 'E', 'A', 'X', '-', '-', 'K', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', 'R', '-', 'I', '-', '-', 'E', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', 'C', '-', 'S', '-', 'T', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', 'H', 'O', 'T', 'D', 'O', 'G', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', 'E', '-', '-', '-', 'G', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', 'D', '-', '-', '-', 'A', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', 'E', 'A', 'G', 'L', 'E', 'S'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

    rack = ["A", "O", "B", "P", "K", "U", "M", "Z"]

    print(BotAI.make_best_move(t, rack, board, {}))
