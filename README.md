![Build Status](https://travis-ci.org/adamsdenniskariuki/Adams-Kariuki-Dojo-Project.svg?branch=v0)

# Dojo Manager

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

	create_room room_type room_names #create rooms of type Office or Living space.

	add_person person_name FELLOW|STAFF  wants_accommodation(Y|N) #create staff or fellows.

	print_room room_name #Prints  the names of all the people in ​room_name​ on the  screen.

	print_allocations filename​  #Prints a list of room allocations onto the screen or file specified.

	print_unallocated filename #Prints a list of unallocated people to the screen or file specified.

	reallocate_person person_name new_room_name​ #Reallocate the person entered​ to ​new_room_name​.

	load_people​ #Adds people to rooms from a txt file.

	save_state​ database_name #Persists all the data stored in the app to an SQLite database.

	load_state database_name #Loads data from a database into the application.


# Author
Adams Kariuki @ 2017




