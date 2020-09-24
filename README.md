# Repositório sobre utilização do Python com Mysql

**Como conectar o python em um banco de dados Mysql?**

Esse repositório foi criado com a finalidade de expor um exemplo básico de conexão
do python com um banco de dados Mysql.



## Conjunto de Passos

**O primeiro passo é rodar o seguinte comando para instalar o conector no python:**

```console
pip install mysql-connector-python
```

**Já no código***

Deve-se importar o conector com a seguinte linha:

```Python
import mysql.connector
```

Deve-se criar a conexão:

```Python
mydb = mysql.connector.connect(
    host="10.40.10.232",
    user="jrdutra",
    password="123456",
    database="laravel_joao"
)
```

Já dentro da função onde será feito o sql, deve-se obter o cursor do mysql:


```Python
mycursor = mydb.cursor()
```

Posteriormente, criar o sql da seguinte forma:

```Python
sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
```

Depois deve-se criar a seguinte tupla:

```Python
val = ("Leandra", "leandra@gmail.com", "123456")
```

Então, executar o sql com a tupla de informações da seguinte forma:

```Python
mycursor.execute(sql, val)
```

E por fim, realizar o commit da tarefa:

```Python
mydb.commit()
```

## Exemplo completo:

```Python
import mysql.connector

mydb = mysql.connector.connect(
    host="10.40.10.232",
    user="jrdutra",
    password="123456",
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
```


## Fontes: 

[https://pynative.com/](https://pynative.com/install-mysql-connector-python/)

[https://www.w3schools.com/](https://www.w3schools.com/python/python_mysql_insert.asp)
