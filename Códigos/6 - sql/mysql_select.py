import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="meu_bd"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

print("especifico:")
print(myresult[8])

# primeiro elemento
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchone()
print(myresult)