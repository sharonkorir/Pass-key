class User:

    '''
    This class will be used to create objects of users
    '''

    user_list = [] #create an empty list of users

    def __init__(self, full_name, user_email, user_name, password):
        '''
        this helps define user properties
        '''

        self.full_name = full_name
        self.user_email = user_email
        self.user_name = user_name # username or email used to log into the application
        self.password = password
    
    def create_account(self): #require user credentials to use Pass-key app
        '''
        create_account method saves user credentials to access Pass-key account 
        '''

        User.user_list.append(self)