import cmd
import random
import os
from model.room import Room, Office, LivingSpace
from model.person import Person, Staff, Fellow
from docopt import docopt, DocoptExit


#class to make the app interactive
class Dojo (cmd.Cmd):
    intro   = '\nWelcome to the dojo program!\n\nType help for assistance and exit to leave.\n'
    prompt  = 'Dojo >>>'
    file    = None
    created_rooms = {}
    created_persons = {}
    room_allocation = {}

    #function create an office
    def dojo_create_office(self, room_name, room_type):

    	if(isinstance(room_name, list)):
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
    		for room in room_name:
    			if(not room.isalpha()):
    				print("Use alphabet (a-z) characters for the room name and room type")
    				return
    	else:
    		if(not room_name.isalpha() or not room_name.isalpha()):
    			return "Use alphabet (a-z) characters for the room name and room type"

    	livingspace_instance = LivingSpace()
    	livingspace_result = livingspace_instance.create_room(arguments['<room_name>'], arguments['<room_type>'])
    	self.created_rooms.update(livingspace_result)
    	for livingspace in livingspace_result:
    		print("A Living Space called {} has been successfully created!".format(livingspace))

    #function to create a living space
    def dojo_add_fellow(self, person_name, person_type, wants_accommodation):

    	error = "Use alphabet (a-z) characters for the person name, type and wants accomodation"

    	if(not wants_accommodation):
    		wants_accommodation = 'N'

    	if(not person_name.replace(' ', '').isalpha() or not person_type.isalpha() or not wants_accommodation.isalpha()):
    		print(error)
    		return error

    	fellow_instance = Fellow()
    	fellow_result = fellow_instance.add_person(person_name, person_type, wants_accommodation)
    	self.created_persons.update({fellow_result[0] : [fellow_result[1], fellow_result[2]]})
    	print(fellow_result[1],fellow_result[0],"has been successfully added,")
    	if(self.allocate_room(fellow_result[0]) == 1):
    		allocation =  self.room_allocation[fellow_result[0]]
    		print(fellow_result[1], fellow_result[0],"has been allocated", allocation, self.created_rooms[allocation])

    #function to create a living space
    def dojo_add_staff(self, person_name, person_type, wants_accommodation):

    	error = "Use alphabet (a-z) characters for the person name, type and wants accomodation"

    	if(not wants_accommodation):
    		wants_accommodation = 'N'

    	if(not person_name.replace(' ', '').isalpha() or not person_type.isalpha() or not wants_accommodation.isalpha()):
    		print(error)
    		return error

    	staff_instance = Staff()
    	staff_result = staff_instance.add_person(person_name, person_type, wants_accommodation)
    	self.created_persons.update({staff_result[0] : [staff_result[1], staff_result[2]]})
    	print(staff_result[1],staff_result[0],"has been successfully added.")
    	if(self.allocate_room(staff_result[0])  == 1):
    		allocation =  self.room_allocation[staff_result[0]]
    		print(staff_result[1], staff_result[0],"has been allocated", allocation, self.created_rooms[allocation])

    #function to create a room
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
        	if (arguments['<room_type>'] == "Office" or arguments['<room_type>'] == "office"):
        		self.dojo_create_office(arguments['<room_name>'], arguments['<room_type>'])

        	elif (arguments['<room_type>'] == "Livingspace" or arguments['<room_type>'] == "livingspace"):
        		self.dojo_create_livingspace(arguments['<room_name>'], arguments['<room_type>'])
        		

    #function to add a person
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
    def allocate_room(self, person_name):
    	office_max_occupants = Office().max_occupants
    	livingspace_max_occupants = LivingSpace().max_occupants

    	if(len(self.created_rooms) > 0):
    		rooms_list = []
    		for key, value in self.created_rooms.items():
    			rooms_list.append(key)

    		random_key = random.randint(0 , len(rooms_list) - 1)
    		room_allocated = rooms_list[random_key]
    		count = 1
    		if(self.created_rooms):
    			for key, value in self.room_allocation.items():
    				if value == room_allocated:
    					count += 1
    			if(self.created_rooms[room_allocated] == "Office" and count <= office_max_occupants):
    				self.room_allocation.update({person_name:room_allocated})
    				return 1
    			elif(self.created_rooms[room_allocated] == "Livingspace" and count <= livingspace_max_occupants):
    				self.room_allocation.update({person_name:room_allocated})
    				return 1
    			else:
    				return 0

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
        	if(len(self.room_allocation) == 0):
        		print("No rooms allocated")
        	else:
        		for key, value in self.room_allocation.items():
        			if value == arguments['<room_name>']:
        				print(key)
        			

    #function to show room allocations
    def do_print_allocations(self, arg):
    	
    	"""
        Usage:
        	print_allocations [-o=<filename>]
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
    		else:
    			print("No room allocations")

    #function display unallocated persons
    def do_print_unallocated(self, arg):
    	
    	"""
        Usage:
        	print_unallocated [-o=<filename>]
        """
    	
    	try:
    		arguments = docopt(self.do_print_unallocated.__doc__, arg)

    	except DocoptExit as e:
        	print('Invalid Command!')
        	print(e)

    	except (KeyboardInterrupt, SystemExit):
    		print("System shut down. Thank you.")

    	else:
    		if(self.created_persons and self.room_allocation):
    			found = 1
    			for key, values in self.created_persons.items():
    				if key not in self.room_allocation:
    					print(key)

    		else:
    			print("No room allocations")

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
