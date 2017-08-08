from person import Person, PersonRepo
from participation import Participation, ParticipationRepo
from event import Event, EventRepo
from datetime import datetime, timedelta


def main():
    drop = True
    ParticipationRepo.create_table(drop)
    PersonRepo.create_table(drop)
    EventRepo.create_table(drop)

    ACM = Event(name="ACM", location="1408", time=datetime.now())
    PP = Event(name="Practical Programming", location="1408", time=datetime.now() + timedelta(1))
    SS = Event(name="School Start", location="2204", time=datetime.now() + timedelta(2))

    EventRepo.add_all([ACM, PP, SS])

    piti = Person(name="Piti")
    pam = Person(name="Pam")
    lookyee = Person(name="Lookyee")

    PersonRepo.add_all([piti, pam, lookyee])

    ParticipationRepo.participate(piti, ACM)
    ParticipationRepo.participate(piti, PP)
    ParticipationRepo.participate(pam, PP)
    ParticipationRepo.participate(pam, SS)
    ParticipationRepo.participate(lookyee, PP)
    ParticipationRepo.participate(lookyee, SS)


if __name__ == '__main__':
    main()
