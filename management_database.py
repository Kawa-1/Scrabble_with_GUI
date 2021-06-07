from __future__ import annotations
import sqlite3 as sl


class ManagementGeneralLeaderboard:

    @staticmethod
    def insert_db(players_with_score: dict) -> noReturn:
        try:
            con = sl.connect("leaderboard.db")
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
            con = sl.connect("leaderboard.db")
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