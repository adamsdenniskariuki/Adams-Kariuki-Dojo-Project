

#class to create a person
class Person(object):

    def __init__(self, person_name, person_type, wants_accommodation):
        self.person_name = person_name
        self.person_type = person_type
        self.wants_accommodation = wants_accommodation
        self.id = id(person_name)


#class to create staff
class Staff(Person):

    def __init__(self, person_name, person_type, wants_accommodation):
        super(Staff, self).__init__(person_name, person_type, wants_accommodation)     


#class to create a fellow
class Fellow(Person):

    def __init__(self, person_name, person_type, wants_accommodation):
        super(Fellow, self).__init__(person_name, person_type, wants_accommodation)