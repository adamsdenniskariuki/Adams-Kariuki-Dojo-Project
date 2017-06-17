import unittest
from interface.interface import Interface

#class to test the Dojo class
class TestDojoClass(unittest.TestCase):

	def setUp(self):
		self.interface_instance = Interface()

	#test create office with errors
	def test_create_office_with_errors(self):
		input_error = self.interface_instance.create_office([" &^*&4^*^ "], "&(&(&(&(&")
		self.assertEqual(input_error, "Use a-z only for the room name and room type")

	#test create office with errors
	def test_create_livingspace_with_errors(self):
		input_error = self.interface_instance.create_livingspace([" &^*&^54*^ "], "&(&(&(&(&")
		self.assertEqual(input_error, "Use a-z only for the room name and room type")

	#test add fellow with errors
	def test_add_fellow_with_errors(self):
		input_error = self.interface_instance.add_fellow(" &^*&^21*^ ", "&(&(&(&(&", "Y")
		self.assertEqual(input_error, "Use a-z only for the person name, type and wants accomodation")

	#test add staff with errors
	def test_add_staff_with_errors(self):
		input_error = self.interface_instance.add_staff(" &^*&^54*^ ", "&(&(&(&(&", "N")
		self.assertEqual(input_error, "Use a-z only for the person name, type and wants accomodation")

	#test create file with errors
	def test_create_file_with_errors(self):
		input_error = self.interface_instance.create_file("&(&(&(&(&")
		self.assertEqual(input_error, "Use a-z only for the file name")

	#test print room with errors
	def test_print_room_with_errors(self):
		input_error = self.interface_instance.print_room("myroom")
		self.assertEqual(input_error, "Room myroom does not exist.")


if __name__ == '__main__':
 	unittest.main()