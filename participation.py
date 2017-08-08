from db import get_cursor
from simpleorm import SimpleBean, SimpleRepo


class Participation(SimpleBean):
    columns = ('id',
               'person_id',
               'event_id')


class ParticipationRepo(SimpleRepo):
    table_name = 'participation'
    bean_class = Participation
    create_query = """
    CREATE TABLE {table_name}(
        id SERIAL NOT NULL PRIMARY KEY,
        person_id integer NOT NULL,
        event_id integer NOT NULL
    )
    """

    @classmethod
    def find_by_event_id(cls, event_id):
        return cls.find_by_col('event_id', event_id)

    @classmethod
    def find_by_person_id(cls, person_id):
        return cls.find_by_col('person_id', person_id)

    @classmethod
    def participate(cls, person, event):
        ppt = cls.bean_class(person_id=person.id, event_id=event.id)
        return cls.add(ppt)

    @classmethod
    def unparticipate(cls, id):
        cls.delete_by_id(id)
