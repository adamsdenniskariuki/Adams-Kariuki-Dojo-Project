import os
import random
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.person import Person, Staff, Fellow
from model.room import Room, Office, LivingSpace
from model.orm_model import Rooms, Persons, Allocations, Unallocated, Base


# class to hold all the controllers
class Interface(object):

	all_rooms = {}
	all_persons = {}
	office_allocation = {}
	living_allocation = {}
	unallocated_persons = {}

	# function create an office
	def create_office(self, room_name, room_type):
		
		input_error = 0
			
		for room in room_name:
			
			if(room in self.all_rooms):
				print("Room already exists!")
				input_error = 1
			
			if(not room.isalpha()):
				print(
					"Use a-z only for the room name and room type"
				)
				return "Use a-z only for the room name and room type"
				input_error = 1

		if(input_error == 0):
			office_instance = Office(room_name, room_type)
			for office in office_instance.room_name:
				self.all_rooms[office] = office_instance.room_type
				print("An Office called {} has been successfully created!".format(
					office))

	# function to create a living space
	def create_livingspace(self, room_name, room_type):

		input_error = 0
		error = "Use a-z only for the room name and room type"
			
		for room in room_name:
			
			if(room in self.all_rooms):
				print("Room already exists!")
				input_error = 1
			
			if(not room.isalpha()):
				print(error)
				return error
				input_error = 1		

		if(input_error == 0):
			livingspace_instance = LivingSpace(room_name, room_type)
			for livingspace in livingspace_instance.room_name:
				self.all_rooms[livingspace] = livingspace_instance.room_type
				print("A Living Space called {} has been successfully created!".
					  format(livingspace))

	# function to add a fellow
	def add_fellow(self, person_name, wants_accommodation):

		add_error = 0
		error = "Use a-z only for the person name, type and wants accomodation"

		if(not wants_accommodation):
			wants_accommodation = "N"

		if(person_name in self.all_persons):
			print(person_type, person_name, "Already exists!")
			add_error = 1

		if(not person_name.replace(' ', '').isalpha() or not wants_accommodation.isalpha()):
			add_error = 1
			print(error)
			return error

		if(add_error == 0):

			fellow_instance = Fellow(person_name, wants_accommodation)
			self.all_persons.update({fellow_instance.id:
				[fellow_instance.person_name, fellow_instance.person_type, fellow_instance.wants_accommodation]})
			print(fellow_instance.person_type, fellow_instance.person_name,
				  "has been successfully added,")

			if(self.allocate_office(fellow_instance.id) == 1):
				officeallocation = self.office_allocation[fellow_instance.id]
				print(fellow_instance.person_type, fellow_instance.person_name,
					"has been allocated",
					officeallocation, self.all_rooms[officeallocation])
			else:
				self.unallocated_persons.update({fellow_instance.id:"Office"})
				print("No offices available for allocation")

			if(wants_accommodation == 'Y' and self.allocate_livingspace(
					fellow_instance.person_name) == 1):
				livingallocation = self.living_allocation[fellow_instance.id]
				print(fellow_instance.person_type, fellow_instance.person_name, "has been allocated",
					  livingallocation, self.all_rooms[livingallocation])
			else:
				self.unallocated_persons.update({fellow_instance.id:"LivingSpace"})
				print("No living spaces allocated")

	# function to add a staff
	def add_staff(self, person_name, wants_accommodation='N'):

		add_error = 0
		error = "Use a-z only for the person name, type and wants accomodation"

		if(person_name in self.all_persons):
			print(person_type, person_name, "Already exists!")
			add_error = 1

		if(not person_name.replace(' ', '').isalpha() or not wants_accommodation.isalpha()):
			add_error = 1
			print(error)
			return error

		if(add_error == 0):

			staff_instance = Staff(person_name)
			self.all_persons.update({staff_instance.id:
				[staff_instance.person_name, staff_instance.person_type, staff_instance.wants_accommodation]})
			print(staff_instance.person_type, staff_instance.person_name, "has been successfully added.")

			if(wants_accommodation == "Y" or wants_accommodation == "y"):
				print("Staff members are not allocated living quarters")

			if(self.allocate_office(staff_instance.id) == 1):
				allocation = self.office_allocation[staff_instance.id]
				print(staff_instance.person_type, staff_instance.person_name, "has been allocated",
					  allocation, self.all_rooms[allocation])
			else:
				self.unallocated_persons.update({staff_instance.id:"Office"})
				print("No offices available for allocation")

	# function to create a file
	def create_file(self, filename, data={}):

		if(not filename.isalpha()):
			return "Use a-z only for the file name"
		else:
			filename = ''.join(["./files/", filename, ".txt"])
			if(os.path.exists(filename)):
				return "The file already exists. Choose another file name."
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
			return "File {} created".format(filename)

	# function to allocate a room to a person
	def allocate_office(self, person_id):
		office_max_occupants = 6

		if(len(self.all_rooms) > 0):

			for room_name, room_type in sorted(
					self.all_rooms.items(),
					key=lambda x: random.random(), reverse=True):
				count = 1
				for key, value in self.office_allocation.items():
					if value == room_name:
						count += 1

				if(room_type == "Office" and count <= office_max_occupants):
					self.office_allocation.update({person_id: room_name})
					return 1

	# function to allocate a livingspace to a person
	def allocate_livingspace(self, person_id):
		livingspace_max_occupants = 4

		if(len(self.all_rooms) > 0):

			for room_name, room_type in sorted(
					self.all_rooms.items(),
					key=lambda x: random.random(), reverse=True):
				count = 1
				for key, value in self.living_allocation.items():
					if value == room_name:
						count += 1

				if(room_type == "Livingspace" and count <=
						livingspace_max_occupants):
					self.living_allocation.update({person_id: room_name})
					return 1

	#function to create the db
	def create_db(self, db_name):

		engine = create_engine('sqlite:///{}'.format(db_name))
		#engine = create_engine('postgres://postgres:healthcheck17@localhost/dojo')
		Base.metadata.create_all(engine)
		DBSession = sessionmaker(bind=engine)
		return DBSession()

	#save state orm
	def save_state_orm(self, db_name="dojo"):
		
		if(not db_name.isalpha()):
			print("Use a-z for the database name")
		else:
			db_name = "db/" + db_name + ".db"
			session = self.create_db(db_name)

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

			if(self.unallocated_persons):
					for key, val in self.unallocated_persons.items():
						new_unallocated_person = Unallocated(key, val)
						session.merge(new_unallocated_person)
						session.commit()

			print('All data saved...')

	#load state of db using orm
	def load_state_orm(self, db_name="dojo"):

		db_name = "db/" + db_name + ".db"
		
		if(os.path.exists(db_name) is False):
			print("database {} does not exist.".format(db_name))
		else:
			session = self.create_db(db_name)
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
					self.unallocated_persons.update({unallocated_object.pid: unallocated_object.room_type})

			if stored_allocations:
				for room_object in stored_allocations:
					if(room_object.room_type == 'Office'):
						self.office_allocation.update({room_object.pid:room_object.room_name})
					else:
						self.living_allocation.update({room_object.pid:room_object.room_name})

			print("Data loaded...")

	# function to reallocate persons
	def reallocate_person(self, person_identifier, new_room_name):

		if(self.office_allocation):

			full_name = ' '.join(person_identifier)
			pid = 0
			for key, value in self.all_persons.items():
				if(full_name == value[0]):
					pid = key

			if(self.all_persons and pid not in self.all_persons):
				print("Person {} does not exist".format(full_name))
			elif(self.all_rooms and new_room_name not in self.all_rooms):
				print("Room {} does not exist".format(new_room_name))
			else:

				if(pid in self.office_allocation):
					office_max_occupants = 6
					count = 1
					reallocated = 0
					for person_id, room_name in self.office_allocation.items():
						if new_room_name == room_name:
							count += 1
					if(count <= office_max_occupants):
						reallocated = 1
						self.office_allocation[pid] = new_room_name
						print("{} has been re-allocated to {}".format(
							full_name, new_room_name))
					if(reallocated == 0):
						print("Room {} is full.".format(new_room_name))

				if(pid in self.living_allocation):
					livingspace_max_occupants = 4
					count = 1
					reallocated = 0
					for person_id, room_name in self.living_allocation.items():
						if new_room_name == room_name:
							count += 1
					if(count <= livingspace_max_occupants):
						reallocated = 1
						self.living_allocation[pid] = new_room_name
						print("{} has been re-allocated to {}".format(
							full_name, new_room_name))
					if(reallocated == 0):
						print("Room {} is full.".format(new_room_name))
		
		else:
			print("No room allocations")

	#function to print unallocated persons
	def print_unallocated(self, file_name="-1"):
		all_unallocated = []
		if(self.all_persons):
			if(self.unallocated_persons):
				for key, value in self.unallocated_persons.items():
					print(self.all_persons[key][0], value)

					all_unallocated.append(' - '.join([self.all_persons[key][0], value]))
				if(file_name != "-1"):
					print(self.create_file(file_name, all_unallocated
												))
			else:
				print("All persons allocated rooms.")
		else:
			print("No persons created")

	#function to print allocations
	def print_allocations(self, file_name="-1"):

		found_allocation = 0
		if(self.office_allocation):
			for key, values in self.office_allocation.items():
				print(self.all_persons[key][0], values, self.all_rooms[values])
			found_allocation = 1
		if(self.living_allocation):
			for key, values in self.living_allocation.items():
				print(self.all_persons[key][0], values, self.all_rooms[values])
			found_allocation = 1
		if(file_name != "-1"):
			print(self.create_file(file_name, {'allocation':
															1}))
		if(found_allocation == 0):
			print("No room allocations")

	#function to print the occupants of a room
	def print_room(self, room_name):
		if(room_name not in self.all_rooms):
			print("Room", room_name, "does not exist.")
			return ("Room {} does not exist.".format(room_name))
		else:
			if(len(self.office_allocation) != 0):
				for key, value in self.office_allocation.items():
					if value == room_name:
						print(self.all_persons[key][0], 'office', value)

			if(len(self.living_allocation) != 0):
				for key, value in self.living_allocation.items():
					if value == room_name:
						print(self.all_persons[key][0], 'living space', value)

	#function to load persons from a text file
	def load_people(self):

		if(os.stat('./files/load.txt').st_size == 0):
			print("The file is empty")
			return
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
					self.add_fellow(full_name, person_type,
										 wants_accommodation)
				else:
					self.add_staff(full_name, person_type,
										wants_accommodation)