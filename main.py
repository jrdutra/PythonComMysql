import mysql.connector

mydb = mysql.connector.connect(
    host="10.40.10.232",
    user="jrdutra",
    password="Jrcdutra1",
    database="laravel_joao"
)


def main():
    mycursor = mydb.cursor()

    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    val = ("Leandra", "leandra@gmail.com", "123456")

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

if __name__ == "__main__":
    main()
