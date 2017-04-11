"""
Dojo.

Usage:
	create_room <room_type> <room_name>...
	add_person (<person_name> <person_name>) (Fellow|Staff) [<wants_accommodation>]
	(-h | --help)
	(-i | --interactive)

Arguments:
	<room_type> Office or Living Space
	<room_name> Name of room
	<person_name> Name of person
	<Fellow|Staff> Person is either Staff or Fellow
	<wants_accommodation> Y or N

Options:
	-h, --help	show this message
	-i, --interactive  Interactive Mode
"""


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
		self.max_occupants = 4
		self.offices = {}

	def create_room(self, room_name, room_type):
		super(Office, self).__init__(room_name, room_type)
		self.offices = super(Office, self).create_room(self.room_name, self.room_type)
		return	self.offices


#class to create a living space
class LivingSpace(Room):
	
	def __init__(self):
		self.max_occupants = 6
		self.living_spaces = {}

	def create_room(self, room_name, room_type):
		super(LivingSpace, self).__init__(room_name, room_type)
		self.living_spaces = super(LivingSpace, self).create_room(self.room_name, self.room_type)
		return self.living_spaces


#class to create a person
class Person(object):

	def __init__(self, person_name, person_type, wants_accommodation = 'N'):
		self.person_name = person_name
		self.person_type = person_type
		self.wants_accommodation = wants_accommodation
		self.person_created = []

	def add_person(self, person_name, person_type, wants_accommodation):
		
		if(self.wants_accommodation and self.wants_accommodation == "Y" 
			and self.person_type == "Staff"):
			return "Staff are not allocated living quarters."
		elif(not self.wants_accommodation and self.person_type == "Staff" 
			or self.wants_accommodation == "N"):
			self.person_created = [self.person_name, self.person_type, 'N']
		elif(not self.wants_accommodation and self.person_type == "Fellow"):
			self.person_created = [self.person_name, self.person_type, 'N']
		elif(self.wants_accommodation and self.person_type == "Fellow"):
			self.person_created = [self.person_name, self.person_type, self.wants_accommodation]
		
		return self.person_created


#class to create staff
class Staff(Person):

	def __init__(self):
		self.created_staff = []

	def add_person(self, person_name, person_type, wants_accommodation = 'N'):
		super(Staff, self).__init__(person_name, person_type, wants_accommodation)
		self.created_staff = super(Staff, self).add_person(self.person_name, 
			self.person_type, self.wants_accommodation)
		return self.created_staff
		

#class to create a fellow
class Fellow(Person):
	
	def __init__(self):
		self.created_fellow = []

	def add_person(self, person_name, person_type, wants_accommodation = 'N'):
		super(Fellow, self).__init__(person_name, person_type, wants_accommodation)
		self.created_fellow = super(Fellow, self).add_person(self.person_name, 
			self.person_type, self.wants_accommodation)
		return self.created_fellow
		
import cmd
import random
from docopt import docopt, DocoptExit


#class to make the app interactive
class Dojo (cmd.Cmd):
    intro   = '\nWelcome to the dojo program!\n\nType help for assistance and exit to leave.\n'
    prompt  = 'Dojo >>>'
    file    = None
    created_rooms = {}
    created_persons = {}
    room_allocation = {}

    def allocate_room(self, person_name):
    	if(len(self.created_rooms) > 0):
    		rooms_list = []
    		for key, value in self.created_rooms.items():
    			rooms_list.append(key)

    		random_key = random.randint(0 , len(rooms_list) - 1)
    		room_allocated = rooms_list[random_key]
    		self.room_allocation.update({person_name:[room_allocated, self.created_rooms[room_allocated]]})

    		return 1

    def do_create_room(self, arg):

        """
        Usage: 
            create_room <room_type> <room_name>...
        """

        try: 
            arguments = docopt(self.do_create_room.__doc__, arg)

        except  DocoptExit as e:
            print('Invalid Command!')
            print(e)

        except SystemExit:
            pass

        else:
        	if arguments['<room_type>'] == "Office":
        		office_instance = Office()
        		office_result = office_instance.create_room(
					arguments['<room_name>'], arguments['<room_type>'])
        		if(isinstance(office_result, dict)):
        			self.created_rooms.update(office_result)
        			for office in office_result:
        				print("An Office called {} has been successfully created!".format(
							office))
        		else:
        			print(office_result)

        	elif arguments['<room_type>'] == "Livingspace":
        		livingspace_instance = LivingSpace()
        		livingspace_result = livingspace_instance.create_room(
        			arguments['<room_name>'], arguments['<room_type>'])
        		if(isinstance(livingspace_result, dict)):
        			self.created_rooms.update(livingspace_result)
        			for livingspace in livingspace_result:
        				print("A Living Space called {} has been successfully created!".format(
							livingspace))
        		else:
        			print(livingspace_result)

    def do_add_person(self, arg):

        """
        Usage: 
            add_person (<person_name> <person_name>) (Fellow|Staff) [<wants_accommodation>]
        """

        try: 
            arguments = docopt(self.do_add_person.__doc__, arg)

        except  DocoptExit as e:
            print('Invalid Command!')
            print(e)

        except SystemExit:
            pass

        else:
        	if arguments['Fellow']:
        		fellow_instance = Fellow()
        		fellow_result = fellow_instance.add_person(" ".join(arguments['<person_name>']),
					'Fellow', arguments['<wants_accommodation>'])
        		if (isinstance(fellow_result, str)):
        			print(fellow_result)
        		else:
        			self.created_persons.update({fellow_result[0] : [fellow_result[1], fellow_result[2]]})
        			print(fellow_result[1],fellow_result[0],"has been successfully added,")
        			if(self.allocate_room(fellow_result[0])):
        				allocations =  self.room_allocation[fellow_result[0]]
        				print(fellow_result[1], fellow_result[0], 
        					"has been allocated", allocations[1], allocations[0])

        	elif arguments['Staff']:
        		staff_instance = Staff()
        		staff_result = staff_instance.add_person(" ".join(arguments['<person_name>']),
					'Staff', arguments['<wants_accommodation>'])
        		if (isinstance(staff_result, str)):
        			print(staff_result)
        		else:
        			self.created_persons.update({staff_result[0] : [staff_result[1], staff_result[2]]})
        			print(staff_result[1],staff_result[0],"has been successfully added.")
        			if(self.allocate_room(staff_result[0])):
        				allocations =  self.room_allocation[staff_result[0]]
        				print(staff_result[1], staff_result[0], 
        					"has been allocated", allocations[1], allocations[0])

    def do_exit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        return True

if __name__ == '__main__':
	try:
		Dojo().cmdloop()
	except (KeyboardInterrupt, SystemExit):
		print("System shut down. Thank you.")
