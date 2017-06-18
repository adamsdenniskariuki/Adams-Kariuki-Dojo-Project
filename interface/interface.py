import os
from random import shuffle
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.person import Staff, Fellow
from model.room import Office, LivingSpace
from model.orm_model import Rooms, Persons, Allocations, Unallocated, Base


# class to hold all the controllers
class Interface(object):

	all_rooms = {}
	all_persons = {}
	office_allocation = {}
	living_allocation = {}
	without_offices = {}
	without_living = {}

	# function create an office
	def create_office(self, rooms, room_type):
		output = []
		for room in rooms:
			
			if(room in self.all_rooms):
				output.append("Room {} already exists!".format(room))
				rooms.remove(room)
			
			if(not room.isalpha()):
				output.append("Use a-z only for the room name and room type")
				rooms.remove(room)

		if(len(rooms) > 0):
			office_instance = Office(rooms, room_type)
			for office in office_instance.room_name:
				self.all_rooms[office] = office_instance.room_type
				output.append("\nAn Office called {} has been successfully created!".format(office))

		return '\n'.join(output)

	# function to create a living space
	def create_livingspace(self, rooms, room_type):

		output = []
			
		for room in rooms:
			
			if(room in self.all_rooms):
				output.append("Room {} already exists!".format(room))
				rooms.remove(room)
			
			if(not room.isalpha()):
				output.append("Use a-z only for the room name and room type")
				rooms.remove(room)
		
		if(len(rooms) > 0):
			livingspace_instance = LivingSpace(rooms, room_type)
			for livingspace in livingspace_instance.room_name:
				self.all_rooms[livingspace] = livingspace_instance.room_type
				output.append("A Living Space called {} has been successfully created!".format(livingspace))

		return '\n'.join(output)

	# function to add a fellow
	def add_fellow(self, person_name, wants_accommodation='N'):

		output = []

		if(not person_name.replace(' ', '').isalpha() or not wants_accommodation.isalpha()):
			output.append("Use a-z only for the person name, type and wants accomodation")

		if(len(output) == 0):

			fellow_instance = Fellow(person_name, wants_accommodation)
			self.all_persons.update({fellow_instance.id:
				[fellow_instance.person_name, fellow_instance.person_type, fellow_instance.wants_accommodation]})
			print(fellow_instance.id)
			output.append(' '.join([fellow_instance.person_type, fellow_instance.person_name,
				"has been successfully added,"]))

			if(self.allocate_office(fellow_instance.id) == 1):
				officeallocation = self.office_allocation[fellow_instance.id]
				output.append(' '.join([fellow_instance.person_type, fellow_instance.person_name,
					"has been allocated", officeallocation, self.all_rooms[officeallocation]]))
			else:
				self.without_offices.update({fellow_instance.id:"Office"})
				output.append("No offices available for allocation")

			if(wants_accommodation.lower() == 'y'):
				if(self.allocate_livingspace(fellow_instance.id) == 1):
					livingallocation = self.living_allocation[fellow_instance.id]
					output.append(' '.join([fellow_instance.person_type, fellow_instance.person_name,
						"has been allocated", livingallocation, self.all_rooms[livingallocation]]))
				else:
					self.without_living.update({fellow_instance.id:"LivingSpace"})
			else:
				output.append("No living spaces allocated")

		return '\n'.join(output)

	# function to add a staff
	def add_staff(self, person_name, wants_accommodation='N'):

		output = []

		if(not person_name.replace(' ', '').isalpha() or not wants_accommodation.isalpha()):
			output.append("Use a-z only for the person name, type and wants accomodation")

		if(len(output) == 0):

			staff_instance = Staff(person_name)
			self.all_persons.update({staff_instance.id:
				[staff_instance.person_name, staff_instance.person_type, staff_instance.wants_accommodation]})
			print(staff_instance.id)
			output.append(' '.join([staff_instance.person_type, staff_instance.person_name,
				"has been successfully added."]))

			if(wants_accommodation.lower() == "y"):
				output.append("Staff members are not allocated living quarters")

			if(self.allocate_office(staff_instance.id) == 1):
				allocation = self.office_allocation[staff_instance.id]
				output.append(' '.join([staff_instance.person_type, staff_instance.person_name,
					"has been allocated", allocation, self.all_rooms[allocation]]))
			else:
				self.without_offices.update({staff_instance.id:"Office"})
				output.append("No offices available for allocation")

		return '\n'.join(output)

	# function to create a file
	def create_file(self, filename, data):

		output = []

		if(not filename.isalpha()):
			output.append("Use a-z only for the file name")
		else:
			filename = ''.join(["./files/", filename, ".txt"])
			
			if(os.path.exists(filename)):
				output.append("The file already exists. Choose another file name.")
			file_handler = open(filename, "w")
			
			if(isinstance(data, list)):
				for key in data:
					file_handler.write(' '.join([key, '\n']))
			else:
				if(self.living_allocation):
					allocated = self.living_allocation.values()
					allocated = list(set(allocated))
					for allocation in allocated:
						file_handler.write(' '.join(
							[allocation, self.all_rooms[allocation]]))
						file_handler.write(
							'\n=======================================\n')
						file_handler.write(','.join(
							[self.all_persons[pid][0] for pid, room in
								self.living_allocation.items()
								if room == allocation]))
						file_handler.write('\n\n')
				
				if(self.office_allocation):
					allocated = self.office_allocation.values()
					allocated = list(set(allocated))
					for allocation in allocated:
						file_handler.write(' '.join(
							[allocation, self.all_rooms[allocation]]))
						file_handler.write(
							'\n=======================================\n')
						file_handler.write(','.join(
							[self.all_persons[pid][0] for pid, room in
								self.office_allocation.items()
								if room == allocation]))
						file_handler.write('\n\n')
			
			file_handler.close()
			output.append("File {} created".format(filename))

		return '\n'.join(output)

	# function to allocate a room to a person
	def allocate_office(self, person_id):

		rooms = [room_name for room_name, room_type in list(self.all_rooms.items()) if(room_type=="Office")]
		shuffle(rooms)

		if(len(rooms) > 0):
			for room_name in rooms:
				if(len([allocated_room for allocated_room in self.office_allocation.values() if(allocated_room == room_name)]) < 4):
					self.office_allocation.update({person_id: room_name})
					return 1
		return 0

	# function to allocate a livingspace to a person
	def allocate_livingspace(self, person_id):

		rooms = [room_name for room_name, room_type in list(self.all_rooms.items()) if(room_type=="LivingSpace")]
		shuffle(rooms)

		if(len(rooms) > 0):
			for room_name in rooms:
				if(len([allocated_room for allocated_room in self.living_allocation.values() if(allocated_room == room_name)]) < 4):
					self.living_allocation.update({person_id: room_name})
					return 1
		return 0

	#function to create the db
	def create_db(self, db_name):

		engine = create_engine('sqlite:///{}'.format(db_name))
		#engine = create_engine('postgres://postgres:healthcheck17@localhost/dojo')
		Base.metadata.create_all(engine)
		DBSession = sessionmaker(bind=engine)
		return DBSession()

	#save state orm
	def save_state_orm(self, db_name="dojo"):
		
		output = []
		if(not db_name.isalpha()):
			output.append("Use a-z for the database name")
		else:
			session = self.create_db(''.join(["db/", db_name, ".db"]))

			if(self.all_persons):
				for key, val in self.all_persons.items():
					new_person = Persons(key, val[0], val[1], val[2])
					session.merge(new_person)
					session.commit()

			if(self.all_rooms):
					for key, val in self.all_rooms.items():
						new_room = Rooms(key, val)
						session.merge(new_room)
						session.commit()

			if(self.office_allocation):
					for key, val in self.office_allocation.items():
						new_office_allocation = Allocations(key, val, self.all_rooms[val])
						session.merge(new_office_allocation)
						session.commit()

			if(self.living_allocation):
					for key, val in self.living_allocation.items():
						new_living_allocation = Allocations(key, val, self.all_rooms[val])
						session.merge(new_living_allocation)
						session.commit()

			if(self.without_offices):
					for key, val in self.without_offices.items():
						new_unallocated_person = Unallocated(key, val)
						session.merge(new_unallocated_person)
						session.commit()

			if(self.without_living):
					for key, val in self.without_living.items():
						new_unallocated_person = Unallocated(key, val)
						session.merge(new_unallocated_person)
						session.commit()

			output.append('All data saved...')
		return '\n'.join(output)

	#load state of db using orm
	def load_state_orm(self, db_name="dojo"):

		output = []
		if(os.path.exists(''.join(["db/", db_name, ".db"])) is False):
			output.append("database {} does not exist.".format(db_name))
		else:
			session = self.create_db(''.join(["db/", db_name, ".db"]))
			stored_persons = session.query(Persons).all()
			stored_rooms = session.query(Rooms).all()
			stored_allocations = session.query(Allocations).all()
			stored_unallocated = session.query(Unallocated).all()

			if stored_persons:
				for person_object in stored_persons:
					self.all_persons.update({person_object.pid: [
								person_object.person_name, person_object.person_type, person_object.wants_accomodation]})

			if stored_rooms:
				for room_object in stored_rooms:
					self.all_rooms.update({room_object.room_name: room_object.room_type})

			if stored_unallocated:
				for unallocated_object in stored_unallocated:
					if(unallocated_object.room_type == 'Office'):
						self.without_offices.update({unallocated_object.pid: unallocated_object.room_type})
					else:
						self.without_offices.update({unallocated_object.pid: unallocated_object.room_type})


			if stored_allocations:
				for room_object in stored_allocations:
					if(room_object.room_type == 'Office'):
						self.office_allocation.update({room_object.pid:room_object.room_name})
					else:
						self.living_allocation.update({room_object.pid:room_object.room_name})

			output.append("Data loaded...")
		return '\n'.join(output)

	# function to reallocate persons
	def reallocate_person(self, person_identifier, new_room_name):

		output = []
		pid_list = [pid if ' '.join(person_identifier) in data else 0
			for pid, data in list(self.all_persons.items()) if ' '.join(person_identifier) in data]

		if(self.all_persons and pid_list):
			pid = pid_list[0]
		else:
			output.append("Person {} does not exist".format(' '.join(person_identifier)))
		
		if(self.all_rooms):
			if(new_room_name not in self.all_rooms):
				output.append("Room {} does not exist".format(new_room_name))
		else:
			output.append("No rooms created")
		
		if(len(output) == 0):

			if(self.office_allocation and pid in self.office_allocation and self.all_rooms[new_room_name] == "Office"):
				if(len([room_name for room_name in list(self.office_allocation.values()) if new_room_name == room_name]) < 6):
					self.office_allocation[pid] = new_room_name
					output.append("{} has been re-allocated to {}".format(' '.join(person_identifier), new_room_name))
				else:
					output.append("Room {} is full.".format(new_room_name))

			elif(self.living_allocation and pid in self.living_allocation and self.all_rooms[new_room_name] == "LivingSpace"):
				if(len([room_name for room_name in list(self.living_allocation.values()) if new_room_name == room_name]) < 6):
					self.living_allocation[pid] = new_room_name
					output.append("{} has been re-allocated to {}".format(' '.join(person_identifier), new_room_name))
				else:
					output.append("Room {} is full.".format(new_room_name))
			else:
				output.append("{} has not been allocated an office or living space.".format(' '.join(person_identifier)))

		return '\n'.join(output)

	#function to print unallocated persons
	def print_unallocated(self, file_name="-1"):
		all_unallocated = []
		output = []
		if(self.all_persons):
			if(self.without_offices):
				for key, value in self.without_offices.items():
					output.append(' '.join([self.all_persons[key][0], value]))
					all_unallocated.append(' - '.join([self.all_persons[key][0], value]))
			if(self.without_living):
				for key, value in self.without_living.items():
					output.append(' '.join([self.all_persons[key][0], value]))
					all_unallocated.append(' - '.join([self.all_persons[key][0], value]))
				if(file_name != "-1"):
					output.append(self.create_file(file_name, all_unallocated))
			else:
				output.append("All persons allocated rooms.")
		else:
			output.append("No persons created")
		return '\n'.join(output)

	#function to print allocations
	def print_allocations(self, file_name="-1"):

		output = []
		if(self.office_allocation):
			for key, values in self.office_allocation.items():
				output.append(' '.join([self.all_persons[key][0], values, self.all_rooms[values]]))
		if(self.living_allocation):
			for key, values in self.living_allocation.items():
				output.append(' '.join([self.all_persons[key][0], values, self.all_rooms[values]]))
		if(file_name != "-1"):
			output.append(self.create_file(file_name, {'allocation':1}))
		if(len(output) == 0):
			output.append("No room allocations")
		return '\n'.join(output)

	#function to print the occupants of a room
	def print_room(self, room_name):

		output = []
		if(room_name not in self.all_rooms):
			output.append("Room {} does not exist.".format(room_name))
		else:
			if(len(self.office_allocation) != 0):
				for key, value in self.office_allocation.items():
					if value == room_name:
						output.append(' '.join([self.all_persons[key][0], 'office', value]))

			if(len(self.living_allocation) != 0):
				for key, value in self.living_allocation.items():
					if value == room_name:
						output.append(' '.join([self.all_persons[key][0], 'living space', value]))
		return '\n'.join(output)

	#function to load persons from a text file
	def load_people(self):

		output = []
		if(os.stat('./files/load.txt').st_size == 0):
			output.append("The file is empty")
		with open('./files/load.txt') as f:
			file_input = [line.strip() for line in f.readlines()]
			for people in file_input:
				full_name = ' '.join([people.split()[0], people.split()[1]
									  ])
				person_type = people.split()[2]
				if(len(people.split()) == 4):
					wants_accommodation = people.split()[3]
				else:
					wants_accommodation = 'N'
				if(person_type == "FELLOW"):
					self.add_fellow(full_name, wants_accommodation)
				else:
					self.add_staff(full_name)
		output.append("Data has been loaded from text file")
		return '\n'.join(output)