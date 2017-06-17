import unittest
from model.room import Office, LivingSpace

#class to test the Office class
class TestRoomClass(unittest.TestCase):

	def setUp(self):
		self.office = Office(["Yellow"], "Office")
		self.livingspace = LivingSpace(["White"], "LivingSpace")

	#test instance of office
	def test_create_office_instance(self):
		self.assertTrue(self.office.room_type, "Office")

	#test instance of living room
	def test_create_livingspace_instance(self):
		self.assertTrue(self.livingspace.room_type, "LivingSpace")

	#test office max occupants
	def test_office_max_occupants(self):
		self.assertTrue(self.office.max_occupants, 6)

	#test living space max occupants
	def test_livingspace_max_occupants(self):
		self.assertTrue(self.livingspace.max_occupants, 4)

if __name__ == '__main__':
 	unittest.main()