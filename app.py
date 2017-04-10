"""
Dojo.

Usage:
	app.py create_room <room_type> <room_name>...
	app.py add_person (<person_name> <person_name>) (Fellow|Staff) [<wants_accommodation>]
	app.py (-h | --help)

Arguments:
	<room_type> Office or Living Space
	<room_name> Name of room
	<person_name> Name of person
	<Fellow|Staff> Person is either Staff or Fellow
	<wants_accommodation> Y or N

Options:
	-h, --help	show this message
"""


class Dojo(object):

	def __init__(self):
		pass


class Room(Dojo):
	
	def __init__(self, room_name = [], room_type = ""):
		self.all_rooms = {}
		self.room_name = room_name
		self.room_type = room_type

	def create_room(self, room_name, room_type):
		self.room_name = room_name
		self.room_type = room_type
		return


class Office(Room):
	
	def __init__(self):
		self.max_occupants = 4

	def create_room(self, room_name, room_type):
		super(Office, self).__init__(room_name, room_type)
		if(isinstance(self.room_name, list) == True):
			for name in self.room_name:
				self.all_rooms[name] = self.room_type
			return self.all_rooms
		else:
			self.all_rooms[self.room_name] = self.room_type
		
		return "An Office called {} has been successfully created!".format(
			self.room_name)


class LivingSpace(Room):
	
	def __init__(self):
		self.max_occupants = 6

	def create_room(self, room_name, room_type):
		super(LivingSpace, self).__init__(room_name, room_type)
		if(isinstance(self.room_name, list) == True):
			for name in self.room_name:
				self.all_rooms[name] = self.room_type
			return self.all_rooms
		else:
			self.all_rooms[self.room_name] = self.room_type
		
		return "A Living Space called {} has been successfully created!".format(
			self.room_name)


class Person(object):
	pass


class Staff(Person):
	pass


class Fellow(Person):
	pass


from docopt import docopt, DocoptExit
from pprint import pprint

if __name__ == '__main__':
	try:
		arguments = docopt(__doc__)

	except  DocoptExit as e:
		print('Invalid Command!')
		print(e)

	except SystemExit:
		pass

	else:
		if arguments['create_room'] == True and arguments['<room_type>'] == "Office":
			room_instance = Office()
			room_result = room_instance.create_room(
				arguments['<room_name>'], arguments['<room_type>'])
			if(isinstance(room_result, dict)):
				for room in room_result:
					print("An Office called {} has been successfully created!".format(
						room))
			else:
				print(room_result)
		
		elif arguments['create_room'] == True and arguments['<room_type>'] == "Livingspace":
			room_instance = LivingSpace()
			room_result = room_instance.create_room(
				arguments['<room_name>'], arguments['<room_type>'])
			if(isinstance(room_result, dict)):
				for room in room_result:
					print("A Living Space called {} has been successfully created!".format(
						room))
			else:
				print(room_result)