from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

from auxiliary.gui_base_methods import board_to_string, string_to_board
from word import Word
from board import Board
from collections import defaultdict
from bag import Bag
from racks import Racks
from player import Player
from end_turn_pop import Ui_Form6
from leaderboard_pop import Ui_Form5
from kick_player import Ui_Form7
import game_over
from management_database import ManagementGeneralLeaderboard
from help import Ui_Form9
from gui_py_source.board_window import Ui_board_window

from trie import Trie, TrieNode
from bot_AI import BotAI


class Board_gui(QtWidgets.QMainWindow):
    def __init__(self, aux_number_of_players, aux_players, menu):
        self.number_of_players = aux_number_of_players
        self.players = aux_players
        self.which_move = 1
        self.change_letters_check = 0
        self.menu_handle = menu

        # register current game in db; [1] -> index, [0] -> status
        _players2str = ','.join([player.name for player in self.players])
        self.game_id = ManagementGeneralLeaderboard.register_game(_players2str)[1]

        # init gui of scrabble board
        QtWidgets.QMainWindow.__init__(self)
        # call constructor of board_window class
        self.ui = Ui_board_window()
        self.ui.setupUi(self)

        self.show()

        self.buttons_to_change = {}
        self.number_buttons_to_change = 0
        self.dict_board_labels = {}
        self.players_sorted = []

        self.valid_move = False
        self.validity_rows_check = False
        self.validity_columns_check = False
        self.pass_first_move_check = 0
        self.current_player = 0
        self.dict_players = {}
        self.new_letter = 0
        self.check_if_player_kicked = False
        self.number_players_start = self.number_of_players
        self.check_game_over = False
        self.moves_count = 0

        self.letters_used = []
        self.coords_of_letters_used = []
        self.loaded_dictionary = Word.get_the_dictionary_for_words()
        print(self.loaded_dictionary)

        # AI LEXICON !!!!!! Trie Data Structure & rack_AI
        self.t = Trie()
        self.t = Trie.load_lexicon(self.t)
        self.rack_AI = []

        self.managment_db = ManagementGeneralLeaderboard()
        self.board = Board()
        self.racks = Racks()
        self.letter_coordinates_dict = defaultdict(list)

        self.letter_to_board = ""

        self.players_to_db = {}  # do zrobienia na end game

        self.pushButton1_check = 0
        self.pushButton2_check = 0
        self.pushButton3_check = 0
        self.pushButton4_check = 0
        self.pushButton5_check = 0
        self.pushButton6_check = 0
        self.pushButton7_check = 0

        self.pushButton1_used = 0
        self.pushButton2_used = 0
        self.pushButton3_used = 0
        self.pushButton4_used = 0
        self.pushButton5_used = 0
        self.pushButton6_used = 0
        self.pushButton7_used = 0

        for i in range(self.number_of_players):
            self.dict_players[i] = self.racks.bag.generate_rack_for_player()
            self.players[i].rack = self.dict_players[i]
            print("XDDD-", self.players[i].rack)
            self.dict_players[i].append(self.players[i].name)
            self.dict_players[i].append(self.players[i].score)
            self.dict_players[i].append(self.players[i].fails)
            #self.dict_players[i].append(self.players[i].swapped)


        # self.letter_list = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D',
        #                     'D', 'D', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'F', 'F', 'G', 'G', 'G',
        #                     'H', 'H', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'J', 'K', 'L', 'L', 'L', 'L', 'M', 'M',
        #                     'N', 'N', 'N', 'N', 'N', 'N', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'P', 'P', 'Q', 'R', 'R',
        #                     'R', 'R', 'R', 'R', 'S', 'S', 'S', 'S', 'T', 'T', 'T', 'T', 'T', 'T', 'U', 'U', 'U', 'U', 'V',
        #                     'V', 'W', 'W', 'X', 'Y', 'Y', 'Z']
        # random.shuffle(self.letter_list)
        # self.random_number = 0

        # self.dict_players = {}

        # for i in range(self.number_of_players):
        #     self.dict_players[i] = []
        #     for j in range(7):
        #         self.random_number = random.randint(0, len(self.letter_list)-1)
        #         self.dict_players[i].append(self.letter_list[self.random_number])
        #         self.letter_list.pop(self.random_number)
        #     self.dict_players[i].append(self.players_names[i])
        #     self.dict_players[i].append(0)

        print(self.dict_players)
        #  CONNECT METHODS TO OBJECTS OF GUI
        self.ui.leaderboardButton.clicked.connect(self.clicked_leaderboard)
        self.ui.helpButton.clicked.connect(self.clicked_help)
        self.ui.clear.clicked.connect(self.clicked_clear)
        self.ui.confirm.clicked.connect(self.clicked_confirm)
        self.ui.confirm.clicked.connect(self.safe_words)
        self.ui.confirm.clicked.connect(self.check_to_kick_player)
        self.ui.confirm.clicked.connect(self.change_player)
        self.ui.change_letters.clicked.connect(self.clicked_change_letters)
        self.ui.change_letters.clicked.connect(self.clicked_clear)
        self.ui.change_letters_confirm.clicked.connect(self.clicked_change_letters_confirm)
        self.ui.change_letters_cancel.clicked.connect(self.clicked_change_letters_cancel)
        self.ui.pushButton1.clicked.connect(self.clicked_pushButton1)
        self.ui.pushButton2.clicked.connect(self.clicked_pushButton2)
        self.ui.pushButton3.clicked.connect(self.clicked_pushButton3)
        self.ui.pushButton4.clicked.connect(self.clicked_pushButton4)
        self.ui.pushButton5.clicked.connect(self.clicked_pushButton5)
        self.ui.pushButton6.clicked.connect(self.clicked_pushButton6)
        self.ui.pushButton7.clicked.connect(self.clicked_pushButton7)

        # SETTING TXT TO LABELS, BTNS
        self.ui.player_name.setText(self.dict_players[0][7])
        self.ui.how_many_points.setText(str(self.dict_players[0][8]))

        self.ui.pushButton1.setText(self.dict_players[0][0])
        self.ui.pushButton2.setText(self.dict_players[0][1])
        self.ui.pushButton3.setText(self.dict_players[0][2])
        self.ui.pushButton4.setText(self.dict_players[0][3])
        self.ui.pushButton5.setText(self.dict_players[0][4])
        self.ui.pushButton6.setText(self.dict_players[0][5])
        self.ui.pushButton7.setText(self.dict_players[0][6])

        self.ui.number_of_letters.setText(str(self.racks.bag.get_size_of_bag()))

        self.actual_board = [['-' for i in range(15)] for j in range(15)]
        self.new_player_move_board = [
            ['-' for i in range(15)] for j in range(15)]
        self.check_in_which_move = [[0 for i in range(15)] for j in range(15)]
        self.board_labels = [[0 for i in range(15)] for j in range(15)]


        for i in range(self.number_of_players):
            self.players_sorted.append([self.dict_players[i][7], self.dict_players[i][8]])

        self.players_sorted.sort(key=lambda x: x[1])

        for i in range(15):
            for j in range(15):
                self.dict_board_labels[eval("self.ui.board_label_" + str(i) + "_" + str(j))] = \
                    [eval("self.ui.board_label_" + str(i) + "_" + str(j)).text(),
                     eval("self.ui.board_label_" + str(i) + "_" + str(j)).styleSheet(), i, j]

        for label in self.dict_board_labels:
            label.mousePressEvent = self.factory(
                label, self.dict_board_labels[label][2], self.dict_board_labels[label][3])
            print(label, self.dict_board_labels[label][2], self.dict_board_labels[label][3])


    def factory(self, label, i, j):
        def clicked_label(event):
            if self.change_letters_check == 0:
                if self.letter_to_board != "":
                    if label.styleSheet() != 'background-color:lightyellow':
                        label.setStyleSheet('background-color:lightyellow; color: black')
                        label.setText(self.letter_to_board)
                        label.setEnabled(False)
                        self.new_player_move_board[i][j] = self.letter_to_board
                        self.check_in_which_move[i][j] = self.which_move

                        self.letters_used.append(self.letter_to_board)

                        self.coords_of_letters_used.append([i, j])

                        if self.pushButton1_check == 1:
                            self.pushButton1_used = 1
                            self.ui.pushButton1.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton1_check = 0

                        if self.pushButton2_check == 1:
                            self.pushButton2_used = 1
                            self.ui.pushButton2.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton2_check = 0

                        if self.pushButton3_check == 1:
                            self.pushButton3_used = 1
                            self.ui.pushButton3.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton3_check = 0

                        if self.pushButton4_check == 1:
                            self.pushButton4_used = 1
                            self.ui.pushButton4.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton4_check = 0

                        if self.pushButton5_check == 1:
                            self.pushButton5_used = 1
                            self.ui.pushButton5.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton5_check = 0

                        if self.pushButton6_check == 1:
                            self.pushButton6_used = 1
                            self.ui.pushButton6.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton6_check = 0

                        if self.pushButton7_check == 1:
                            self.pushButton7_used = 1
                            self.ui.pushButton7.setStyleSheet('background-color:orange')
                            self.letter_to_board = ""
                            self.pushButton7_check = 0

        return clicked_label

    def ai_place_letter(self, word: str, coords: list) -> None:
        _letters = list(word)
        for index, _tile in enumerate(coords):
            _label = eval("self.ui.board_label_" + str(_tile[0]) + "_" + str(_tile[1]))
            if _label.styleSheet() != 'background-color:lightyellow':
                _label.setStyleSheet('background-color:lightyellow; color: black')
                _label.setText(_letters[index])
                self.new_player_move_board[_tile[0]][_tile[1]] = _letters[index]
                self.check_in_which_move[_tile[0]][_tile[1]] = _letters[index]
                _label.setEnabled(False)

            self.letters_used.append(_letters[index])
            self.coords_of_letters_used.append([_tile[0], _tile[1]])

    def clicked_confirm(self):
        words_4_score = {}
        if (self.which_move == 1 or self.pass_first_move_check == 0) and self.players[self.current_player].bot is True:
            if self.players[self.current_player].difficulty == "HARD":
                print("Clicked Confirm 243", self.players[self.current_player].rack)
                self.players[self.current_player].rack = self.players[self.current_player].rack[:7]
                print(self.players[self.current_player])
                print(type(self.loaded_dictionary))
                self.valid_move, words_4_score, self.rack_AI = BotAI.ai_first_move_hard(self.loaded_dictionary,
                                                                                   self.players[self.current_player].rack)
                if self.valid_move is True:
                    self.pass_first_move_check = 1
                    #word_letters = ""
                    #coords = []
                    # 0 - word, 1 - coords
                    for word_and_coords in words_4_score.items():
                        self.letter_coordinates_dict = self.board.place_letters(word_and_coords[0], word_and_coords[1],
                                                                                self.new_player_move_board)
                        print(word_and_coords[0], word_and_coords[1])
                        self.ai_place_letter(word_and_coords[0], word_and_coords[1])
                        self.board.checked_words.update({word_and_coords[0]: word_and_coords[1]})

            elif self.players[self.current_player].difficulty == "EASY":
                self.players[self.current_player].rack = self.players[self.current_player].rack[:7]
                self.valid_move, words_4_score, self.rack_AI = BotAI.ai_first_move_easy(self.loaded_dictionary,
                                                                                        self.players[
                                                                                            self.current_player].rack)

                if self.valid_move is True:
                    self.pass_first_move_check = 1
                    for word_and_coords in words_4_score.items():
                        self.letter_coordinates_dict = self.board.place_letters(word_and_coords[0], word_and_coords[1],
                                                                                self.new_player_move_board)
                        print(word_and_coords[0], word_and_coords[1])
                        self.ai_place_letter(word_and_coords[0], word_and_coords[1])
                        self.board.checked_words.update({word_and_coords[0]: word_and_coords[1]})



        elif (self.which_move == 1 or self.pass_first_move_check == 0):
            self.letter_coordinates_dict = self.board.place_letters(self.letters_used, self.coords_of_letters_used, self.new_player_move_board)
            self.valid_move, words_4_score = self.board.first_move(self.coords_of_letters_used, self.new_player_move_board, self.loaded_dictionary)
            if self.valid_move is True:
                self.pass_first_move_check = 1

        # Here somewhere should be check if player is bot or not
        #elif self.players[self.current_player].bot is False:
        # WORKFLOW for AI
        elif self.players[self.current_player].bot is True and self.pass_first_move_check == 1:
            if self.players[self.current_player].difficulty == "HARD":
                print("After first_move WORKFLOW AI")
                self.players[self.current_player].rack = self.players[self.current_player].rack[:7]
                self.valid_move, words_4_score, self.rack_AI = BotAI.make_hard_move(self.t,
                            self.players[self.current_player].rack, self.new_player_move_board, self.board.checked_words)
                print("WORDS_4_SCORE_AI", words_4_score)

            elif self.players[self.current_player].difficulty == "EASY":
                self.players[self.current_player].rack = self.players[self.current_player].rack[:7]
                self.valid_move, words_4_score, self.rack_AI = BotAI.make_easy_move(self.t,
                          self.players[self.current_player].rack, self.new_player_move_board, self.board.checked_words)



        else:
            # It is the normal workflow for player /not/ AI!!!
            self.letter_coordinates_dict = self.board.place_letters(self.letters_used, self.coords_of_letters_used, self.new_player_move_board)
            self.validity_rows_check = self.board.check_validity_placement_rows(self.new_player_move_board)
            self.validity_columns_check = self.board.check_validity_placement_columns(self.new_player_move_board)

            if self.validity_rows_check is True and self.validity_columns_check is True:
                self.valid_move, words_4_score = self.board.check_words_from_board(self.loaded_dictionary, self.new_player_move_board)

        if self.valid_move is True and words_4_score != {} and self.players[self.current_player].bot is True:
            # increment moves_count
            self.moves_count += 1
            # index of score field
            print("277", self.dict_players[self.current_player])
            self.dict_players[self.current_player][8] += self.board.get_score(words_4_score, self.new_player_move_board)
            # update players score on gui
            self.players[self.current_player].score = self.dict_players[self.current_player][8]
            # place letters put by AI
            letters = ""
            coordinates = []
            for word_and_coords in words_4_score.items():
                self.board.checked_words.update({word_and_coords[0]: word_and_coords[1]})
                letters += word_and_coords[0]
                coordinates.extend(word_and_coords[1])
            self.ai_place_letter(letters, coordinates)
            # copy the player's board onto main board
            self.actual_board = self.new_player_move_board
            ### INSERT BOARD INTO DB
            _b2string = board_to_string(self.actual_board)
            # TODO: copy self.new_player_move_board into db
            ManagementGeneralLeaderboard.save_board(_b2string, self.game_id, self.players[self.current_player].name,
                                                    self.moves_count)
            # acquire all board per move info; index[1][0][3] denotes board2string; index[] is bool
            #_string2b = string_to_board(ManagementGeneralLeaderboard.acquire_board(self.game_id)[1][0][3])

            self.board.actual_board = self.actual_board
            # check for new adjacencies 0,1,2
            self.board.create_sum_board_4_connection()

            for i in range(15):
                for j in range(15):
                    self.dict_board_labels[eval("self.ui.board_label_" + str(i) + "_" + str(j))] = \
                        [eval("self.ui.board_label_" + str(i) + "_" + str(j)).text(),
                        eval("self.ui.board_label_" + str(i) + "_" + str(j)).styleSheet(), i, j]



        elif self.valid_move is True and words_4_score != {}:
            # increment moves_count
            self.moves_count += 1
            # index of score field
            self.dict_players[self.current_player][8] += self.board.get_score(words_4_score, self.new_player_move_board)
            # update players score on gui
            self.players[self.current_player].score = self.dict_players[self.current_player][8]
            # copy the player's board onto main board
            self.actual_board = self.new_player_move_board

            ### INSERT BOARD INTO DB
            _b2string = board_to_string(self.actual_board)
            # TODO: copy self.new_player_move_board into db
            ManagementGeneralLeaderboard.save_board(_b2string, self.game_id, self.players[self.current_player].name, self.moves_count)
            # acquire all board per move info; index[1][0][3] denotes board2string; index[] is bool
            #_string2b = string_to_board(ManagementGeneralLeaderboard.acquire_board(self.game_id)[1][0][3])

            self.board.actual_board = self.actual_board
            # check for new adjacencies 0,1,2
            self.board.create_sum_board_4_connection()

            # self.dict_players[self.current_player][9] = 0
            # no foul committed; delete all warnings for the player if valid move
            # del self.players[self.current_player].fails

            for i in range(15):
                for j in range(15):
                    self.dict_board_labels[eval("self.ui.board_label_" + str(i) + "_" + str(j))] = \
                        [eval("self.ui.board_label_" + str(i) + "_" + str(j)).text(),
                        eval("self.ui.board_label_" + str(i) + "_" + str(j)).styleSheet(), i, j]

        # foul committed
        else:
            # add penalty point
            self.dict_players[self.current_player][9] += 1
            # increase foul count
            self.players[self.current_player].fails = 1

            for _tile in self.coords_of_letters_used:
                eval("self.ui.board_label_" + str(_tile[0]) + "_" + str(_tile[1])).setEnabled(1)
            self.coords_of_letters_used.clear()

            for i in range(15):
                for j in range(15):
                    # clear player's virtual board
                    if self.check_in_which_move[i][j] == self.which_move:
                        self.new_player_move_board[i][j] = '-'
                        eval("self.ui.board_label_" + str(i) + "_" + str(j)).setText(
                            self.dict_board_labels[eval("self.ui.board_label_" + str(i) + "_" + str(j))][0])

                        eval("self.ui.board_label_" + str(i) + "_" + str(j)).setStyleSheet(
                            self.dict_board_labels[eval("self.ui.board_label_" + str(i) + "_" + str(j))][1])

        # Generating new Tiles on the rack
        if self.valid_move is True and self.players[self.current_player].bot is True:
            # SWITCH would be useful...
            how_many_tiles_used = 7 - len(self.rack_AI)
            last_write = 0
            for i in range(0, how_many_tiles_used):
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                if i == 0:
                    self.ui.pushButton1.setText(self.new_letter)
                    # bylo git self.dict_players[self.current_player][1] = self.new_letter
                    self.dict_players[self.current_player][0] = self.new_letter
                elif i == 1:
                    self.ui.pushButton2.setText(self.new_letter)
                    self.dict_players[self.current_player][1] = self.new_letter
                elif i == 2:
                    self.ui.pushButton3.setText(self.new_letter)
                    self.dict_players[self.current_player][2] = self.new_letter
                elif i == 3:
                    self.ui.pushButton4.setText(self.new_letter)
                    self.dict_players[self.current_player][3] = self.new_letter
                elif i == 4:
                    self.ui.pushButton5.setText(self.new_letter)
                    self.dict_players[self.current_player][4] = self.new_letter
                elif i == 5:
                    self.ui.pushButton6.setText(self.new_letter)
                    self.dict_players[self.current_player][5] = self.new_letter
                elif i == 6:
                    self.ui.pushButton7.setText(self.new_letter)
                    self.dict_players[self.current_player][6] = self.new_letter

                # To check how many tiles were not touched during the move
                last_write = i

            # Add letters to the rack which stayed on the rack; Order will be different on the rack
            index = 0
            for i in range(last_write+1, 7):
                if i == 0:
                    self.ui.pushButton1.setText(self.new_letter)
                    self.dict_players[self.current_player][0] = self.rack_AI[index]
                elif i == 1:
                    self.ui.pushButton2.setText(self.new_letter)
                    self.dict_players[self.current_player][1] = self.rack_AI[index]
                elif i == 2:
                    self.ui.pushButton3.setText(self.new_letter)
                    self.dict_players[self.current_player][2] = self.rack_AI[index]
                elif i == 3:
                    self.ui.pushButton4.setText(self.new_letter)
                    self.dict_players[self.current_player][3] = self.rack_AI[index]
                elif i == 4:
                    self.ui.pushButton5.setText(self.new_letter)
                    self.dict_players[self.current_player][4] = self.rack_AI[index]
                elif i == 5:
                    self.ui.pushButton6.setText(self.new_letter)
                    self.dict_players[self.current_player][5] = self.rack_AI[index]
                elif i == 6:
                    self.ui.pushButton7.setText(self.new_letter)
                    self.dict_players[self.current_player][6] = self.rack_AI[index]

                index += 1

            self.players[self.current_player].rack = self.dict_players[self.current_player][:7]

        # player can skip move and exchange letters on rack
        elif self.valid_move is True:
            #self.dict_players[self.current_player][10] = 0
            #del self.players[self.current_player].swapped
            if self.pushButton1_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.ui.pushButton1.setText(self.new_letter)
                # bylo git self.dict_players[self.current_player][1] = self.new_letter
                self.dict_players[self.current_player][0] = self.new_letter
                #print(self.dict_players[self.current_player])
                #print(self.dict_players[self.current_player][0])

            if self.pushButton2_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.ui.pushButton2.setText(self.new_letter)
                self.dict_players[self.current_player][1] = self.new_letter
                #print(self.dict_players[self.current_player])
                #print(self.dict_players[self.current_player][1])

            if self.pushButton3_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.ui.pushButton3.setText(self.new_letter)
                self.dict_players[self.current_player][2] = self.new_letter

            if self.pushButton4_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.ui.pushButton4.setText(self.new_letter)
                self.dict_players[self.current_player][3] = self.new_letter

            if self.pushButton5_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.ui.pushButton5.setText(self.new_letter)
                self.dict_players[self.current_player][4] = self.new_letter

            if self.pushButton6_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.ui.pushButton6.setText(self.new_letter)
                self.dict_players[self.current_player][5] = self.new_letter

            if self.pushButton7_used == 1:
                self.new_letter = self.racks.bag.generate_letter_from_bag()
                self.ui.pushButton7.setText(self.new_letter)
                self.dict_players[self.current_player][6] = self.new_letter

        self.pushButton1_used = 0
        self.pushButton2_used = 0
        self.pushButton3_used = 0
        self.pushButton4_used = 0
        self.pushButton5_used = 0
        self.pushButton6_used = 0
        self.pushButton7_used = 0

        self.pushButton1_check = 0
        self.pushButton2_check = 0
        self.pushButton3_check = 0
        self.pushButton4_check = 0
        self.pushButton5_check = 0
        self.pushButton6_check = 0
        self.pushButton7_check = 0

        self.ui.pushButton1.setStyleSheet('background-color:lightgrey')
        self.ui.pushButton2.setStyleSheet('background-color:lightgrey')
        self.ui.pushButton3.setStyleSheet('background-color:lightgrey')
        self.ui.pushButton4.setStyleSheet('background-color:lightgrey')
        self.ui.pushButton5.setStyleSheet('background-color:lightgrey')
        self.ui.pushButton6.setStyleSheet('background-color:lightgrey')
        self.ui.pushButton7.setStyleSheet('background-color:lightgrey')

        self.letter_to_board = ""

        self.valid_move = False

        self.ui.number_of_letters.setText(str(self.racks.bag.get_size_of_bag()))
        self.letters_used.clear()
        self.coords_of_letters_used.clear()

        self.which_move += 1

        # tu trzeba zrobic sprawdzenie boardu i wtedy:
        # for i in range(15):
        #         for j in range(15):
        #                 self.dict_board_labels[eval("self.board_label_" + str(i) + "_" + str(j))] = \
        #                 [eval("self.board_label_" + str(i) + "_" + str(j)).text(), eval("self.board_label_" + str(i) + "_" + str(j)).styleSheet()]

    def clicked_clear(self):
        self.letters_used.clear()
        for _tile in self.coords_of_letters_used:
            eval("self.ui.board_label_" + str(_tile[0]) + "_" + str(_tile[1])).setEnabled(1)
        self.coords_of_letters_used.clear()

        for i in range(15):
            for j in range(15):
                if self.check_in_which_move[i][j] == self.which_move:
                    self.new_player_move_board[i][j] = '-'
                    eval("self.ui.board_label_" + str(i) + "_" + str(j)).setText(
                        self.dict_board_labels[eval("self.ui.board_label_" + str(i) + "_" + str(j))][0])

                    eval("self.ui.board_label_" + str(i) + "_" + str(j)).setStyleSheet(
                        self.dict_board_labels[eval("self.ui.board_label_" + str(i) + "_" + str(j))][1])

                    if self.pushButton1_used == 1:
                        self.pushButton1_used = 0
                        self.ui.pushButton1.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton1_check = 0

                    if self.pushButton2_used == 1:
                        self.pushButton2_used = 0
                        self.ui.pushButton2.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton2_check = 0

                    if self.pushButton3_used == 1:
                        self.pushButton3_used = 0
                        self.ui.pushButton3.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton3_check = 0

                    if self.pushButton4_used == 1:
                        self.pushButton4_used = 0
                        self.ui.pushButton4.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton4_check = 0

                    if self.pushButton5_used == 1:
                        self.pushButton5_used = 0
                        self.ui.pushButton5.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton5_check = 0

                    if self.pushButton6_used == 1:
                        self.pushButton6_used = 0
                        self.ui.pushButton6.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton6_check = 0

                    if self.pushButton7_used == 1:
                        self.pushButton7_used = 0
                        self.ui.pushButton7.setStyleSheet('background-color:lightgrey')
                        self.letter_to_board = ""
                        self.pushButton7_check = 0

    def clicked_change_letters(self):
        self.change_letters_check = 1
        self.ui.change_letters.setStyleSheet("background-color:\"red\"\n""")

    def clicked_change_letters_cancel(self):
        self.change_letters_check = 0
        self.ui.change_letters.setStyleSheet("background-color:\"lightgrey\"\n""")

    def clicked_change_letters_confirm(self):
        if self.change_letters_check == 1:
            self.temp = 0

            if self.pushButton1_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton1_check = 0
                self.buttons_to_change[self.temp] = self.ui.pushButton1
                self.temp += 1

            if self.pushButton2_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton2_check = 0
                self.buttons_to_change[self.temp] = self.ui.pushButton2
                self.temp += 1

            if self.pushButton3_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton3_check = 0
                self.buttons_to_change[self.temp] = self.ui.pushButton3
                self.temp += 1

            if self.pushButton4_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton4_check = 0
                self.buttons_to_change[self.temp] = self.ui.pushButton4
                self.temp += 1

            if self.pushButton5_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton5_check = 0
                self.buttons_to_change[self.temp] = self.ui.pushButton5
                self.temp += 1

            if self.pushButton6_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton6_check = 0
                self.buttons_to_change[self.temp] = self.ui.pushButton6
                self.temp += 1

            if self.pushButton7_check == 1:
                self.number_buttons_to_change += 1
                self.pushButton7_check = 0
                self.buttons_to_change[self.temp] = self.ui.pushButton7
                self.temp += 1

            if self.number_buttons_to_change <= self.racks.bag.get_size_of_bag():
                for i in self.buttons_to_change:
                    # self.random_number = random.randint(
                    #     0, len(self.letter_list)-1)
                    # self.buttons_to_change[i].setText(
                    #     self.letter_list[self.random_number])

                    # self.letter_list.pop(self.random_number)
                    self.letter_to_swap = self.buttons_to_change[i].text()
                    aux_letter = self.racks.bag.swap_letters(self.letter_to_swap)
                    self.buttons_to_change[i].setText(aux_letter)
                    self.buttons_to_change[i].setStyleSheet(
                        "background-color:\"lightgrey\"\n""")

            self.ui.change_letters.setStyleSheet(
                "background-color:\"lightgrey\"\n""")
            self.change_letters_check = 0
            self.which_move += 1
            self.ui.number_of_letters.setText(str(self.racks.bag.get_size_of_bag()))

            #self.dict_players[self.current_player][10] += 1
            #self.players[self.current_player].swapped = 1
            self.dict_players[self.current_player][9] += 1
            self.players[self.current_player].fails = 1

            self.safe_words()
            self.check_to_kick_player()
            self.change_player()

    def check_to_kick_player(self):
        letter_helper = self.dict_players[self.current_player]
        self.players[self.current_player].rack = [letter_helper[0], letter_helper[1], letter_helper[2], \
                                                  letter_helper[3], letter_helper[4], letter_helper[5], \
                                                  letter_helper[6]]
        # if self.dict_players[self.current_player][9] == 2 or self.dict_players[self.current_player][10] == 3:
        if self.dict_players[self.current_player][9] == 3:

            self.name_kicked_player = self.dict_players[self.current_player][7]

            self.players_to_db[self.dict_players[self.current_player][7]] = self.dict_players[self.current_player][8]
            print(self.players_to_db)

            self.dict_players.pop(self.current_player)
            self.number_of_players -= 1

            self.check_if_player_kicked = True

        else:
            self.check_if_player_kicked = False

    def change_player(self):
        if self.racks.bag.get_size_of_bag() < 7:
            for key in self.dict_players:
                self.players_to_db[self.dict_players.get(key)[7]] = self.dict_players.get(key)[8]

            self.managment_db.insert_db(self.players_to_db)
            self.game_over()

        else:
            if self.check_if_player_kicked is True:
                for i in range(self.number_of_players + 1):
                    if i in self.dict_players:
                        pass

                    else:
                        for j in range(self.number_of_players - i):
                            self.dict_players[i+j] = self.dict_players.pop(i+j+1)

            if self.number_of_players == 1:
                print(self.dict_players)
                self.players_to_db[self.dict_players[0][7]] = self.dict_players[0][8]
                self.managment_db.insert_db(self.players_to_db)
                self.game_over()

            elif self.number_of_players != 0:
                self.players_sorted = []

                for i in range(self.number_of_players):
                    self.players_sorted.append([self.dict_players[i][7], self.dict_players[i][8]])

                self.players_sorted.sort(key=lambda x: x[1])

                if self.check_if_player_kicked is True:
                    self.kicked_player_pop()
                else:
                    self.new_player_pop()

                self.current_player = (self.which_move - 1) % self.number_of_players
                self.ui.player_name.setText(self.dict_players[self.current_player][7])
                self.ui.how_many_points.setText(str(self.dict_players[self.current_player][8]))
                # get letters of new player and place on buttons
                letter_helper = self.dict_players[self.current_player]

                self.ui.pushButton1.setText(letter_helper[0])
                self.ui.pushButton2.setText(letter_helper[1])
                self.ui.pushButton3.setText(letter_helper[2])
                self.ui.pushButton4.setText(letter_helper[3])
                self.ui.pushButton5.setText(letter_helper[4])
                self.ui.pushButton6.setText(letter_helper[5])
                self.ui.pushButton7.setText(letter_helper[6])

    # def kicked_player_pop(self):
    #     self.window5 = QtWidgets.QMainWindow()
    #     self.ui = Ui_Form7(self.name_kicked_player)
    #     self.ui.setupUi(self.window5)
    #     self.window5.show()
    #     QtCore.QTimer.singleShot(3000, self.window5.close)
    #     self.kicked_player_check = True

    ######### POP-UP HANDLERS
    # ui[1-9] is how ui[0] remains intact kurwa trzeba bylo to od nowa pisac
    def game_over(self):
        self.check_game_over = True
        self.players_sorted = []
        self.moves_count = 0
        for key in self.players_to_db:
            self.players_sorted.append([key, self.players_to_db.get(key)])

        self.players_sorted.sort(key=lambda x: x[1])
        ### SET WINNER ASSUMING SORTED[0][1] IS WINNER
        # ManagementGeneralLeaderboard.update_game_winner(self.game_id, self.players_sorted[0][1])
        ManagementGeneralLeaderboard.update_game_winner(self.game_id, self.players_sorted[0][0])

        ### UPDATE MENU LEADERBOARD
        self.menu_handle.fetch_and_set_players_score()
        self.menu_handle._is_hs_open = False

        self.window4 = QtWidgets.QMainWindow()
        self.ui4 = game_over.Ui_Form8(self.players_sorted, self)
        self.ui4.setupUi(self.window4)
        self.window4.show()
        # self.form.hide()
        self.close()

    def kicked_player_pop(self):
        self.window5 = QtWidgets.QMainWindow()
        self.ui5 = Ui_Form7(self.name_kicked_player)
        self.ui5.setupUi(self.window5)
        self.window5.show()
        QtCore.QTimer.singleShot(3000, self.window5.close)

        QtCore.QTimer.singleShot(3000, self.new_player_pop)

    def new_player_pop(self):
        # open notification of turn termination
        self.window2 = QtWidgets.QMainWindow()
        # Throws error when there are more than 2 players; during ending
        # Jeżeli jest jeden gracz to wywoła się funcja game_over/endgame
        if len(self.dict_players) == 1:
            return
        else:
            print(self.dict_players[self.current_player][7])
            self.ui2 = Ui_Form6(self.players_sorted, self.dict_players[self.current_player][7])
            self.ui2.setupUi(self.window2)
            self.window2.show()
            QtCore.QTimer.singleShot(3000, self.window2.close)

    def clicked_leaderboard(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui3 = Ui_Form5(self.players_sorted)
        self.ui3.setupUi(self.window3)
        self.window3.show()

    def clicked_help(self):
        self.window6 = QtWidgets.QMainWindow()
        self.ui6 = Ui_Form9()
        self.ui6.setupUi(self.window6)
        self.window6.show()

    def safe_words(self):
        self.dict_players[self.current_player][0] = self.ui.pushButton1.text()
        self.dict_players[self.current_player][1] = self.ui.pushButton2.text()
        self.dict_players[self.current_player][2] = self.ui.pushButton3.text()
        self.dict_players[self.current_player][3] = self.ui.pushButton4.text()
        self.dict_players[self.current_player][4] = self.ui.pushButton5.text()
        self.dict_players[self.current_player][5] = self.ui.pushButton6.text()
        self.dict_players[self.current_player][6] = self.ui.pushButton7.text()

        print(self.dict_players)

    ######### BUTTONS HANDLERS
    def clicked_pushButton1(self):
        if self.pushButton1_used == 0:
            if self.change_letters_check == 1:
                if self.pushButton1_check == 0:
                    self.ui.pushButton1.setStyleSheet('background-color:red')
                    self.pushButton1_check = 1

                else:
                    self.ui.pushButton1.setStyleSheet('background-color:lightgrey')
                    self.pushButton1_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.ui.pushButton1.setStyleSheet('background-color:red')
                    self.pushButton1_check = 1
                    self.letter_to_board = self.ui.pushButton1.text()
                else:
                    self.ui.pushButton1.setStyleSheet('background-color:lightgrey')
                    self.pushButton1_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton2(self):
        if self.pushButton2_used == 0:
            if self.change_letters_check == 1:
                if self.pushButton2_check == 0:
                    self.ui.pushButton2.setStyleSheet('background-color:red')
                    self.pushButton2_check = 1

                else:
                    self.ui.pushButton2.setStyleSheet('background-color:lightgrey')
                    self.pushButton2_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:

                    self.ui.pushButton2.setStyleSheet('background-color:red')
                    self.pushButton2_check = 1
                    self.letter_to_board = self.ui.pushButton2.text()
                else:
                    self.ui.pushButton2.setStyleSheet('background-color:lightgrey')
                    self.pushButton2_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton3(self):

        if self.pushButton3_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton3_check == 0:
                    self.ui.pushButton3.setStyleSheet('background-color:red')
                    self.pushButton3_check = 1

                else:
                    self.ui.pushButton3.setStyleSheet('background-color:lightgrey')
                    self.pushButton3_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.ui.pushButton3.setStyleSheet('background-color:red')
                    self.pushButton3_check = 1
                    self.letter_to_board = self.ui.pushButton3.text()
                else:
                    self.ui.pushButton3.setStyleSheet('background-color:lightgrey')
                    self.pushButton3_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton4(self):
        if self.pushButton4_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton4_check == 0:
                    self.ui.pushButton4.setStyleSheet('background-color:red')
                    self.pushButton4_check = 1

                else:
                    self.ui.pushButton4.setStyleSheet('background-color:lightgrey')
                    self.pushButton4_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.ui.pushButton4.setStyleSheet('background-color:red')
                    self.pushButton4_check = 1
                    self.letter_to_board = self.ui.pushButton4.text()
                else:
                    self.ui.pushButton4.setStyleSheet('background-color:lightgrey')
                    self.pushButton4_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton5(self):
        if self.pushButton5_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton5_check == 0:
                    self.ui.pushButton5.setStyleSheet('background-color:red')
                    self.pushButton5_check = 1

                else:
                    self.ui.pushButton5.setStyleSheet('background-color:lightgrey')
                    self.pushButton5_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.ui.pushButton5.setStyleSheet('background-color:red')
                    self.pushButton5_check = 1
                    self.letter_to_board = self.ui.pushButton5.text()
                else:
                    self.ui.pushButton5.setStyleSheet('background-color:lightgrey')
                    self.pushButton5_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton6(self):
        if self.pushButton6_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton6_check == 0:
                    self.ui.pushButton6.setStyleSheet('background-color:red')
                    self.pushButton6_check = 1

                else:
                    self.ui.pushButton6.setStyleSheet('background-color:lightgrey')
                    self.pushButton6_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.ui.pushButton6.setStyleSheet('background-color:red')
                    self.pushButton6_check = 1
                    self.letter_to_board = self.ui.pushButton6.text()
                else:
                    self.ui.pushButton6.setStyleSheet('background-color:lightgrey')
                    self.pushButton6_check = 0
                    self.letter_to_board = ""

    def clicked_pushButton7(self):
        if self.pushButton7_used == 0:

            if self.change_letters_check == 1:
                if self.pushButton7_check == 0:
                    self.ui.pushButton7.setStyleSheet('background-color:red')
                    self.pushButton7_check = 1

                else:
                    self.ui.pushButton7.setStyleSheet('background-color:lightgrey')
                    self.pushButton7_check = 0

            else:
                if self.pushButton1_check == 0 and self.pushButton2_check == 0 and self.pushButton3_check == 0 and self.pushButton4_check == 0 \
                        and self.pushButton5_check == 0 and self.pushButton6_check == 0 and self.pushButton7_check == 0:
                    self.ui.pushButton7.setStyleSheet('background-color:red')
                    self.pushButton7_check = 1
                    self.letter_to_board = self.ui.pushButton7.text()
                else:
                    self.ui.pushButton7.setStyleSheet('background-color:lightgrey')
                    self.pushButton7_check = 0
                    self.letter_to_board = ""


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    test1 = Player("", [])
    test2 = Player("", [])
    test3 = Player("", [])
    # test4 = Player("", [])
    test1.name = "XD"
    test2.name = "elo"
    test3.name = "yo"
    # test4.name = "asd"
    test = [test1, test2, test3]
    ui = Board_gui(3, test, QMainWindow())
    # ui.setupUi(Form)
    # Form.show()
    sys.exit(app.exec())
