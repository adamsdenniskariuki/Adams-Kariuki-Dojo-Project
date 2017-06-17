import unittest
from model.person import Staff, Fellow

#class to test the Staff class
class TestStaffClass(unittest.TestCase):

	def setUp(self):
		self.staff = Staff("Madge Wanjiru")
		self.fellow = Fellow("Sam John", "Y")

	#test instance of staff
	def test_add_staff_instance(self):
		self.assertTrue(self.staff.person_type, "Staff")

	#test instance of fellow
	def test_add_fellow_instance(self):
		self.assertTrue(self.fellow, "Fellow")


if __name__ == '__main__':
 	unittest.main()