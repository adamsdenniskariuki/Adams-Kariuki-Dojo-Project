import unittest
from controller.controllers import Controllers

#class to test the Dojo class
class TestDojoClass(unittest.TestCase):

	def setUp(self):
		self.controllers_instance = Controllers()

	#test create office with errors
	def test_dojo_create_office_with_errors(self):
		input_error = self.controllers_instance.create_office([" &^*&4^*^ "], "&(&(&(&(&")
		self.assertEqual(input_error, "Use a-z only for the room name and room type")

	#test create office with errors
	def test_dojo_create_livingspace_with_errors(self):
		input_error = self.controllers_instance.create_livingspace([" &^*&^54*^ "], "&(&(&(&(&")
		self.assertEqual(input_error, "Use a-z only for the room name and room type")

	#test add fellow with errors
	def test_dojo_add_fellow_with_errors(self):
		input_error = self.controllers_instance.add_fellow(" &^*&^21*^ ", "&(&(&(&(&", "Y")
		self.assertEqual(input_error, "Use a-z only for the person name, type and wants accomodation")

	#test add staff with errors
	def test_dojo_add_staff_with_errors(self):
		input_error = self.controllers_instance.add_staff(" &^*&^54*^ ", "&(&(&(&(&", "N")
		self.assertEqual(input_error, "Use a-z only for the person name, type and wants accomodation")

	#test create file with errors
	def test_dojo_create_file_with_errors(self):
		input_error = self.controllers_instance.create_file("&(&(&(&(&")
		self.assertEqual(input_error, "Use a-z only for the file name")


if __name__ == '__main__':
 	unittest.main()