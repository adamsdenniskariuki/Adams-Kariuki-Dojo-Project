import unittest
from .  import *
from model.person import Staff

#class to test the Staff class
class TestStaffClass(unittest.TestCase):

	#declare variables
	def setUp(self):
		self.staff_instance = Staff()

	#test staff is created
	def test_add_staff_successfully(self):
		all_persons_count = len(self.staff_instance.created_staff)
		staff = self.staff_instance.add_person("Adams Kariuki", "Staff")
		self.assertTrue(staff)
		print(self.staff_instance.created_staff)
		new_person_count = len(self.staff_instance.created_staff)
		self.assertEqual(new_person_count - all_persons_count, 3)

	#test add staff with errors
	def test_add_staff_with_errors(self):
		staff_input_error = self.staff_instance.add_person("  4654 %#^6 ", " &^*&^*^ ", "&(&(&(&(&")
		self.assertEqual(staff_input_error, "Use alphabet (a-z) characters for the person name, person type and wants accomodation")

	#test instance of staff
	def test_add_staff_instance(self):
		self.assertTrue(self.staff_instance, Staff)


if __name__ == '__main__':
 	unittest.main()