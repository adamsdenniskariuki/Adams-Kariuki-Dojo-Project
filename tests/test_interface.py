import unittest
import os
from interface.interface import Interface

#class to test the Dojo class
class TestDojoClass(unittest.TestCase):

	def setUp(self):
		self.interface = Interface()
		self.blue_office = self.interface.create_office(["blue"], "Office")
		self.white_livingspace = self.interface.create_livingspace(["white"], "LivingSpace")
		self.fellow = self.interface.add_fellow("John Kamau", "Y")
		self.staff = self.interface.add_staff("Adams Kitui")

	#test create office
	def test_create_office(self):
		self.assertTrue(self.blue_office)
		
		create_office_output = self.interface.create_office(["r3d"], "Office")
		self.assertEqual(create_office_output, "Use a-z only for the room name and room type")
		
		create_office_output = self.interface.create_office(["blue"], "Office")
		self.assertEqual(create_office_output, "Room blue already exists!")

	#test create living space
	def test_create_livingspace(self):
		self.assertTrue(self.white_livingspace)
		
		create_living_output = self.interface.create_livingspace(["bl4ck"], "LivingSpace")
		self.assertEqual(create_living_output, "Use a-z only for the room name and room type")
		
		create_living_output = self.interface.create_livingspace(["white"], "LivingSpace")
		self.assertEqual(create_living_output, "Room white already exists!")

	#test add fellow
	def test_add_fellow(self):
		self.assertTrue(self.fellow)
		
		add_fellow_output = self.interface.add_fellow("David Fulani", "N")
		self.assertIn("No living spaces allocated", add_fellow_output)

		add_fellow_error = self.interface.add_fellow("D4rius M1k3", "7")
		self.assertEqual(add_fellow_error, "Use a-z only for the person name, type and wants accomodation")

	#test add staff
	def test_add_staff(self):
		self.assertTrue(self.staff)

		add_staff_error = self.interface.add_staff("Drew King", "Y")
		self.assertIn("Staff members are not allocated living quarters", add_staff_error)
		
		add_staff_error = self.interface.add_staff("Y0le ms33")
		self.assertEqual(add_staff_error, "Use a-z only for the person name, type and wants accomodation")

	#test create file with errors
	def test_create_file_with_errors(self):
		create_file_error = self.interface.create_file("s4v3d", {})
		self.assertEqual(create_file_error, "Use a-z only for the file name")
		
		create_file_error = self.interface.create_file("load", {})
		self.assertEqual(create_file_error, "The file already exists. Choose another file name.")

	#test wrong database name
	def test_wrong_database_name(self):
		save_database_output = self.interface.save_state_orm("p3es1st")
		self.assertEqual(save_database_output, 'Use a-z for the database name')
		
		load_database_output = self.interface.load_state_orm("l04d3d")
		self.assertEqual(load_database_output, 'database l04d3d does not exist.')

	#test data is loaded from database
	def test_data_is_saved_and_loaded_from_database(self):
		save_database_output = self.interface.save_state_orm("testdb")
		self.assertEqual(save_database_output, 'All data saved...')
		
		load_database_output = self.interface.load_state_orm("testdb")
		self.assertEqual(load_database_output, 'Data loaded...')
		
		self.assertEqual(self.interface.all_rooms['blue'], 'Office')
		self.assertEqual(self.interface.all_rooms['white'], 'LivingSpace')

	#test reallocate person to another room
	def test_reallocate_person(self):
		reallocate_person_output = self.interface.reallocate_person(['Sam', 'Kim'], "blue")
		self.assertEqual(reallocate_person_output, "Person Sam Kim does not have any allocations or does not exist")
		
		reallocate_person_output = self.interface.reallocate_person(['Adams', 'Kitui'], "purple")
		self.assertEqual(reallocate_person_output, "Room purple has not been allocated or does not exist")
		
		self.assertTrue(self.interface.create_office(["red"], "Office"))
		reallocate_person_output = self.interface.reallocate_person(['John', 'Kamau'], "red")
		self.assertEqual(reallocate_person_output, 'John Kamau has been re-allocated to red')

	#test print unallocated method
	def test_print_unallocated(self):
		print_unallocated_output = self.interface.print_unallocated()
		self.assertIn("Office", print_unallocated_output)
		
		self.interface.print_unallocated("unallocatedtest")
		self.assertEqual(os.path.exists("./files/unallocatedtest.txt"), True)

	#test print allocations method
	def test_print_allocations(self):
		print_allocations_output = self.interface.print_allocations()
		self.assertIn('John Kamau', print_allocations_output)

		self.interface.print_unallocated("allocationstest")
		self.assertEqual(os.path.exists("./files/allocationstest.txt"), True)

	#test print a non existent room 
	def test_print_room_with_errors(self):
		print_room_output = self.interface.print_room("myroom")
		self.assertEqual(print_room_output, "Room myroom does not exist.")

	#test print a room 
	def test_print_room(self):
		print_room = self.interface.print_room("blue")
		self.assertIn("John Kamau", print_room)

	#test data can be loaded from text file
	def test_load_people_from_text_file(self):
		load_text_output = self.interface.load_people()
		self.assertEqual(load_text_output, 'Data has been loaded from text file')
		

if __name__ == '__main__':
 	unittest.main()