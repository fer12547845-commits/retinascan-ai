import sqlite3

db = sqlite3.connect("retinascan.db", check_same_thread=False)
cursor = db.cursor()