

import os
import random
import sqlite3
from model.person import Person, Staff, Fellow
from model.room import Room, Office, LivingSpace


# class to hold all the controllers
class Controllers(object):

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
	def add_fellow(self, person_name, person_type, wants_accommodation):

		add_error = 0
		error = "Use a-z only for the person name, type and wants accomodation"

		if(not wants_accommodation):
			wants_accommodation = "N"

		if(person_name in self.all_persons):
			print(person_type, person_name, "Already exists!")
			add_error = 1

		if(not person_name.replace(' ', '').isalpha() or not person_type.
				isalpha() or not wants_accommodation.isalpha()):
			add_error = 1
			print(error)
			return error

		if(add_error == 0):

			fellow_instance = Fellow(person_name, person_type,
													   wants_accommodation)
			self.all_persons.update({fellow_instance.person_name:
				[fellow_instance.person_type, fellow_instance.wants_accommodation]})
			print(fellow_instance.person_type, fellow_instance.person_name,
				  "has been successfully added,")

			if(self.allocate_office(fellow_instance.person_name) == 1):
				officeallocation = self.office_allocation[fellow_instance.person_name]
				print(fellow_instance.person_type, fellow_instance.person_name,
					"has been allocated",
					officeallocation, self.all_rooms[officeallocation])
			else:
				self.unallocated_persons.update({fellow_instance.person_name:"Office"})
				print("No offices available for allocation")

			if(wants_accommodation == 'Y' and self.allocate_livingspace(
					fellow_instance.person_name) == 1):
				livingallocation = self.living_allocation[fellow_instance.person_name]
				print(fellow_instance.person_type, fellow_instance.person_name, "has been allocated",
					  livingallocation, self.all_rooms[livingallocation])
			else:
				self.unallocated_persons.update({fellow_instance.person_name:"LivingSpace"})
				print("No living spaces allocated")

	# function to add a staff
	def add_staff(self, person_name, person_type, wants_accommodation):

		add_error = 0
		error = "Use a-z only for the person name, type and wants accomodation"

		if(person_name in self.all_persons):
			print(person_type, person_name, "Already exists!")
			add_error = 1

		if(not person_name.replace(' ', '').isalpha() or not person_type.
				isalpha() or not wants_accommodation.isalpha()):
			add_error = 1
			print(error)
			return error

		if(add_error == 0):

			staff_instance = Staff(person_name, person_type,
													 wants_accommodation)
			self.all_persons.update({staff_instance.person_name:
				[staff_instance.person_type, staff_instance.wants_accommodation]})
			print(staff_instance.person_type, staff_instance.person_name, "has been successfully added.")

			if(wants_accommodation == "Y" or wants_accommodation == "y"):
				print("Staff members are not allocated living quarters")

			if(self.allocate_office(staff_instance.person_name) == 1):
				allocation = self.office_allocation[staff_instance.person_name]
				print(staff_instance.person_type, staff_instance.person_name, "has been allocated",
					  allocation, self.all_rooms[allocation])
			else:
				self.unallocated_persons.update({staff_instance.person_name:"Office"})
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
							[name for name, room in
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
							[name for name, room in
								self.office_allocation.items()
								if room == allocation]))
						file_handler.write('\n\n')
			file_handler.close()
			return "File {} created".format(filename)

	# function to allocate a room to a person
	def allocate_office(self, person_name):
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
					self.office_allocation.update({person_name: room_name})
					return 1

	# function to allocate a livingspace to a person
	def allocate_livingspace(self, person_name):
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
					self.living_allocation.update({person_name: room_name})
					return 1

	#save data to the database
	def save_state(self, db_name):

		try:
			path = r"./db/"
			if(db_name and db_name.isalpha()):
				path = ''.join([path, db_name])
			else:
				path = r"./db/dojodb"
			connection = sqlite3.connect(path)
			db_cursor = connection.cursor()
			db_cursor.execute(
				''.join(['CREATE TABLE IF NOT EXISTS dojo_room (',
						'room_name text PRIMARY KEY,' +
						 'room_type text not null);']))
			db_cursor.execute(
				'CREATE TABLE IF NOT EXISTS dojo_person (' +
				'person_name text PRIMARY KEY,' +
				'person_type text not null,' +
				'wants_accomodation text not null);')
			db_cursor.execute(
				'CREATE TABLE IF NOT EXISTS dojo_allocation('
				'person_name text not null,' +
				'room_name text not null,' +
				'room_type text not null);')
			db_cursor.execute(
				'CREATE TABLE IF NOT EXISTS dojo_unallocated('
				'person_name text not null,' +
				'room_type text not null);')
			if(self.all_rooms):
				for key, val in self.all_rooms.items():
					db_cursor.execute(
						"INSERT OR REPLACE INTO dojo_room" +
						"(room_name, room_type)" +
						"VALUES ('{v1}', '{v2}')" .format(
							v1=key, v2=val))
			if(self.all_persons):
				for key, val in self.all_persons.items():
					db_cursor.execute(
						"INSERT OR REPLACE INTO dojo_person" +
						"(person_name, person_type, wants_accomodation)" +
						"VALUES ('{v1}', '{v2}', '{v3}')"
						.format(
							v1=key, v2=val[0],
							v3=val[1]))
			if(self.office_allocation):
				for key, val in self.office_allocation.items():
					db_cursor.execute(
						"UPDATE dojo_allocation SET room_name = '{v1}'" +
						"WHERE person_name = '{v2}' AND room_type = '{v3}'"
						.format(
							v1=val, v2=key,
							v3=self.all_rooms[val]))
					if(db_cursor.rowcount != 1):
						db_cursor.execute(
							"INSERT INTO dojo_allocation" +
							"(person_name, room_name, room_type)" +
							"VALUES ('{v1}', '{v2}', '{v3}')"
							.format(
								v1=key, v2=val,
								v3=self.all_rooms[val]))
			if(self.living_allocation):
				for key, val in self.living_allocation.items():
					db_cursor.execute(
						"UPDATE dojo_allocation SET room_name = '{v1}'" +
						"WHERE person_name = '{v2}' AND room_type = '{v3}'"
						.format(
							v1=val, v2=key,
							v3=self.all_rooms[val]))
					if(db_cursor.rowcount != 1):
						db_cursor.execute(
							"INSERT INTO dojo_allocation " +
							"(person_name, room_name, room_type)" +
							"VALUES ('{v1}', '{v2}', '{v3}')" .format(
								v1=key, v2=val,
								v3=self.all_rooms[val]))
			if(self.unallocated_persons):
				for key, val in self.unallocated_persons.items():
					db_cursor.execute(
						"UPDATE dojo_unallocated SET person_name = '{v1}', room_type = '{v2}'" +
						"WHERE person_name = '{v1}' AND room_type = '{v2}'"
						.format(
							v1=key, v2=val))
					if(db_cursor.rowcount != 1):
						db_cursor.execute(
							"INSERT INTO dojo_unallocated " +
							"(person_name, room_type)" +
							"VALUES ('{v1}', '{v2}')" .format(
								v1=key, v2=val))
			connection.commit()
			connection.close()
			print('All data saved...')
		except Exception as e:
			print('Error:', e)

	#function to load state from the database
	def load_state(self, db_name):

		try:
			if(db_name and db_name.isalpha()):
				path = ''.join(['./db/', db_name])
				if(os.path.exists(path) is False):
					print("database {} does not exist.".format(arguments[
						'<dojodb>']))
				else:
					connection = sqlite3.connect(path)
					db_cursor = connection.cursor()
					db_cursor.execute('SELECT * FROM dojo_person')
					for room_data in db_cursor.fetchall():
						self.all_persons.update({room_data[0]: [
							room_data[1], room_data[2]]})
					db_cursor.execute('SELECT * FROM dojo_room')
					for room_data in db_cursor.fetchall():
						self.all_rooms.update({room_data[0]: room_data
												   [1]})
					db_cursor.execute('SELECT * FROM dojo_allocation')
					for room_data in db_cursor.fetchall():
						if(self.all_rooms[room_data[1]] == 'Office'):
							self.office_allocation.update({room_data[0]:
														   room_data[1]})
						else:
							self.living_allocation.update({room_data[0]:
														   room_data[1]})
					db_cursor.execute('SELECT * FROM dojo_unallocated')
					for unalloc_data in db_cursor.fetchall():
						self.unallocated_persons.update({unalloc_data[0]: unalloc_data
												   [1]})
					connection.close()
					print("Data loaded...")
			else:
				print(
					"Use alphabet (a-z) characters for the database name")
		except Exception as e:
			print('Error:', e)

	# function to reallocate persons
	def reallocate_person(self, person_identifier, new_room_name):

		if(self.office_allocation):

			full_name = ' '.join(person_identifier)

			if(self.all_persons and full_name not in self.all_persons):
				print("Person {} does not exist".format(full_name))
			elif(self.all_rooms and new_room_name not in self.all_rooms):
				print("Room {} does not exist".format(new_room_name))
			else:
				if(full_name in self.office_allocation):
					office_max_occupants = 6
					count = 1
					reallocated = 0
					for person_name, room_name in self.office_allocation.items():
						if new_room_name == room_name:
							count += 1
					if(count <= office_max_occupants):
						reallocated = 1
						self.office_allocation[full_name] = new_room_name
						print("{} has been re-allocated to {}".format(
							full_name, new_room_name))
					if(reallocated == 0):
						print("Room {} is full.".format(new_room_name))

				if(full_name in self.living_allocation):
					livingspace_max_occupants = 4
					count = 1
					reallocated = 0
					for person_name, room_name in self.living_allocation.items():
						if new_room_name == room_name:
							count += 1
					if(count <= livingspace_max_occupants):
						reallocated = 1
						self.living_allocation[full_name] = new_room_name
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
					print(key, value)

					all_unallocated.append(' - '.join([key, value]))
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
				print(key, values, self.all_rooms[values])
			found_allocation = 1
		if(self.living_allocation):
			for key, values in self.living_allocation.items():
				print(key, values, self.all_rooms[values])
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
						print(key, 'office', value)

			if(len(self.living_allocation) != 0):
				for key, value in self.living_allocation.items():
					if value == room_name:
						print(key, 'living space', value)

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

	#function to generate random numbers for the id
	def generate_id(self):

		generated_id = []
		for number in range(8):
			generated_id.append(str(random.randint(1,11)))
		return int(''.join(generated_id))
