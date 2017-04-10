import unittest
from app import Office, LivingSpace

class TestApp(unittest.TestCase):

	def test_create_office_successfully(self):
		my_class_instance = Office()
		initial_room_count = len(my_class_instance.all_rooms)
		blue_office = my_class_instance.create_room("Blue", "office")
		self.assertTrue(blue_office)
		new_room_count = len(my_class_instance.all_rooms)
		self.assertEqual(new_room_count - initial_room_count, 1)

	def test_create_livingspace_successfully(self):
		my_class_instance = LivingSpace()
		initial_room_count = len(my_class_instance.all_rooms)
		blue_office = my_class_instance.create_room("Blue", "office")
		self.assertTrue(blue_office)
		new_room_count = len(my_class_instance.all_rooms)
		self.assertEqual(new_room_count - initial_room_count, 1)

if __name__ == '__main__':
 	unittest.main()