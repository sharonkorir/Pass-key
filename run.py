#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

#create user account
def create_user_acc(fullname, username, password):
    '''
    Function to create a Pass-key account
    '''
    new_user = User(fullname, username, password)
    return new_user

#save user account
def save_user_acc(user):
    '''
    Function to save user account
    '''

    user.save_user_account()

#display user list
def show_users():
  '''
  function to show existing users
  '''
  return User.show_user()

#verify and login to account
def verify_acc(username, password):
    '''
    Function to log in to account
    '''
    verify_user = User.verify_account(username, password)
    return verify_user


#credentials part
def save_acc(account_name, account_user_name, account_password):
    '''
    function to save existing account credentials
    '''
    new_credentials = Credentials(account_name, account_user_name, account_password)
    return new_credentials

def create_new_acc(account_name, account_user_name, account_password):
    '''
    function to create new account with existing password
    '''
    new_credentials = Credentials(account_name, account_user_name, account_password)
    return new_credentials

def create_new_acc_password(account_name, account_user_name, account_password):
    '''
    function to create new account and generate password
    '''
    new_credentials = Credentials(account_name, account_user_name, account_password)
    return new_credentials

def generate_pwd(credentials):
    '''
    Function to generate random password
    '''

    credentials.generate_password()

def delete_acc(credentials):
    '''
    Function to delete accounts
    ''' 

    credentials.delete_accounts()

def view_acc(credentials):
    '''
    Function to display saved accounts
    '''

    return Credentials.view_accounts()


def main():
    print("Welcome to Pass-key. Please create an account or sign in")
    print("\n")

    while True:

        print("Use these short codes: ca - create new Pass-key account, li -  log in to existing Pass-key account, esc - sign out of your account:")

        short_code = input().lower()

        if short_code == 'ca':
            print("New Account")
            print("-"*20)

            print("Enter your full name:")
            fullname = input().strip()

            print("Enter your Pass-key account username")
            username = input().strip()

            print("Enter your password")
            password = input().strip()

            save_user_acc(create_user_acc(fullname, username, password))#create and save a pass-key account
            print ('\n')
            print(f"New Passkey Account for {fullname} created successfuly! Your username is {username}")
            print ('\n')

            print("Please use the li short code to log into your pass key account")

        elif short_code == 'li':
            print("Enter your username")
            login_username = input().strip()

            print("Enter your password")
            login_password = input().strip()

            login = verify_acc(login_username, login_password)

            #sign in to existing account
            if verify_acc(login_username, login_password) == login:

                print(f"Welcome to your account {login_username}")
                print('-' * 20)
        
        elif short_code == 'esc':
            print("You will be signed out shortly")
            break  

        else:
            print("Please use the appropriate short codes")


if __name__ == '__main__':

    main()





