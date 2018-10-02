import mysql.connector
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='192.168.42.45',
                                       database='feedback',
                                       user='admin',
                                       password='123456')
        if conn.is_connected() is False:
            print('Failed to connect to MySQL database')

    except Error as e:
        print(e)
        conn.close()

    return conn

def process_data(data):
    valstr = ""
    for i,val in enumerate(data):
        if i < len(data)-1:
            valstr= valstr + "'" + str(val) + "',"
        else:
            valstr = valstr + "'" + str(val) + "'"
    print(valstr)
    return valstr

def truncate(table):
    conn = None
    query = "TRUNCATE TABLE " + table + ";"
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def select_all_ticketdetails():
    conn = None
    query = "SELECT CUSTOMER, CHANNEL, PROBLEM, DETAILS FROM TicketDetails order by 1;"

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def insert(table, data):
    conn = None
    query = "INSERT INTO " + table+ " VALUES(" + process_data(data) +");"

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(query)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    connect()