import unittest
from model.person import Fellow

#class to test the Fellow class
class TestFellowClass(unittest.TestCase):

	#declare variables
	def setUp(self):
		self.fellow_instance = Fellow()

	#test fellow is created
	def test_add_fellow_successfully(self):
		all_persons_count = len(self.fellow_instance.created_fellow)
		fellows = self.fellow_instance.add_person("Adams Kariuki", "Fellow", "Y")
		self.assertTrue(fellows)
		new_person_count = len(self.fellow_instance.created_fellow)
		print(new_person_count)
		self.assertTrue(new_person_count - all_persons_count, 3)

	#test add fellow with errors
	def test_add_fellow_with_errors(self):
		fellow_input_error = self.fellow_instance.add_person("  4654 %#^6 ", " &^*&^*^ ", "&(&(&(&(&")
		self.assertEqual(fellow_input_error, "Use alphabet (a-z) characters for the person name, person type and wants accomodation")

	#test instance of fellow
	def test_add_fellow_instance(self):
		self.assertTrue(self.fellow_instance, Fellow)


if __name__ == '__main__':
 	unittest.main()