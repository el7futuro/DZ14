import sqlite3

con = sqlite3.connect("netflix.db")
cur = con.cursor()
sqlite_query = ("select * FROM netflix " )
cur.execute(sqlite_query)
result = cur.fetchall()

con.close()

if __name__ == '__main__':
    print(result)