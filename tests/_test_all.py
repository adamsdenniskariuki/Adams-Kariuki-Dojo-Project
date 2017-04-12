import unittest
from tests.test_dojo import TestDojoClass
from tests.test_staff import TestStaffClass
from tests.test_fellow import TestFellowClass
from tests.test_office import TestOfficeClass
from tests.test_livingspace import TestLivingSpaceClass

#run all the test classes
if __name__ == '__main__':

    dojotest = unittest.TestLoader().loadTestsFromTestCase(TestDojoClass)
    stafftest = unittest.TestLoader().loadTestsFromTestCase(TestStaffClass)
    fellowtest = unittest.TestLoader().loadTestsFromTestCase(TestFellowClass)
    officetest = unittest.TestLoader().loadTestsFromTestCase(TestOfficeClass)
    livingspacetest = unittest.TestLoader().loadTestsFromTestCase(TestLivingSpaceClass)

    alltests = unittest.TestSuite([dojotest, stafftest, fellowtest, officetest, livingspacetest])

    unittest.TextTestRunner().run(alltests)