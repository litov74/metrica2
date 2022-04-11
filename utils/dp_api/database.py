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


def db_add_yandex_user(id: int, login: str, password: str):
    """

    :param id:
    :param login:
    :param password:
    :return:
    """
    cursor.execute('INSERT INTO data (user_id, service, login, password) VALUES (?, ?, ?, ?)', (id, "yandex", login, password))
    conn.commit()


def db_add_vk_user(id: int, login: str, password: str):
    """

    :param id:
    :param login:
    :param password:
    :return:
    """
    cursor.execute('INSERT INTO data (user_id, service, login, password) VALUES (?, ?, ?, ?)', (id, "vk", login, password))
    conn.commit()


def db_remove_yandex_user(user_name: str = None, user_login: str = None, user_pass: str = None):
    """
    Removes Yandex user. Required only user_login and user_pass
    :param user_name: deprecated!
    :param user_login: required
    :param user_pass: required
    :return: None
    """
    if(user_login != None and user_pass != None):
        key: int = db_get_user_id_by_pass_and_login(user_login, user_pass, "yandex")
        cursor.execute('DELETE FROM data WHERE id = ?', (str(key)))
    conn.commit()


def db_remove_vk_user(user_name: str = None, user_login: str = None, user_pass: str = None):
    """
    Removes VK user. Required only user_login and user_pass
    :param user_name: deprecated!
    :param user_login: required
    :param user_pass: required
    :return: None
    """
    if(user_name != None):
        cursor.execute('DELETE FROM user WHERE user_name = ? AND service = vk', (user_name, ))
    elif(user_login != None):
        cursor.execute('DELETE FROM data WHERE login = ? AND service = vk', (user_login, ))
    elif(user_pass != None):
        cursor.execute('DELETE FROM data WHERE password = ? AND service = vk', (user_pass, ))
    conn.commit()


def db_list_user():
    """
    Returns user list from user DB
    :return: list
    """
    res = cursor.execute('SELECT * FROM user').fetchall()
    return res


def db_link_user(service: str, id: int, login: str, password: str):
    """

    :param service:
    :param id:
    :param login:
    :param password:
    :return:
    """
    res = (cursor.execute(f'SELECT * FROM data WHERE service = "{service}" AND login = "{login}" AND password = "{password}"')).fetchone()
    cursor.execute('DELETE FROM data WHERE id = ?', (str(res[0])))
    conn.commit()
    cursor.execute('INSERT INTO data (user_id, service, login, password) VALUES (?, ?, ?, ?)', (id, res[1], res[2], res[3]))
    conn.commit()


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

    :param name: usr name to search
    :return: user id (str)
    """
    res = (cursor.execute('SELECT * FROM user WHERE user_name = ?', (name, )).fetchone())[1] #1 - user id, 0 - db id
    return res


def db_get_user_id_by_pass_and_login(login: str, passw: str, service: str):
    """

    :param login:
    :param passw:
    :param service:
    :return:
    """
    res = (cursor.execute('SELECT * FROM data where login = ?', (login, )).fetchall())
    for i in range(0, len(res)):
        if res[i][4] == passw and res[i][2] == service:
            print(int(res[i][0]))
            return int(res[i][0])
    return


def db_get_data_id_by_id(id: str):
    """

    :param id:
    :return:
    """
    res = (cursor.execute('SELECT * FROM data WHERE user_id = {}'.format(id))).fetchone()
    if str(res) == "None":
        return False
    else:
        return True
