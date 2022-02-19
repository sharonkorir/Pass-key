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