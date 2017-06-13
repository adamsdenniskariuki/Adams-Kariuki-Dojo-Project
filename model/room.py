

#class to create a room
class Room(object):

    def __init__(self, room_name, room_type, max_occupants):
        self.room_name = room_name
        self.room_type = room_type
        self.max_occupants = max_occupants


#class to create an office
class Office(Room):

    def __init__(self, room_name, room_type):
        super(Office, self).__init__(room_name, room_type, max_occupants=6)


#class to create a living space
class LivingSpace(Room):

    def __init__(self, room_name, room_type):
        super(LivingSpace, self).__init__(room_name, room_type, max_occupants=4)
