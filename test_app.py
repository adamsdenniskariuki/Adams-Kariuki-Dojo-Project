import unittest
from model.room import Office, LivingSpace
from model.person import Fellow, Staff


#class to test the Office class
class TestOfficeClass(unittest.TestCase):

	#declare variables
	def setUp(self):
		self.office_instance = Office()

	#test office is created
	def test_create_office_successfully(self):
		initial_room_count = len(self.office_instance.offices)
		blue_office = self.office_instance.create_room("Blue", "office")
		self.assertTrue(blue_office)
		new_room_count = len(self.office_instance.offices)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test create office with error
	def test_create_office_with_errors(self):
		office_input_error = self.office_instance.create_room("       dadasdas ", "&^%^%&^%&")
		self.assertEqual(office_input_error, "Use alphabet (a-z) characters for the room name and room type")

	#test instance of office
	def test_create_office_instance(self):
		self.assertTrue(self.office_instance, Office)

	#test office max occupants
	def test_office_max_occupants(self):
		self.assertTrue(self.office_instance.max_occupants, 6)


#class to test the LivingSpace class
class TestLivingSpaceClass(unittest.TestCase):

	#declare variables
	def setUp(self):
		self.livingspace_instance = LivingSpace() 

	#test living space is created
	def test_create_livingspace_successfully(self):
		initial_room_count = len(self.livingspace_instance.living_spaces)
		red_livingspace = self.livingspace_instance.create_room("Red", "livingspace")
		self.assertTrue(red_livingspace)
		new_room_count = len(self.livingspace_instance.living_spaces)
		self.assertEqual(new_room_count - initial_room_count, 1)

	#test create living space with errors
	def test_create_office_with_errors(self):
		livingspace_input_error = self.livingspace_instance.create_room("       dadasdas ", "&^%^%&^%&")
		self.assertEqual(livingspace_input_error, "Use alphabet (a-z) characters for the room name and room type")

	#test instance of living space
	def test_create_livingspace_instance(self):
		self.assertTrue(self.livingspace_instance, LivingSpace)

	#test living space max occupants
	def test_livingspace_max_occupants(self):
		self.assertTrue(self.livingspace_instance.max_occupants, 4)


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