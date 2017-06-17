import cmd
from docopt import docopt, DocoptExit
from interface.interface import Interface

#function to get the inputs from docopt
def get_docopt_inputs(func):

	def fn(self, arg):

		try:
			arguments = docopt(fn.__doc__, arg)

		except DocoptExit as e:
			print('Invalid Command!')
			print(e)

		except (KeyboardInterrupt, SystemExit):
			print("System shut down. Thank you.")

		return func(self, arguments)

	fn.__name__ = func.__name__
	fn.__doc__ = func.__doc__
	fn.__dict__.update(func.__dict__)
	return fn


# class to make the app interactive
class Dojo (cmd.Cmd):

	intro = ''.join(['\nWelcome to the Amity program!\n\n',
					'Type help for assistance and exit to leave.'])
	prompt = '\nAmity >>>'
	interface = Interface()

	# function to get inputs to create a room
	@get_docopt_inputs
	def do_create_room(self, arg):
		"""
		Usage:
			create_room <room_type> <room_name>...
		"""

		if(arg['<room_type>'] == "Office" or
				arg['<room_type>'] == "office"):
			self.interface.create_office(arg['<room_name>'], arg[
				'<room_type>'])
		elif(arg['<room_type>'] == "Livingspace" or arg[
				'<room_type>'] == "livingspace"):
			self.interface.create_livingspace(arg['<room_name>'],
										 arg['<room_type>'])
		else:
			print("Indicate the office type: Office or Livingspace")

	# function to get inputs to add a person
	@get_docopt_inputs
	def do_add_person(self, arg):
		"""
		Usage:
			add_person (<person_name> <person_name>) (Fellow|Staff)
				[<wants_accommodation>]
		"""

		if(arg['<wants_accommodation>'] is None):
			arg['<wants_accommodation>'] = "N"

		if(arg['Fellow']):
			self.interface.add_fellow(
				" ".join(
					arg['<person_name>']),
				arg['<wants_accommodation>'])

		if(arg['Staff']):
			self.interface.add_staff(
				" ".join(
					arg['<person_name>']),
				arg['<wants_accommodation>'])

	# function to show specific room allocation
	@get_docopt_inputs
	def do_print_room(self, arg):
		"""
		Usage:
			print_room <room_name>
		"""

		self.interface.print_room(arg['<room_name>'])

	# function to show room allocations
	@get_docopt_inputs
	def do_print_allocations(self, arg):
		"""
		Usage:
			print_allocations [-o FILE]
		"""

		if(arg['FILE'] and arg['-o']):
			self.interface.print_allocations(arg['FILE'])
		else:
			self.interface.print_allocations()

	# function display unallocated persons
	@get_docopt_inputs
	def do_print_unallocated(self, arg):
		"""
		Usage:
			print_unallocated [-o FILE]
		"""

		if(arg['FILE'] and arg['-o']):
			self.interface.print_unallocated(arg['FILE'])
		else:
			self.interface.print_unallocated()

	# function to take variables to reallocate persons
	@get_docopt_inputs
	def do_reallocate_person(self, arg):
		"""
		Usage:
			reallocate_person <person_identifier> [<person_identifier>]
				<new_room_name>
		"""

		self.interface.reallocate_person(arg[
				'<person_identifier>'], arg['<new_room_name>'])

	# function to take variables to reallocate persons
	@get_docopt_inputs
	def do_load_people(self, arg):
		"""
		Usage:
			load_people
		"""

		self.interface.load_people()

	# function to save state to db
	@get_docopt_inputs
	def do_save_state(self, arg):
		"""
		Usage:
			save_state [-db DBNAME]
		"""

		if not arg['DBNAME']:
			arg['DBNAME'] = "dojo"

		self.interface.save_state_orm(arg['DBNAME'])

	# function to load state from db
	@get_docopt_inputs
	def do_load_state(self, arg):
		"""
		Usage:
			load_state [<dojodb>]
		"""

		if not arg['<dojodb>']:
			arg['<dojodb>'] = "dojo"

		self.interface.load_state_orm(arg['<dojodb>'])

	# function to exit when 'exit' is typed
	def do_exit(self, arg):
		"""Quits out of Interactive Mode."""

		print('Good Bye!')
		return True

	def do_cls(self, arg):
		os.system('clear')


# execute main code block
if __name__ == '__main__':

	try:
		Dojo().cmdloop()

	except (KeyboardInterrupt, SystemExit):
		print("System shut down. Thank you.")
