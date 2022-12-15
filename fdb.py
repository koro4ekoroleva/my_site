import sqlite3

from app import app


class whatDB:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def setMenu(self, title, url):
        try:
            self.__cur.execute('INSERT INTO mainmenu VALUES(NULL, ?, ?)', (title, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка добавления в БД', e)
            return False
        return True

    def delMenu(self, id=0):
        try:
            if id == 0:
                self.__cur.execute('DELETE FROM mainmenu')
            else:
                self.__cur.execute(f"DELETE FROM mainmenu")  # сия фигня должна удалять по id
            self.__db.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления из БД', e)
            return False
        return True


if __name__ == '__main__':
    from app import create_db, connect_db

    db = connect_db()
    db = whatDB(db)

    """print(db.setMenu('Главная', 'index'))
    print(db.setMenu('О программе', 'about'))
    print(db.setMenu('Помощь', 'help'))
    print(db.setMenu('Обо мне', 'me'))
    print(db.setMenu('Спагетти', 'spagetti'))
    print(db.setMenu('Nyan Cat', 'Nyan Cat'))"""
    #print(db.delMenu(id=5))
    create_db()
