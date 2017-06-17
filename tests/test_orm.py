import unittest
from model.orm_model import Rooms, Persons, Allocations, Unallocated

#class to test the Office class
class TestRoomClass(unittest.TestCase):

	def setUp(self):
		self.rooms = Rooms("Yellow", "Office")
		self.persons = Persons(213, "dennis kariuki", "Fellow", "Y")
		self.allocations = Allocations(213, "Yellow", "Office")
		self.unallocated = Unallocated(213, "Livingspace")

	#test instance of rooms
	def test_create_room_instance(self):
		self.assertTrue(self.rooms.room_name, "Yellow")

	#test instance of persons
	def test_create_persons_instance(self):
		self.assertTrue(self.persons.person_name, "dennis kariuki")

	#test instance of allocations
	def test_allocations_instance(self):
		self.assertTrue(self.allocations.pid, 213)

	#test instance of Unallocated
	def test_unallocated_instance(self):
		self.assertTrue(self.unallocated.pid, 213)

if __name__ == '__main__':
 	unittest.main()