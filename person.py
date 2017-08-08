from db import get_cursor
from simpleorm import SimpleBean, SimpleRepo


class Person(SimpleBean):
    columns = ('id', 'name')


class PersonRepo(SimpleRepo):
    table_name = 'people'
    bean_class = Person

    create_query = """
        CREATE TABLE {table_name}(
            id SERIAL NOT NULL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )
        """
