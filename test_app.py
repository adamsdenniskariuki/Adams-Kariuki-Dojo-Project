import unittest
from app import Office, LivingSpace, Fellow, Staff

class TestApp(unittest.TestCase):

	#test office is created
	def test_create_office_successfully(self):
		office_instance = Office()
		initial_room_count = len(office_instance.all_rooms)
		blue_office = office_instance.create_room("Blue", "office")
		self.assertTrue(blue_office)
		new_room_count = len(office_instance.all_rooms)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test living space is created
	def test_create_livingspace_successfully(self):
		livingspace_instance = LivingSpace()
		initial_room_count = len(livingspace_instance.all_rooms)
		red_livingspace = livingspace_instance.create_room("Red", "livingspace")
		self.assertTrue(red_livingspace)
		new_room_count = len(livingspace_instance.all_rooms)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test fellow is created
	def test_add_fellow_successfully(self):
		fellow_instance = Fellow()
		all_persons_count = len(fellow_instance.all_persons)
		fellows = fellow_instance.add_person("Adams Kariuki", "Fellow", "Y")
		self.assertTrue(fellows)
		new_person_count = len(fellow_instance.all_persons)
		self.assertEqual(new_person_count - all_persons_count, 3)

	#test staff is created
	def test_add_staff_successfully(self):
		staff_instance = Staff()
		all_persons_count = len(staff_instance.all_persons)
		staff = staff_instance.add_person("Adams Kariuki", "Staff")
		self.assertTrue(staff)
		new_person_count = len(staff_instance.all_persons)
		self.assertEqual(new_person_count - all_persons_count, 2)

if __name__ == '__main__':
 	unittest.main()