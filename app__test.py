import unittest
from user import User #import user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviors
    '''

    def setUp(self):
        '''
        Set up method to run before each rest case
        '''

        self.new_user = User("Jane Doe", "janedoe@email.com", "janed03", "password") # create user object

    def test_init_(self):
        '''
        test to see if tge object is initialized properly
        '''

        self.assertEqual(self.new_user.full_name, "Jane Doe")
        self.assertEqual(self.new_user.user_email, "janedoe@email.com")
        self.assertEqual(self.new_user.user_name, "janed03")
        self.assertEqual(self.new_user.password, "password")

    def test_create_account(self):
        '''
        test create user test case to see if a new user is saved into the user list'''

        self.new_user.create_account() 
        self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
    unittest.main()