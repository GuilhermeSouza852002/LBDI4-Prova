from sqlalchemy import create_engine, inspect

URL = "mysql+mysqlconnector://root:123456@localhost:3306/ORM"



def main():
    engine = create_engine(url=URL)

    print("Database List using SQLAlchemy")
    print("=================================")
    insp = inspect(engine)
    db_list = insp.get_schema_names()
    print(db_list)

    print("List database")
    print("=================================")

    with engine.connect() as connection:
        result_set = connection.execute("SHOW DATABASES")
        for row in result_set:
            print(row)

    print("\nUse database ORM")
    print("=================================")

    with engine.connect() as connection:
        connection.execute("USE ORM;")
        result_set = connection.execute("SHOW TABLES")
        for row in result_set:
            print(row[0])

        print('\n\n')
        print(result_set)


if __name__ == "__main__":
    main()