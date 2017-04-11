import unittest
from .  import *
from app import Dojo

#class to test the Dojo class
class TestDojoClass(unittest.TestCase):

	def setUp(self):
		self.dojo_instance = Dojo()

	#test create office with errors
	def test_dojo_create_office_with_errors(self):
		dojo_input_error = self.dojo_instance.dojo_create_office(" &^*&^*^ ", "&(&(&(&(&")
		self.assertEqual(dojo_input_error, "Use alphabet (a-z) characters for the room name and room type")

	#test create office with errors
	def test_dojo_create_livingspace_with_errors(self):
		dojo_input_error = self.dojo_instance.dojo_create_livingspace(" &^*&^*^ ", "&(&(&(&(&")
		self.assertEqual(dojo_input_error, "Use alphabet (a-z) characters for the room name and room type")

	#test add fellow with errors
	def test_dojo_add_fellow_with_errors(self):
		dojo_input_error = self.dojo_instance.dojo_add_fellow(" &^*&^*^ ", "&(&(&(&(&", "UY^(Y**")
		self.assertEqual(dojo_input_error, "Use alphabet (a-z) characters for the person name, type and wants accomodation")

	#test add staff with errors
	def test_dojo_add_staff_with_errors(self):
		dojo_input_error = self.dojo_instance.dojo_add_staff(" &^*&^*^ ", "&(&(&(&(&", "UY^(Y**")
		self.assertEqual(dojo_input_error, "Use alphabet (a-z) characters for the person name, type and wants accomodation")


if __name__ == '__main__':
 	unittest.main()