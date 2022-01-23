import sqlite3
from db.exceptions import UserNotRegistered, PasswordIsWrong, LoginAlreadyInUse
from windows.User import User


class UsersDB:
    def __init__(self):
        self.conn = sqlite3.connect('db/UsersDB.db')
        self.cursor = self.conn.cursor()

    def authenticate(self, login, password):
        result = self.cursor.execute("""SELECT id, login, password, balls FROM User
                    WHERE login = ?""", (login,)).fetchone()
        if result is None:
            raise UserNotRegistered(f"Пользователь с логином {login} не зарегистрирован")
        if result[2] != password:
            raise PasswordIsWrong("Неверный пароль")

        return User(id=result[0], login=result[1], balls=result[3])


    def register(self, login, password):
        try:
            self.cursor.execute("""INSERT INTO User (login, password) VALUES (?, ?)""", (login, password))
            self.conn.commit()
            result = self.cursor.execute("""SELECT id, login, balls FROM User
                            WHERE login = ?""", (login,)).fetchone()
            return User(id=result[0], login=result[1], balls=result[2])
        except sqlite3.IntegrityError as e:
            if str(e) == 'UNIQUE constraint failed: User.login':
                raise LoginAlreadyInUse(f'Пользователь с логином {login} уже зарегистрирован')
            else:
                raise e
