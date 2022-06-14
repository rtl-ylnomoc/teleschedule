import psycopg2 as pg

from helpers import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DEFAULT_GROUP_PASSWORD


def sql_start():
    global conn, cur
    conn = pg.connect(host=DB_HOST, user=DB_USER,
                      password=DB_PASSWORD, database=DB_NAME)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute('SELECT version()')
    print(f'PG Server version: {cur.fetchone()}')
    # cur.execute('CREATE TABLE IF NOT EXISTS schedule_days (id serial PRIMARY KEY, specgroup TEXT, day timestamptz, schedule TEXT)')
    cur.execute(
        'CREATE TABLE IF NOT EXISTS schedule_users (id integer PRIMARY KEY, specgroup TEXT, isadmin INTEGER)')
    # cur.execute('''
    #             INSERT INTO schedule_days (specgroup, day, schedule)
    #             VALUES ('123', '11-09-2001', 'chel')''')


def sql_stop():
    cur.close()
    conn.close()
    print('Data baZZe closed successfully')


# client
def sql_read_day(password: str, day: str):
    """ Gets schedule day by group password and date.

    Args:
        password (str): User group password.
        day (str): Day date of format strftime('%Y-%m-%d').

    Returns:
        list (tuple (str)): Schedule day table rows.
    """
    # cur.execute(
    #     '''SELECT * FROM schedule_days WHERE (specgroup=%s) AND (day=%s)''', [group, day])
    cur.execute('''
select ras_par, sub_name, tip_name, prep_name, kab_name, ras_date_date, grup_pass
from timetable.ras_les as les 
join timetable.ras as ras on les.id_ras=ras.id_ras 
join timetable.ras_date as date on les.id_ras=date.id_ras 
join timetable.ras_grup as rgrup on les.id_ras=rgrup.id_ras 
join timetable.grup as grup on grup.id_grup=rgrup.id_grup 
join timetable.sub as sub on les.id_sub=sub.id_sub
join timetable.tip as tip on les.id_tip=tip.id_tip
join timetable.prep as prep on les.id_prep=prep.id_prep
join timetable.kab as kab on les.id_kab=kab.id_kab
where grup_pass=%s and ras_date_date=%s
order by ras_par
limit 10
                ''', [password, day])
    return cur.fetchall()


def sql_get_user_ids():
    """ Gets user ids.
    Returns:
        list (int): User ids.
    """
    cur.execute('SELECT id, isadmin FROM schedule_users')
    user_ids = cur.fetchall()
    print('[sql_get_user_ids]', user_ids)
    return user_ids


def sql_get_user(id: int):
    """ Gets user row by their id or returns empty tuple.

    Args:
        id (int): User id

    Returns:
        tuple (int, str, int) | tuple (): User row.
    """
    cur.execute('SELECT * FROM schedule_users WHERE id=%s', [id])
    user = cur.fetchone()
    # if not user:
    #     cur.execute('INSERT INTO schedule_users (id, specgroup, isadmin) VALUES (%s, %s, %s)', [
    #         id, DEFAULT_GROUP_PASSWORD, '0'])
    #     # user = sql_get_user(id)
    #     user = tuple([id, DEFAULT_GROUP_PASSWORD, 0])
    print('[sql_get_user]', user)
    return user


def get_user_group(id: int):
    """ Gets user group password by their id or returns DEFAULT_GROUP_PASSWORD if user wasn't found.

    Args:
        id (int): User id.

    Returns:
        str: User group. Defaults to DEFAULT_GROUP_PASSWORD if user wasn't found.
    """
    row = sql_get_user(id)
    return row[1] if row else DEFAULT_GROUP_PASSWORD


async def sql_set_group(id: int, password: str):
    """ Sets user specgroup property to password or creates user with it if user wasn't found.

    Args:
        id (int): User id.
        password (str): User group password.
    """
    if sql_get_user(id):
        cur.execute('UPDATE schedule_users SET specgroup=%s WHERE id=%s', [
            password, id])
    else:
        cur.execute('INSERT INTO schedule_users (id, specgroup, isadmin) VALUES (%s, %s, %s)', [
            id, password, '0'])


# admin
def sql_add_admin(id: int):
    """ Sets user in users table isadmin property to 1 or creates user with it if user wasn't found.

    Args:
        id (int): User id.
    """
    if sql_get_user(id):
        cur.execute(
            'UPDATE schedule_users SET isadmin=%s WHERE id=%s', ['1', id])
    else:
        cur.execute('INSERT INTO schedule_users (id, specgroup, isadmin) VALUES (%s, %s, %s)', [
            id, DEFAULT_GROUP_PASSWORD, '1'])


def sql_get_admins():
    """ Gets admins' ids.

    Returns:
        list (int): Admins' ids.
    """
    cur.execute('SELECT id FROM schedule_users WHERE isadmin=true')
    return [row[0] for row in cur.fetchall()]


def sql_check_admin(id: int):
    """ Checks if user is admin by their id.

    Args:
        id (int): User id.

    Returns:
        bool: If user is admin — True, if not — False.
    """
    cur.execute('SELECT isadmin FROM schedule_users WHERE id=%s', [id])
    return cur.fetchone()  # if explodes maybe have to convert id to str explicitly
