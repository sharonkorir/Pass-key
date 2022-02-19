class User:

    '''
    This class will be used to create objects of users
    '''

    user_list = [] #create an empty list of users

    def __init__(self, first_name, second_name, user_name, password):
  
        '''
        this helps define user properties
        '''

        self.first_name = first_name
        self.second_name = second_name
        self.user_name = user_name # username or email used to log into the application
        self.password = password