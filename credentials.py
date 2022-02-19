class Credentials:

    '''
    This class will be used to create objects of credentials
    '''

    credentials_list = [] #create an empty list of users

    def __init__(self, account_name, account_email, account_user_name, account_password):
        '''
        this helps define user properties
        '''

        self.account_name = account_name
        self.account_email = account_email
        self.account_user_name = account_user_name # username or email used to log into the application
        self.account_password = account_password
    