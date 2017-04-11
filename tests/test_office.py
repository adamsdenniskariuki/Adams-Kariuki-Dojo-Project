import unittest
from .  import *
from model.room import Office

#class to test the Office class
class TestOfficeClass(unittest.TestCase):

	#declare variables
	def setUp(self):
		self.office_instance = Office()

	#test office is created
	def test_create_office_successfully(self):
		initial_room_count = len(self.office_instance.offices)
		blue_office = self.office_instance.create_room("Blue", "office")
		self.assertTrue(blue_office)
		new_room_count = len(self.office_instance.offices)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test create office with error
	def test_create_office_with_errors(self):
		office_input_error = self.office_instance.create_room("       dadasdas ", "&^%^%&^%&")
		self.assertEqual(office_input_error, "Use alphabet (a-z) characters for the room name and room type")

	#test instance of office
	def test_create_office_instance(self):
		self.assertTrue(self.office_instance, Office)

	#test office max occupants
	def test_office_max_occupants(self):
		self.assertTrue(self.office_instance.max_occupants, 6)

if __name__ == '__main__':
 	unittest.main()