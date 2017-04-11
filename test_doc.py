from docopt import docopt, DocoptExit

def do_add_person():

        """
        Usage: 
            test_doc.py add_person (<person_name>) (Fellow|Staff) [<wants_accommodation>]
        """

        try: 
            arguments = docopt(do_add_person.__doc__)

        except  DocoptExit as e:
            print('Invalid Command!')
            print(e)

        except SystemExit:
            pass

        else:
            print(arguments)

if __name__ == '__main__':
    do_add_person()