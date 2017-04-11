import unittest
from model.room import Office, LivingSpace
from model.person import Fellow, Staff
from app import Dojo

class TestApp(unittest.TestCase):

	def setUp(self):
		self.office_instance = Office()
		self.livingspace_instance = LivingSpace()
		self.fellow_instance = Fellow()
		self.staff_instance = Staff()
		self.dojo_instance = Dojo()

	#test office is created
	def test_create_office_successfully(self):
		initial_room_count = len(self.office_instance.offices)
		blue_office = self.office_instance.create_room("Blue", "office")
		self.assertTrue(blue_office)
		new_room_count = len(self.office_instance.offices)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test instance of office
	def test_create_office_instance(self):
		self.assertTrue(self.office_instance, Office)

	#test office max occupants
	def test_office_max_occupants(self):
		self.assertTrue(self.office_instance.max_occupants, 6) 

	#test living space is created
	def test_create_livingspace_successfully(self):
		initial_room_count = len(self.livingspace_instance.living_spaces)
		red_livingspace = self.livingspace_instance.create_room("Red", "livingspace")
		self.assertTrue(red_livingspace)
		new_room_count = len(self.livingspace_instance.living_spaces)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test instance of living space
	def test_create_livingspace_instance(self):
		self.assertTrue(self.livingspace_instance, LivingSpace)

	#test living space max occupants
	def test_livingspace_max_occupants(self):
		self.assertTrue(self.livingspace_instance.max_occupants, 4)

	#test fellow is created
	def test_add_fellow_successfully(self):
		all_persons_count = len(self.fellow_instance.created_fellow)
		fellows = self.fellow_instance.add_person("Adams Kariuki", "Fellow", "Y")
		self.assertTrue(fellows)
		new_person_count = len(self.fellow_instance.created_fellow)
		self.assertEqual(new_person_count - all_persons_count, 3)

	#test instance of fellow
	def test_add_fellow_instance(self):
		self.assertTrue(self.fellow_instance, Fellow)

	#test staff is created
	def test_add_staff_successfully(self):
		all_persons_count = len(self.staff_instance.created_staff)
		staff = self.staff_instance.add_person("Adams Kariuki", "Staff")
		self.assertTrue(staff)
		print(self.staff_instance.created_staff)
		new_person_count = len(self.staff_instance.created_staff)
		self.assertEqual(new_person_count - all_persons_count, 3)

	#test instance of staff
	def test_add_staff_instance(self):
		self.assertTrue(self.staff_instance, Staff)



if __name__ == '__main__':
 	unittest.main()