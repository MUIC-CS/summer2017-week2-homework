from simpleorm import SimpleBean, SimpleRepo
from participation import ParticipationRepo


class Event(SimpleBean):
    columns = ('id', 'name', 'location', 'time')


class EventRepo(SimpleRepo):
    table_name = 'events'
    bean_class = Event
    create_query = """
        CREATE TABLE {table_name}(
            id SERIAL NOT NULL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            location VARCHAR(255) NOT NULL,
            time TIMESTAMP NOT NULL
        );
    """

    def get_participations(self):
        return ParticipationRepo.find_by_event_id(self.id)

    def get_participants(self):
        # this is called n+1 problem hitting db too many times
        # a good orm can take care of this problem
        person_ids = [p.person_id for p in self.get_participations()]
        return [PersonRepo.find_by_id(id) for id in person_ids]
