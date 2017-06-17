import unittest
from model.room import Office, LivingSpace

#class to test the Office class
class TestRoomClass(unittest.TestCase):

	#test instance of office
	def test_create_office_instance(self):
		self.assertTrue(Office(["Yellow"], "Office"), Office)

	#test instance of living room
	def test_create_livingspace_instance(self):
		self.assertTrue(LivingSpace(["White"], "Livingspace"), LivingSpace)

	#test office max occupants
	def test_office_max_occupants(self):
		self.assertTrue(Office(["Green"], "Office").max_occupants, 6)

	#test living space max occupants
	def test_livingspace_max_occupants(self):
		self.assertTrue(LivingSpace(["Gray"], "Livingspace").max_occupants, 4)

if __name__ == '__main__':
 	unittest.main()