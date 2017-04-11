import cmd
import random
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
        		office_instance = Office()
        		office_result = office_instance.create_room(arguments['<room_name>'], arguments['<room_type>'])
        		self.created_rooms.update(office_result)
        		for office in office_result:
        			print("An Office called {} has been successfully created!".format(office))

        	elif (arguments['<room_type>'] == "Livingspace" or arguments['<room_type>'] == "livingspace"):
        		livingspace_instance = LivingSpace()
        		livingspace_result = livingspace_instance.create_room(arguments['<room_name>'], arguments['<room_type>'])
        		self.created_rooms.update(livingspace_result)
        		for livingspace in livingspace_result:
        			print("A Living Space called {} has been successfully created!".format(livingspace))

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
        		fellow_instance = Fellow()
        		fellow_result = fellow_instance.add_person(" ".join(arguments['<person_name>']),'Fellow', arguments['<wants_accommodation>'])
        		self.created_persons.update({fellow_result[0] : [fellow_result[1], fellow_result[2]]})
        		print(fellow_result[1],fellow_result[0],"has been successfully added,")
        		if(self.allocate_room(fellow_result[0]) == 1):
        			allocation =  self.room_allocation[fellow_result[0]]
        			print(fellow_result[1], fellow_result[0],"has been allocated", allocation, self.created_rooms[allocation])

        	elif arguments['Staff']:
        		staff_instance = Staff()
        		staff_result = staff_instance.add_person(" ".join(arguments['<person_name>']),'Staff', arguments['<wants_accommodation>'])
        		self.created_persons.update({staff_result[0] : [staff_result[1], staff_result[2]]})
        		print(staff_result[1],staff_result[0],"has been successfully added.")
        		if(self.allocate_room(staff_result[0])  == 1):
        			allocation =  self.room_allocation[staff_result[0]]
        			print(staff_result[1], staff_result[0],"has been allocated", allocation, self.created_rooms[allocation])
    
    #function to allocate a room to a person
    def allocate_room(self, person_name):
    	office_max_occupants = Office().max_occupants
    	livingspace_max_occupants = Office().max_occupants

    	if(len(self.created_rooms) > 0):
    		rooms_list = []
    		for key, value in self.created_rooms.items():
    			rooms_list.append(key)

    		random_key = random.randint(0 , len(rooms_list) - 1)
    		room_allocated = rooms_list[random_key]
    		self.room_allocation.update({person_name:room_allocated})

    		return 1

    #function to exit when 'exit' is typed
    def do_exit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        return True

#execute main code block
if __name__ == '__main__':
	
	try:
		Dojo().cmdloop()
	
	except (KeyboardInterrupt, SystemExit):
		print("System shut down. Thank you.")
