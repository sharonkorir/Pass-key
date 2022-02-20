import random, string #to generate random password
#import pyperclip #attempt copy paste

class Credentials:

    '''
    This class will be used to create objects of credentials
    '''

    accounts_list = [] #create an empty list of users

    def __init__(self, account_name, account_user_name, account_password):
        '''
        this helps define user properties
        '''

        self.account_name = account_name
        self.account_user_name = account_user_name # username or email used to log into the application
        self.account_password = account_password
    
    def save_accounts(self): #require user credentials to use Pass-key app
        '''
        this method saves existing account credentials to user's Pass-key account 
        '''

        Credentials.accounts_list.append(self)

    def delete_accounts(self):
        '''
        this method deletes a saved account from the accounts_list
        '''

        Credentials.accounts_list.remove(self)

    def create_new_account(self): #create new credentials
        '''
        this method creates and saves new credentials
        '''

        Credentials.accounts_list.append(self)
    
    def generate_password(self):
        '''
        this method generates a random user password using string and random modules
        '''
        #get desired password length
        password_length = int(input("\n Enter the length of your password: "))

        #limit password length to 15 characters?

        #define data
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        numbers = string.digits

        password_characters = upper + lower + numbers

        #generate random characters
        random_password = random.sample(password_characters, password_length) #pass desired length as argument

        #create password
        account_password = "".join(random_password)

        #test if this works
        print("\n" + account_password)

        return account_password

    @classmethod
    def view_accounts(cls):
        '''
        method that returns the accounts list
        '''
        return cls.accounts_list

    