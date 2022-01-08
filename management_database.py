from __future__ import annotations

import platform
import os
import sqlite3 as sl


class ManagementGeneralLeaderboard:
    _path = ''
    if platform.system() == 'Darwin':
        _path = '{}{}'.format(os.getcwd(), '/leaderboard.db')
    elif platform.system() == 'Windows':
        _path = '{}{}'.format(os.getcwd(), '\\leaderboard.db')

    @staticmethod
    def insert_db(players_with_score: dict) -> noReturn:
        try:
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            list_4_up = []
            for player in players_with_score:
                player_safe = ManagementGeneralLeaderboard.htmlspecialchars(player)
                list_4_up.append((player_safe, players_with_score.get(player)))

            cur.executemany("INSERT INTO general_leaderboard VALUES (?, ?)", list_4_up)
            con.commit()
            con.close()
        except Exception as e:
            print(e)

    @staticmethod
    def get_general_leaderboard() -> list_of_tuples:
        try:
            # con = sl.connect('{}{}'.format(os.getcwd(), '/leaderboard.db'))
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            cur.execute("SELECT * FROM general_leaderboard ORDER BY score DESC")
            everything = cur.fetchall()
            con.commit()
            con.close()
            return everything
        except Exception as e:
            print(e)
            return [()]

    @staticmethod
    def htmlspecialchars(text: str) -> str:
        return (
            text.replace("&", "&amp;").
                replace('"', "&quot;").
                replace("<", "&lt;").
                replace(">", "&gt;")
        )

    @staticmethod
    def save_board(board_to_string: str, game_id: int, player: str, move_id: int) -> bool:
        """
            board_to_string: board updated with letters after n-th move;
            game_id: id of scrabble match generated as game_id++ from last row acquired from all_games;
            player: who made the move;
            move_id: acquired as Board_gui.moves_count++;
        """
        try:
            # con = sl.connect("{}{}".format(os.getcwd(), "/leaderboard.db"))
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            cur.execute("INSERT INTO saved_boards(game_id, player, move_id, board) VALUES(?, ?, ?, ?)", (game_id, player, move_id, board_to_string,))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def acquire_board(game_id: int) -> [bool | list]:
        """
        ACCEPTS: game_id generated upon game start
        RETURNS: list of tuples (game_id, player that did the move, move id in respect to the game start, board2string)
        """
        try:
            # con = sl.connect("{}{}".format(os.getcwd(), "/leaderboard.db"))
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            cur.execute("SELECT * FROM saved_boards WHERE game_id=(?) ORDER BY move_id", (game_id,))
            _all_moves_per_game = cur.fetchall()
            con.commit()
            con.close()
            return [True, _all_moves_per_game]
        except Exception as e:
            print(e)
            return [False, []]

    @staticmethod
    def get_game_id() -> [bool | int]:
        try:
            # con = sl.connect("{}{}".format(os.getcwd(), "/leaderboard.db"))
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            cur.execute("SELECT count(game_id) FROM all_games")
            _last_index = cur.fetchall()
            con.commit()
            con.close()
            return [True, _last_index]
        except Exception as e:
            print(e)
            return [False, []]

    @staticmethod
    def register_game(players: str) -> [bool | int]:
        try:
            print(os.getcwd())
            # con = sl.connect("{}{}".format(os.getcwd(), "/leaderboard.db"))
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            cur.execute("SELECT count(game_id) FROM all_games")
            _last_index = cur.fetchall()[0][0]
            cur.execute("INSERT INTO all_games(game_id, players) VALUES(?, ?)", (_last_index+1, players,))
            con.commit()
            con.close()
            return [True, _last_index]
        except Exception as e:
            print(e)
            return [False, []]

    @staticmethod
    def update_game_winner(game_id: int, winner: str) -> bool:
        try:
            # con = sl.connect("{}{}".format(os.getcwd(), "/leaderboard.db"))
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            cur.execute("UPDATE all_games SET winner=(?) WHERE game_id=(?)", (winner, game_id,))
            con.commit()
            con.close()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def acquire_games_list(number=None) -> [bool | int]:
        try:
            # con = sl.connect("{}{}".format(os.getcwd(), "/leaderboard.db"))
            con = sl.connect(ManagementGeneralLeaderboard._path)
            cur = con.cursor()
            if number is not None:
                cur.execute("SELECT * FROM all_games ORDER BY game_id LIMIT (?)", (number,))
            elif number is None:
                cur.execute("SELECT * FROM all_games")
            _all_moves_per_game = cur.fetchall()
            con.commit()
            con.close()
            return [True, _all_moves_per_game]
        except Exception as e:
            print(e)
            return [False, []]

