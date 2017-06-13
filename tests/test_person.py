import unittest
from model.person import Staff, Fellow

#class to test the Staff class
class TestStaffClass(unittest.TestCase):

	#test instance of staff
	def test_add_staff_instance(self):
		self.assertTrue(Staff("Madge Wanjiru", "Staff", "N"), Staff)

	#test instance of fellow
	def test_add_fellow_instance(self):
		self.assertTrue(Fellow("Sam John", "Fellow", "Y"), Fellow)


if __name__ == '__main__':
 	unittest.main()