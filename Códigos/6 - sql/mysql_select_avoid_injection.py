import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="meu_bd"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address LIKE %s"
adr = ("%way%", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x) 