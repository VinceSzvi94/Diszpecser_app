import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Churros0505!",
)

# cursor objektum
cursorObject = dataBase.cursor()

# adatbazis letrehozasa
cursorObject.execute("CREATE DATABASE IF NOT EXISTS diszpecser_szolg")

print("Adatbazis letrehozva")