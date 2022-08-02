import sqlite3

##Создание и запись данных
def InpSet(token, secret, language):
    db = sqlite3.connect("ConnectSettings.db")
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS settingsapi (
        token text, 
        secret text, 
        language text
    )""")
    sql.execute(f"insert into settingsapi values (?, ?, ?)", (token, secret, language))
    db.commit()

##Обращение к БД
def OutSet():
    db = sqlite3.connect("ConnectSettings.db")
    sql = db.cursor()
    sql.execute("SELECT * FROM settingsapi")
    settings = sql.fetchall()
    db.commit()
    return settings

##Очищение БД
def DelSet():
    db = sqlite3.connect("ConnectSettings.db")
    sql = db.cursor()
    sql.execute("SELECT * FROM settingsapi")
    db.commit()