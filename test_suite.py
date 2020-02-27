import unittest
from python_2nd_project.test_me_app import test_me_app2
from python_2nd_project.hdfc_window_frame import GoogleOrgSearch1


loader=unittest.TestLoader()

suite=unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_me_app2))

#suite.addTest(unittest.TestLoader().loadTestsFromTestCase(GoogleOrgSearch1))
runner=unittest.TextTestRunner(verbosity=2)

result=runner.run(suite)