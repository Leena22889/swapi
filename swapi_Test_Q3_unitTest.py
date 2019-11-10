#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      L
#
# Created:     10/11/2019
# Copyright:   (c) L 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import swapi_test_Q2

class TestStartWarsCharacter(unittest.TestCase):

    def setUp(self):
        return r'https://swapi.co/api/people'

    def test_startWarsCharacter_returns_nonempty(self):
        api = swapi_test_Q2.ApiHelper()
        api.star_wars_characters(self.setUp())
        self.assertNotEqual(api.star_wars_details, None)


if __name__ == '__main__':
    unittest.main()
