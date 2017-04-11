import unittest
from .  import *
from model.room import LivingSpace

#class to test the LivingSpace class
class TestLivingSpaceClass(unittest.TestCase):

	#declare variables
	def setUp(self):
		self.livingspace_instance = LivingSpace() 

	#test living space is created
	def test_create_livingspace_successfully(self):
		initial_room_count = len(self.livingspace_instance.living_spaces)
		red_livingspace = self.livingspace_instance.create_room("Red", "livingspace")
		self.assertTrue(red_livingspace)
		new_room_count = len(self.livingspace_instance.living_spaces)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test create living space with errors
	def test_create_office_with_errors(self):
		livingspace_input_error = self.livingspace_instance.create_room("       dadasdas ", "&^%^%&^%&")
		self.assertEqual(livingspace_input_error, "Use alphabet (a-z) characters for the room name and room type")

	#test instance of living space
	def test_create_livingspace_instance(self):
		self.assertTrue(self.livingspace_instance, LivingSpace)

	#test living space max occupants
	def test_livingspace_max_occupants(self):
		self.assertTrue(self.livingspace_instance.max_occupants, 4)


if __name__ == '__main__':
 	unittest.main()