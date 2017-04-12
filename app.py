import cmd
import random
import os
import sqlite3
from model.room import Room, Office, LivingSpace
from model.person import Person, Staff, Fellow
from docopt import docopt, DocoptExit


#class to make the app interactive
class Dojo (cmd.Cmd):
    intro   = '\nWelcome to the dojo program!\n\nType help for assistance and exit to leave.'
    prompt  = '\nDojo >>>'
    created_rooms = {}
    created_persons = {}
    room_allocation = {}
    living_allocation = {}

    #function create an office
    def dojo_create_office(self, room_name, room_type):
    	
    	if(isinstance(room_name, list)):
    		if(self.created_rooms):
    			for r in room_name:
    				if(r in self.created_rooms):
    					print("Room already exists!")
    					return
    		for room in room_name:
    			if(not room.isalpha()):
    				print("Use alphabet (a-z) characters for the room name and room type")
    				return
    	else:
    		if(not room_name.isalpha() or not room_name.isalpha()):
    			return "Use alphabet (a-z) characters for the room name and room type"

    	office_instance = Office()
    	office_result = office_instance.create_room(room_name, room_type)
    	self.created_rooms.update(office_result)
    	for office in office_result:
    		print("An Office called {} has been successfully created!".format(office))

    #function to create a living space
    def dojo_create_livingspace(self, room_name, room_type):

    	if(isinstance(room_name, list)):
    		if(self.created_rooms):
    			for r in room_name:
    				if(r in self.created_rooms):
    					print("Room already exists!")
    					return
    		for room in room_name:
    			if(not room.isalpha()):
    				print("Use alphabet (a-z) characters for the room name and room type")
    				return
    	else:
    		if(not room_name.isalpha() or not room_name.isalpha()):
    			return "Use alphabet (a-z) characters for the room name and room type"

    	livingspace_instance = LivingSpace()
    	livingspace_result = livingspace_instance.create_room(room_name, room_type)
    	self.created_rooms.update(livingspace_result)
    	for livingspace in livingspace_result:
    		print("A Living Space called {} has been successfully created!".format(livingspace))

    #function to add a fellow
    def dojo_add_fellow(self, person_name, person_type, wants_accommodation):

    	error = "Use alphabet (a-z) characters for the person name, type and wants accomodation"

    	if(not wants_accommodation):
    		wants_accommodation = "N"

    	if(person_name in self.created_persons):
    		print(person_type, person_name, "Already exists!")
    		return

    	if(not person_name.replace(' ', '').isalpha() or not person_type.isalpha() or not wants_accommodation.isalpha()):
    		print(error)
    		return error

    	fellow_instance = Fellow()
    	fellow_result = fellow_instance.add_person(person_name, person_type, wants_accommodation)
    	if(not isinstance(fellow_result, list)):
    		print(fellow_result)
    		return
    	self.created_persons.update({fellow_result[0] : [fellow_result[1], fellow_result[2]]})
    	print(fellow_result[1],fellow_result[0],"has been successfully added,")
    	if(self.allocate_office(fellow_result[0]) == 1 ):
    		officeallocation =  self.room_allocation[fellow_result[0]]
    		print(fellow_result[1], fellow_result[0],"has been allocated", officeallocation, self.created_rooms[officeallocation])
    	else:
    		print("No offices available for allocation")

    	if(wants_accommodation == 'Y' and self.allocate_livingspace(fellow_result[0]) == 1 ):
    		livingallocation =  self.living_allocation[fellow_result[0]]
    		print(fellow_result[1], fellow_result[0],"has been allocated", livingallocation, self.created_rooms[livingallocation])
    	else:
    		print("No living spaces allocated")

    #function to add a staff
    def dojo_add_staff(self, person_name, person_type, wants_accommodation):

    	error = "Use alphabet (a-z) characters for the person name, type and wants accomodation"

    	if(not wants_accommodation):
    		wants_accommodation = "N"

    	if(person_name in self.created_persons):
    		print(person_type, person_name, "Already exists!")
    		return

    	if(not person_name.replace(' ', '').isalpha() or not person_type.isalpha() or not wants_accommodation.isalpha()):
    		print(error)
    		return error

    	staff_instance = Staff()
    	staff_result = staff_instance.add_person(person_name, person_type, wants_accommodation)
    	if(not isinstance(staff_result, list)):
    		print(staff_result)
    		return
    	self.created_persons.update({staff_result[0] : [staff_result[1], staff_result[2]]})
    	print(staff_result[1],staff_result[0],"has been successfully added.")
    	if(self.allocate_office(staff_result[0])  == 1):
    		allocation =  self.room_allocation[staff_result[0]]
    		print(staff_result[1], staff_result[0],"has been allocated", allocation, self.created_rooms[allocation])
    	else:
    		print("No offices available for allocation")

    #function to create a file
    def dojo_create_file(self, filename, data = {}):

    	if(not filename.isalpha()):
    		return "Use alphabet (a-z) characters for the file name"
    	else:
    		filename = ''.join(["files/", filename, ".txt"])
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
	    				file_handler.write(allocation)
	    				file_handler.write('\n=======================================\n')
	    				file_handler.write(','.join([name for name, room in self.living_allocation.items() if room == allocation]))
	    				file_handler.write('\n\n')
	    		if(self.room_allocation):
	    			allocated = self.room_allocation.values()
	    			allocated = list(set(allocated))
	    			for allocation in allocated:
	    				file_handler.write(allocation)
	    				file_handler.write('\n=======================================\n')
	    				file_handler.write(','.join([name for name, room in self.room_allocation.items() if room == allocation]))
	    				file_handler.write('\n\n')
    		file_handler.close()
    		return "File {} created".format(filename)

    #function to get inputs to create a room
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

        except (KeyboardInterrupt, SystemExit):
        	print("System shut down. Thank you.")

        else:
        	if(arguments['<room_type>'] == "Office" or arguments['<room_type>'] == "office"):
        		self.dojo_create_office(arguments['<room_name>'], arguments['<room_type>'])
        	elif(arguments['<room_type>'] == "Livingspace" or arguments['<room_type>'] == "livingspace"):
        		self.dojo_create_livingspace(arguments['<room_name>'], arguments['<room_type>'])
        	else:
        		print("Indicate the office type: Office or Livingspace")
        		

    #function to get inputs to add a person
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

        except (KeyboardInterrupt, SystemExit):
        	print("System shut down. Thank you.")

        else:
        	if arguments['Fellow']:
        		self.dojo_add_fellow(" ".join(arguments['<person_name>']),'Fellow', arguments['<wants_accommodation>'])	

        	elif arguments['Staff']:
        		self.dojo_add_staff(" ".join(arguments['<person_name>']),'Staff', arguments['<wants_accommodation>'])
        		
    
    #function to allocate a room to a person
    def allocate_office(self, person_name):
    	office_max_occupants = Office().max_occupants

    	if(len(self.created_rooms) > 0):
    		
    		for room_name,room_type in self.created_rooms.items():
    			count = 1
    			for key, value in self.room_allocation.items():
    				if value == room_name:
    					count += 1

    			if(room_type == "Office" and count <= office_max_occupants):
    				self.room_allocation.update({person_name:room_name})
    				return 1

    #function to allocate a livingspace to a person
    def allocate_livingspace(self, person_name):
    	livingspace_max_occupants = LivingSpace().max_occupants

    	if(len(self.created_rooms) > 0):
    		
    		for room_name,room_type in self.created_rooms.items():
    			count = 1
    			for key, value in self.living_allocation.items():
    				if value == room_name:
    					count += 1

    			if(room_type == "Livingspace" and count <= livingspace_max_occupants):
    				self.living_allocation.update({person_name:room_name})
    				return 1

    #function to show specific room allocation
    def do_print_room(self, arg):
    	
    	"""
        Usage: 
            print_room <room_name>
        """
    	
    	try:
    		arguments = docopt(self.do_print_room.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
    		print("System shut down. Thank you.")

    	else:
        	if(len(self.room_allocation) != 0):
        		for key, value in self.room_allocation.items():
        			if value == arguments['<room_name>']:
        				print(key,'office',value)
        	else:
        		print("No rooms allocated")
        	if(len(self.living_allocation) != 0):
        		for key, value in self.living_allocation.items():
        			if value == arguments['<room_name>']:
        				print(key,'living space',value)
        	else:
        		print("No rooms allocated")
        			

    #function to show room allocations
    def do_print_allocations(self, arg):
    	
    	"""
        Usage:
        	print_allocations [-o FILE]
        """
    	
    	try:
    		arguments = docopt(self.do_print_allocations.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
    		print("System shut down. Thank you.")

    	else:
    		if(self.room_allocation):
    			for key, values in self.room_allocation.items():
    				print(key, values)
    			for key, values in self.living_allocation.items():
    				print(key, values)
    			if(arguments['FILE'] and arguments['-o']):
    				print(self.dojo_create_file(arguments['FILE'], {'allocation':1}))
    		else:
    			print("No room allocations")

    #function display unallocated persons
    def do_print_unallocated(self, arg):
    	
    	"""
        Usage:
        	print_unallocated [-o FILE]
        """
    	
    	try:
    		arguments = docopt(self.do_print_unallocated.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
    		print("System shut down. Thank you.")

    	else:
    		unallocated = []
    		if(self.created_persons):
    			for key, values in self.created_persons.items():
    				if key not in self.room_allocation:
    					unallocated.append(key)
    				if key not in self.living_allocation:
    					unallocated.append(key)
    				unallocated = list(set(unallocated))
    				print(''.join(unallocated))
    		else:
    			print("No persons created") 
    				
    			if(arguments['FILE'] and arguments['-o']):
    				print(self.dojo_create_file(arguments['FILE'], unallocated))

    #function to reallocate persons
    def dojo_reallocate_person(self, person_identifier, new_room_name):

    	full_name = ' '.join(person_identifier)

    	if(self.created_persons and full_name not in self.created_persons):
    		return "Person {} does not exist".format(full_name)
    	elif(self.created_rooms and new_room_name not in self.created_rooms):
    		return "Room {} does not exist".format(new_room_name)
    	else:
    		if(self.room_allocation[full_name]):
    			self.room_allocation[full_name] = new_room_name
    			return "{} has been allocated to {}".format(full_name, new_room_name)
    		
    		if(self.living_allocation[full_name]):
    			self.living_allocation[full_name] = new_room_name
    			return "{} has been allocated to {}".format(full_name, new_room_name)
    		


    #function to take variables to reallocate persons
    def do_reallocate_person(self, arg):
    	
    	"""
        Usage:
        	reallocate_person <person_identifier> [<person_identifier>] <new_room_name>
        """

    	try:
        	arguments = docopt(self.do_reallocate_person.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
        	print("System shut down. Thank you.")

    	else:
        	if(self.room_allocation):
        		print(self.dojo_reallocate_person(arguments['<person_identifier>'], arguments['<new_room_name>']))
        	else:
        		print("No room allocations")

    #function to take variables to reallocate persons
    def do_load_people(self, arg):
    	
    	"""
        Usage:
        	load_people
        """

    	try:
        	arguments = docopt(self.do_load_people.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
        	print("System shut down. Thank you.")

    	else:
    		if(os.stat('files/load.txt').st_size == 0):
    			print("The file is empty")
    			return
    		with open('files/load.txt') as f:
        		file_input = [line.strip() for line in f.readlines()]
        		for people in file_input:
        			full_name = ' '.join([people.split()[0], people.split()[1]])
        			person_type = people.split()[2]
        			if(len(people.split()) == 4):
        				wants_accommodation = people.split()[3]
        			else:
        				wants_accommodation = 'N'
        			if(person_type == "FELLOW"):
        				self.dojo_add_fellow(full_name, person_type, wants_accommodation)
        			else:
        				self.dojo_add_staff(full_name, person_type, wants_accommodation)
    
    #function to save state to db
    def do_save_state(self, arg):
    	
    	"""
        Usage:
        	save_state
        """

    	try:
        	arguments = docopt(self.do_save_state.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
        	print("System shut down. Thank you.")

    	else:
    		try:
	        	connection = sqlite3.connect(r"E:/Dojo/v2/Adams-Kariuki-Dojo-Project/db/dojodb")
	        	db_cursor = connection.cursor()
	        	db_cursor.execute('CREATE TABLE IF NOT EXISTS dojo_room (room_name text PRIMARY KEY, room_type text not null);')
	        	db_cursor.execute('CREATE TABLE IF NOT EXISTS dojo_person (person_name text PRIMARY KEY, person_type text not null, wants_accomodation text not null);')
	        	db_cursor.execute('CREATE TABLE IF NOT EXISTS dojo_allocation (person_name text not null, room_name text not null);')
	        	if(self.created_rooms):
	        		for key, val in self.created_rooms.items():
	        			db_cursor.execute("INSERT OR REPLACE INTO dojo_room (room_name, room_type) VALUES ('{v1}', '{v2}')".format(v1=key, v2=val))
	        	if(self.created_persons):
	        		for key, val in self.created_persons.items():
	        			db_cursor.execute("INSERT OR REPLACE INTO dojo_person (person_name, person_type, wants_accomodation) VALUES ('{v1}', '{v2}', '{v3}')".format(v1=key, v2=val[0], v3=val[1]))
	        	if(self.room_allocation):
	        		for key, val in self.room_allocation.items():
	        			db_cursor.execute("INSERT OR REPLACE INTO dojo_allocation (person_name, room_name) VALUES ('{v1}', '{v2}')".format(v1=key, v2=val))
	        	if(self.living_allocation):
	        		for key, val in self.living_allocation.items():
	        			db_cursor.execute("INSERT OR REPLACE INTO dojo_allocation (person_name, room_name) VALUES ('{v1}', '{v2}')".format(v1=key, v2=val))
	        	connection.commit()
	        	connection.close()
	    	except Exception as e:
	        	print('Error:',e)

    #function to load state from db
    def do_load_state(self, arg):
    	
    	"""
        Usage:
        	load_state [<dojodb>]
        """

    	try:
        	arguments = docopt(self.do_load_state.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
        	print("System shut down. Thank you.")

    	else:
    		try:
    			path = r'E:/Dojo/v2/Adams-Kariuki-Dojo-Project/db/dojodb'
    			if(arguments['<dojodb>'] and arguments['<dojodb>'].isalpha()):
	    			path = ''.join(['E:/Dojo/v2/Adams-Kariuki-Dojo-Project/db/', arguments['<dojodb>']])
		    		if(os.path.exists(path) == False):
		    			print("database {} does not exist.".format(arguments['<dojodb>']))
		    		else:
			    		connection = sqlite3.connect(path)
			    		db_cursor = connection.cursor()
			    		db_cursor.execute('SELECT * FROM dojo_person')
			    		for room_data in db_cursor.fetchall():
			    			self.created_persons.update({room_data[0]:[room_data[1], room_data[2]]})
			    		db_cursor.execute('SELECT * FROM dojo_room')
			    		for room_data in db_cursor.fetchall():
			    			self.created_rooms.update({room_data[0]: room_data[1]})
			    		db_cursor.execute('SELECT * FROM dojo_allocation')
			    		for room_data in db_cursor.fetchall():
			    			if(self.created_rooms[room_data[1]] == 'Office'):
			    				self.room_allocation.update({room_data[0]: room_data[1]})
			    			else:
			    				self.living_allocation.update({room_data[0]: room_data[1]})
	    				connection.close()
	    				print("Data loaded...")
	    		else:
	    			print("Use alphabet (a-z) characters for the database name")
	    	except Exception as e:
	        	print('Error:',e)     			

    #function to exit when 'exit' is typed
    def do_exit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        return True

    def do_cls(self, arg):
    	os.system('cls')

#execute main code block
if __name__ == '__main__':
	
	try:
		Dojo().cmdloop()
	
	except (KeyboardInterrupt, SystemExit):
		print("System shut down. Thank you.")