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
		self.created_rooms = {}
		self.room_name = room_name
		self.room_type = room_type

	def create_room(self, room_name, room_type):
		self.room_name = room_name
		self.room_type = room_type
		
		if(isinstance(self.room_name, list) == True):
			for name in self.room_name:
				self.created_rooms[name] = self.room_type
			return self.created_rooms
		else:
			self.created_rooms[self.room_name] = self.room_type
			return self.created_rooms


class Office(Room):
	
	def __init__(self):
		self.max_occupants = 4
		self.all_rooms = {}

	def create_room(self, room_name, room_type):
		super(Office, self).__init__(room_name, room_type)
		self.all_rooms = super(Office, self).create_room(self.room_name, self.room_type)
		return	self.all_rooms


class LivingSpace(Room):
	
	def __init__(self):
		self.max_occupants = 6
		self.all_rooms = {}

	def create_room(self, room_name, room_type):
		super(LivingSpace, self).__init__(room_name, room_type)
		self.all_rooms = super(LivingSpace, self).create_room(self.room_name, self.room_type)
		return self.all_rooms


class Person(object):

	def __init__(self, person_name = [], person_type = ""):
		self.person_name = person_name
		self.person_type = person_type
		self.all_persons = []

	def add_person(self, person_name, person_type, wants_accommodation = 'N'):
		self.person_name = person_name
		self.person_type = person_type
		return


class Staff(Person):
	
	def __init__(self):
		self.all_persons = []

	def add_person(self, person_name, person_type, wants_accommodation = 'N'):
		super(Staff, self).__init__(person_name, person_type, )
		self.wants_accommodation = wants_accommodation
		if(self.wants_accommodation == 'Y'):
			return "Staff are not allocated living quarters."
		else:
			self.all_persons = [self.person_name, self.person_type]
			return self.all_persons


class Fellow(Person):
	
	def __init__(self):
		self.all_persons = []

	def add_person(self, person_name, person_type, wants_accommodation = 'N'):
		super(Fellow, self).__init__(person_name, person_type)
		self.wants_accommodation = wants_accommodation
		if(not self.wants_accommodation):
			self.all_persons = [self.person_name, self.person_type, 'N']
		else:
			self.all_persons = [self.person_name, self.person_type, self.wants_accommodation]
		return self.all_persons


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
		if arguments['create_room'] and arguments['<room_type>'] == "Office":
			room_instance = Office()
			room_result = room_instance.create_room(
				arguments['<room_name>'], arguments['<room_type>'])
			if(isinstance(room_result, dict)):
				for room in room_result:
					print("An Office called {} has been successfully created!".format(
						room))
			else:
				print(room_result)
		
		elif arguments['create_room'] and arguments['<room_type>'] == "Livingspace":
			room_instance = LivingSpace()
			room_result = room_instance.create_room(
				arguments['<room_name>'], arguments['<room_type>'])
			if(isinstance(room_result, dict)):
				for room in room_result:
					print("A Living Space called {} has been successfully created!".format(
						room))
			else:
				print(room_result)

		elif arguments['add_person'] and arguments['Fellow']:
			person_instance = Fellow()
			person_result = person_instance.add_person(" ".join(arguments['<person_name>']),
				'Fellow', arguments['<wants_accommodation>'])
			if (isinstance(person_result, str)):
				print(person_result)
			else:
				for person in person_result:
					print(person)
			

		elif arguments['add_person'] and arguments['Staff']:
			person_instance = Staff()
			person_result = person_instance.add_person(" ".join(arguments['<person_name>']),
				'Staff', arguments['<wants_accommodation>'])
			if (isinstance(person_result, str)):
				print(person_result)
			else:
				for person in person_result:
					print(person)


