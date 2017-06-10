![Build Status](https://travis-ci.org/adamsdenniskariuki/Adams-Kariuki-Dojo-Project.svg?branch=v0)

# Amity

An interactive command line app to allocate rooms and living spaces to staff and fellows.

# Installation / Getting Started

- clone the repo and run app.py in the command line (python app.py).

## dependencies
- python version 3.4 and above.
- docopt version 0.6.2 and above.
- virtualenv version 15.1.0 and above.

## documentation
- virtualenv https://virtualenv.pypa.io/en/stable/
- docopt http://docopt.org/
- python https://docs.python.org/3/

# Usage / Commands

	create_room room_type room_names : _create rooms of type Office or Living space._

	add_person person_name FELLOW|STAFF  wants_accommodation(Y|N) : _create staff or fellows._

	print_room room_name : _Prints  the names of all the people in ​room_name​ on the screen._

	print_allocations filename​ : _Prints a list of room allocations onto the screen or file specified._

	print_unallocated filename : _Prints a list of unallocated people to the screen or file specified._

	reallocate_person person_name new_room_name​ : _Reallocate the person entered​ to ​a new room​._

	load_people​ : _Adds people to rooms from a txt file._

	save_state​ database_name : _Persists all the data stored in the app to an SQLite database._

	load_state database_name : _Loads data from a database into the application._

# Author
Adams Kariuki Dennis @ 2017




