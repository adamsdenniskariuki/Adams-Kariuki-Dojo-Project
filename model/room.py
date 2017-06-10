

#class to create a room
class Room(object):

    def __init__(self, room_name, room_type):
        self.created_rooms = {}
        self.room_name = room_name
        self.room_type = room_type

    def create_room(self, room_name, room_type):

        if(isinstance(self.room_name, list) == True):
            for name in self.room_name:
                self.created_rooms[name] = self.room_type
            return self.created_rooms
        else:
            self.created_rooms[self.room_name] = self.room_type
            return self.created_rooms


#class to create an office
class Office(Room):

    def __init__(self):
        self.max_occupants = 6
        self.offices = {}

    def create_room(self, room_name, room_type):
        super(Office, self).__init__(room_name, room_type)
        if(isinstance(self.room_name, str)):
            if(not self.room_name.isalpha() or not self.room_name.isalpha()):
                return "Use alphabet (a-z) characters for the room name and room type"
        self.offices = super(Office, self).create_room(self.room_name, self.room_type)
        return    self.offices


#class to create a living space
class LivingSpace(Room):

    def __init__(self):
        self.max_occupants = 4
        self.living_spaces = {}

    def create_room(self, room_name, room_type):
        super(LivingSpace, self).__init__(room_name, room_type)
        if(isinstance(self.room_name, str)):
            if(not self.room_name.isalpha() or not self.room_name.isalpha()):
                return "Use alphabet (a-z) characters for the room name and room type"
        self.living_spaces = super(LivingSpace, self).create_room(self.room_name, self.room_type)
        return self.living_spaces
