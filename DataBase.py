# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import sqlite3

try:
    conn = sqlite3.connect('/home/santapitia/Desktop/audio-compare-master/IndriIndri.db')
    sql = '''CREATE TABLE ColectData(
                  id INTEGER PRIMARY KEY,
                   FeoItovizany TEXT NOT NULL,
                  FeoVaovao TEXT NOT NULL
           );'''

    cur = conn.cursor()
    print("Connexion réussie à SQLite")
    cur.execute(sql)
    conn.commit()
    print("Table SQLite est créée")

    cur.close()
    conn.close()
    print("Connexion SQLite est fermée")

except sqlite3.Error as error:
    print("Erreur lors de la création du table SQLite", error)
   
