import unittest
from model.room import Office, LivingSpace

#class to test the Office class
class TestRoomClass(unittest.TestCase):

	def setUp(self):
		self.office = Office(["Pink"], "Office")
		self.livingspace = LivingSpace(["Black"], "LivingSpace")

	#test office max occupants
	def test_office_max_occupants(self):
		self.assertTrue(self.office.max_occupants, 6)

	#test living space max occupants
	def test_livingspace_max_occupants(self):
		self.assertTrue(self.livingspace.max_occupants, 4)

if __name__ == '__main__':
 	unittest.main()