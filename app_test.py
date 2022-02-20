import unittest
#import pyperclip #to copy credentials to clipboard
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

    def test_create_user_account(self):
        '''
        test create user test case to see if a new user is saved into the user list
        '''

        self.new_user.create_user_account() 
        self.assertEqual(len(User.user_list),1)

    def test_account_login(self):
        '''
        test user login test case to see if user requires credentials to access passkey account; user account exists'''

        self.new_user.create_user_account()
        test_user = User("Jane Doe", "janedoe@email.com", "janed03", "password")
        test_user.create_user_account()

        #confirm whether user account exists
        account_exists = User.user_exists("janed03")
        self.assertTrue(account_exists)

        #verify username and password for login
        confirm_user = User.verify_account("janed03", "password")

        self.assertEqual(confirm_user.user_name, test_user.user_name)
        self.assertEqual(confirm_user.password, test_user.password)

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
            Credentials.accounts_list = []

#other test cases
    def test_init_(self):
        '''
        test to see if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_name, "Instagram")
        self.assertEqual(self.new_credentials.account_user_name, "janed03")
        self.assertEqual(self.new_credentials.account_password, "password")

    def test_save_accounts(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_accounts()
        self.assertEqual(len(Credentials.accounts_list),1)

    def test_save_multiple_accounts(self):
        '''
        test to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credentials.save_accounts()
        test_credentials = Credentials("Instagram", "janed03", "password") # new account credentials
        test_credentials.save_accounts()
        self.assertEqual(len(Credentials.accounts_list),2)

    def test_delete_accounts(self):
        '''
        to test if we can remove an account from our credentials list
        '''
        self.new_credentials.save_accounts()
        test_credentials = Credentials("Instagram", "janed03", "password") # new account credentials
        test_credentials.save_accounts()
        self.new_credentials.delete_accounts()
        self.assertEqual(len(Credentials.accounts_list),1)

    def test_create_new_account(self):
        '''
        to test if user can create new credentials
        '''
        self.new_credentials.save_accounts()
        test_credentials = Credentials("Instagram", "janed03", "password") # new account credentials
        test_credentials.generate_password()
        test_credentials.save_accounts()
        self.assertEqual(len(Credentials.accounts_list),2)

    def test_view_all_accounts(self):
        '''
        method to display a list of all saved accounts and credentials
        '''

        self.assertEqual(Credentials.view_accounts(), Credentials.accounts_list)

    def test_copy_credentials(self):
        '''
        test to confirm user copies account user name and password
        '''

if __name__ == '__main__':
    unittest.main()
    