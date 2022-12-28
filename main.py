import psycopg2


try:
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1234',
        database='Homework3',
        port='5432'
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        try:
            with connection.cursor() as cursor:
                sql = "CREATE TABLE My_table (name varchar(40) not null, surname varchar(70) not null)"
                cursor.execute(sql)
                print("table created successfully")

        except Exception as _ex:
            pass

        finally:
            with connection.cursor() as cursor:

                sql = "DELETE FROM My_table"
                cursor.execute(sql)

                sql = "INSERT INTO My_table (name, surname) VALUES ('Joshua', 'MR Bin'), ('vladimir', '<Bogdan bogom dan>')"
                cursor.execute(sql)

                sql = "SELECT name, surname FROM My_table"
                cursor.execute(sql)
                print(cursor.fetchall())

                sql = "UPDATE My_table SET name = 'vitaly' WHERE name = 'Papich' "
                cursor.execute(sql)

                sql = "SELECT name, surname FROM My_table"
                cursor.execute(sql)
                print('\n', cursor.fetchall())

                sql = "DELETE FROM My_table WHERE name = 'Bogdan' "
                cursor.execute(sql)

                sql = "SELECT name, surname FROM My_table"
                cursor.execute(sql)
                print('\n', cursor.fetchall())

except Exception as _ex:
    print("Error postgres", _ex)

finally:
    if connection:
        connection.close()