import sqlite3

conn = sqlite3.connect('users.db', check_same_thread=False)
cursor = conn.cursor()


def db_fill_user_table(user_id: int, user_name: str):
    """

    :param user_id:
    :param user_name:
    :return:
    """
    cursor.execute('INSERT INTO user (user_id, user_name) VALUES (?, ?)', (user_id, user_name))
    conn.commit()


def db_remove_yandex_user(user_name: str = None, user_login: str = None, user_pass: str = None):
    """
    Removes Yandex user. Required only user_login and user_pass
    :param user_name: deprecated!
    :param user_login: required
    :param user_pass: required
    :return: None
    """
#    if(user_login != None and user_pass != None):
#        key: int = db_get_user_id_by_pass_and_login(user_login, user_pass, "yandex")
#        cursor.execute('DELETE FROM data WHERE id = ?', (str(key)))
    conn.commit()


def db_list_user():
    """
    Returns user list from user DB
    :return: list
    """
    res = cursor.execute('SELECT * FROM user').fetchall()
    return res


def db_add_task_to_user(id, code, task):
    cursor.execute('INSERT INTO task (id, task, code) VALUES (?, ?, ?)', (id, task, code))
    conn.commit()


def db_get_tasks_by_user_id(id):
    lid = str(id)
    res = cursor.execute('SELECT * FROM task WHERE id = ?', (lid, )).fetchall()
    return res


def db_remove_task_from_user():
    pass


def db_search_user_by_fullname(name: str):
    """
    Can be used to search user in 'user' DB

    :param name: user name to search
    :return: True if exists, False else
    """
    res = str(cursor.execute('SELECT * FROM user WHERE user_name = ?', (name, )).fetchone())
    conn.commit()
    print(res)
    if res == 'None': return False
    else: return True


def db_get_user_id_by_name(name: str):
    """
    Returns user id from 'user' DB
    returns nothing
    :param name: usr name to search
    :return: user id (str)
    """
    res = (cursor.execute('SELECT * FROM user WHERE user_name = ?', (name, )).fetchone())[1] #1 - user id, 0 - db id
    return res