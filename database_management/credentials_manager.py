import hashlib
import os
import platform
import sqlite3 as sl


class CredentialsManager:
    _path = ''
    if platform.system() == 'Darwin':
        _path = '{}{}'.format(os.getcwd(), '/DatabaseLogs/leaderboard.db')
    elif platform.system() == 'Windows':
        _path = '{}{}'.format(os.getcwd(), '\\DatabaseLogs\\leaderboard.db')

    @staticmethod
    def verify_credentials(login: str, password: str) -> bool:
        print('login to check %s; pass to check %s' % (login, password))

        _hash_pass = password.encode('utf-8')
        _hash_pass = hashlib.sha256(_hash_pass).hexdigest()
        _login = CredentialsManager.htmlspecialchars(login)

        try:
            ### ONLY IF RUN FROM THIS LVL
            # conn = sl.connect("../database_management/users_database.db")
            # users now in leaderboard.db
            """
                TODO: CHANGE leaderboard.db name to something more inclusive
            """
            conn = sl.connect(CredentialsManager._path)
            print(os.getcwd())
            cur = conn.cursor()
            cur.execute("SELECT password FROM users WHERE username=(?)", (_login,))
            # returns list of tuples, access first one w/ first value, i.e hashed password
            _pass = cur.fetchall()[0][0]
            conn.commit()
            conn.close()

        except Exception as e:
            print(e)
            return False

        # verify if fetched password for a given login matches the one entered
        if _pass == _hash_pass:
            return True
            print('correct pass')
        return False

    @staticmethod
    def change_password(login: str, password: str, new_password: str) -> bool:
        # verify if correct credentials
        if CredentialsManager.verify_credentials(login, password):
            _new_pass = new_password.encode('utf-8')
            _new_pass = hashlib.sha256(_new_pass).hexdigest()
            print('login given %s; pass to change %s, new: %s' % (login, password, new_password))

            try:
                conn = sl.connect(CredentialsManager._path)
                print(os.getcwd())
                cur = conn.cursor()
                cur.execute("UPDATE users SET password=(?) WHERE username=(?)", (_new_pass, login))
                conn.commit()
                conn.close()
                return True

            except Exception as e:
                print(e)

            return True
        else:
            return False

    @staticmethod
    def register_player(login: str, password: str) -> bool:
        _hash_pass = password.encode('utf-8')
        _hash_pass = hashlib.sha256(_hash_pass).hexdigest()
        _login = CredentialsManager.htmlspecialchars(login)
        print('register: login to check %s; pass to check %s' % (login, password))
        try:
            ### ONLY IF RUN FROM THIS LVL
            # conn = sl.connect("../database_management/users_database.db")
            # users now in leaderboard.db
            """
                TODO: CHANGE leaderboard.db name to something more inclusive
            """
            conn = sl.connect(CredentialsManager._path)
            print(os.getcwd())
            cur = conn.cursor()
            cur.execute("INSERT INTO users VALUES(?, ?)", (_login, _hash_pass))
            conn.commit()
            conn.close()
            return True

        except Exception as e:
            print(e)
            return False

    @staticmethod
    def htmlspecialchars(text: str) -> str:
        return (
            text.replace("&", "&amp;").
                replace('"', "&quot;").
                replace("<", "&lt;").
                replace(">", "&gt;")
        )
