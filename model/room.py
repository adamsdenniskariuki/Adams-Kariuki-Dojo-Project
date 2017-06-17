from abc import ABCMeta, abstractmethod

#class to create a room
class Room(metaclass=ABCMeta):

    def __init__(self, room_name, room_type, max_occupants):
        self.room_name = room_name
        self.room_type = room_type
        self.max_occupants = max_occupants

    @abstractmethod
    def __repr__(self):
        return "{}".format(self.room_name)


#class to create an office
class Office(Room):

    def __init__(self, room_name, room_type):
        super(Office, self).__init__(room_name, "Office", max_occupants=6)

    def __repr__(self):
        return "{}".format(self.room_name)


#class to create a living space
class LivingSpace(Room):

    def __init__(self, room_name, room_type):
        super(LivingSpace, self).__init__(room_name, "LivingSpace", max_occupants=4)

    def __repr__(self):
        return "{}".format(self.room_name)
