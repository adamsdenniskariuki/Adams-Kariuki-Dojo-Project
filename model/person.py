import time
from abc import ABCMeta, abstractmethod

#class to create a person
class Person(metaclass=ABCMeta):

    def __init__(self, person_name, person_type, wants_accommodation='N'):
        self.person_name = person_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation
        self.id = id(self.person_name) + int(time.time())

    @abstractmethod
    def __repr__(self):
        return "{}".format(self.person_name)


#class to create staff
class Staff(Person):

    def __init__(self, person_name):
        super(Staff, self).__init__(person_name, 'Staff')

    def __repr__(self):
        return "{}".format(self.person_name)


#class to create a fellow
class Fellow(Person):

    def __init__(self, person_name, wants_accommodation):
        super(Fellow, self).__init__(person_name, 'Fellow', wants_accommodation)

    def __repr__(self):
        return "{}".format(self.person_name)