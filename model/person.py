#class to create a person
class Person(object):

	def __init__(self, person_name, person_type, wants_accommodation = 'N'):
		self.person_name = person_name
		self.person_type = person_type
		self.wants_accommodation = wants_accommodation
		self.person_created = []

	def add_person(self, person_name, person_type, wants_accommodation):
		if(self.wants_accommodation is not 'N' and self.person_type == "Staff"):
			return "Staff are not allocated living quarters."
		elif(self.person_type == "Staff"):
			self.person_created = [self.person_name, self.person_type, 'N']
		elif(self.person_type == "Fellow" and self.wants_accommodation is "Y"  or self.wants_accommodation is "N"):
			self.person_created = [self.person_name, self.person_type, wants_accommodation]
		elif(self.wants_accommodation is not "N" or self.wants_accommodation is not "Y"):
			return "Invalid value for accomodation. Use Y or N"
		
		return self.person_created


#class to create staff
class Staff(Person):

	def __init__(self):
		self.created_staff = []

	def add_person(self, person_name, person_type, wants_accommodation = 'N'):
		super(Staff, self).__init__(person_name, person_type, wants_accommodation)
		if(not self.person_name.replace(' ','').isalpha() or not self.person_type.isalpha() or not self.wants_accommodation.isalpha()):
			return "Use alphabet (a-z) characters for the person name, person type and wants accomodation"
		self.created_staff = super(Staff, self).add_person(self.person_name, self.person_type, self.wants_accommodation)
		return self.created_staff
		

#class to create a fellow
class Fellow(Person):
	
	def __init__(self):
		self.created_fellow = []

	def add_person(self, person_name, person_type, wants_accommodation = 'N'):
		super(Fellow, self).__init__(person_name, person_type, wants_accommodation)
		if(not self.person_name.replace(' ','').isalpha() or not self.person_type.isalpha() or not self.wants_accommodation.isalpha()):
			return "Use alphabet (a-z) characters for the person name, person type and wants accomodation"
		self.created_fellow = super(Fellow, self).add_person(self.person_name, self.person_type, self.wants_accommodation)
		return self.created_fellow