import unittest
from user import User #import user class
from credentials import Credentials # import credentials class 

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviors
    '''

#set up and class creation
    def setUp(self):
        '''
        Set up method to run before each rest case
        '''

        self.new_user = User("Jane Doe", "janedoe@email.com", "janed03", "password") # create user object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
    
#other tests
    def test_init_(self):
        '''
        test to see if the object is initialized properly
        '''

        self.assertEqual(self.new_user.full_name, "Jane Doe")
        self.assertEqual(self.new_user.user_email, "janedoe@email.com")
        self.assertEqual(self.new_user.user_name, "janed03")
        self.assertEqual(self.new_user.password, "password")

    def test_create_account(self):
        '''
        test create user test case to see if a new user is saved into the user list
        '''

        self.new_user.create_account() 
        self.assertEqual(len(User.user_list),1)

    def test_account_login(self):
        '''
        test user login test case to see if user requires credentials'''

        

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behavior
    '''

#set up and class creation
    def setUp(self):
        '''
        Set up method to run before each rest case
        '''

        self.new_credentials = Credentials("Instagram", "janed03", "password") # create credentials object

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

#other test cases
    def test_init_(self):
        '''
        test to see if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name, "Instagram")
        self.assertEqual(self.new_credentials.account_user_name, "janed03")
        self.assertEqual(self.new_credentials.account_password, "password")

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new contact
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Instagram", "janed03", "password") # new account credentials
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

if __name__ == '__main__':
    unittest.main()
    