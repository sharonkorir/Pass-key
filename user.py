class User:

    '''
    This class will be used to create objects of users
    '''

    user_list = [] #create an empty list of users

    def __init__(self, fullname, username, password):
        '''
        this helps define user properties
        '''

        self.fullname = fullname
        self.username = username # username or email used to log into the application
        self.password = password
    
    def save_user_account(self): #add user to user list
        '''
        create_account method saves user credentials to access Pass-key account 
        '''

        User.user_list.append(self)

    @classmethod
    def verify_account(cls, username, password):
        '''
        Method that checks if user account exists then logs in

        Args:
            username and password to verify user
        Returns :
            account that matches name and password
        '''
        user_acc = ""
        for user in cls.user_list:
            if user.username == username and user.password == password:
                return user_acc

    @classmethod
    def show_user(cls):
        '''
        Method that shows existing users
        '''

        return cls.user_list