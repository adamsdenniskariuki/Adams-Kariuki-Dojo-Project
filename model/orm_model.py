from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Rooms(Base):
	__tablename__ = 'rooms'
	room_id = Column(Integer)
	room_name = Column(String(250), primary_key=True, nullable=False)
	room_type = Column(String(250), nullable=False)

	def __init__(self, room_name, room_type):
		self.room_name = room_name
		self.room_type = room_type

class Persons(Base):
	__tablename__ = 'person'
	pid = Column(Integer, primary_key=True)
	person_name = Column(String(250), nullable=False)
	person_type = Column(String(250), nullable=False)
	wants_accomodation = Column(String(250), nullable=False)

	def __init__(self, pid, person_name, person_type, wants_accomodation):
		self.pid = pid
		self.person_name = person_name
		self.person_type = person_type
		self.wants_accomodation = wants_accomodation

class Allocations(Base):
	__tablename__ = 'allocation'
	pid = Column(Integer, primary_key=True)
	room_name = Column(String(250), nullable=False)
	room_type = Column(String(250), nullable=False)

	def __init__(self, pid, room_name, room_type):
		self.pid = pid
		self.room_name = room_name
		self.room_type = room_type

class Unallocated(Base):
	__tablename__ = 'unallocated'
	id = Column(Integer, primary_key=True)
	pid = Column(Integer, nullable=False)
	room_type = Column(String(250), nullable=False)

	def __init__(self, pid, room_type):
		self.pid = pid
		self.room_type = room_type