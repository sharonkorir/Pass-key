#!/usr/bin/env python3.8

from click import password_option
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
def save_acc(credentials):
    '''
    function to save existing account credentials to accounts list
    '''
    credentials.save_accounts()

def create_new_acc(account_name, account_user_name, account_password):
    '''
    function to create new account with existing password
    '''
    new_credentials = Credentials(account_name, account_user_name, account_password)
    return new_credentials

def generate_pwd(credentials):
    '''
    Function to generate random password
    '''

    random_pwd = credentials.generate_password()
    return random_pwd

def delete_acc(credentials):
    '''
    Function to delete accounts
    ''' 

    credentials.delete_accounts()

def view_acc():
    '''
    Function to display saved accounts
    '''

    return Credentials.view_accounts()

def find_acc(credentials):
    '''
    Function to search existing account credentials
    '''

    return Credentials.find_account(credentials)


def main():
    print("Welcome to Pass-key. Please create an account or sign in")
    print("\n")

    while True:

        print("Use these short codes: ca - create new Pass-key account, li -  log in to existing Pass-key account")

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
                print('-' * 40)

            else:
                print("Account does not exist, please use ca to create account")

        while True:
            print("Use these short codes: sc - save existing account credentials, cc - create new account credentials, dc - delete credentials, vc - display account credentials ")
            
            short_code = input().lower()
            if short_code == 'sc':
                print("Save your existing account credentials")
                print("-"*20)

                print("Enter the account name:")
                account_name = input().strip()

                print("Enter your account username")
                account_username = input().strip()

                print("Enter your account password")
                account_password = input().strip()

                save_acc(create_new_acc(account_name, account_username, account_password))#save existing accounts and credentials
                print ('\n')
                print(f"Your {account_name} credentials have been saved successfully")
                print ('\n')

            elif short_code == 'cc':
                print("Enter new account credentials")
                print("-"*20)

                print("Enter the account name:")
                account_name = input().strip()

                print("Enter your account username:")
                account_username = input().strip()

                print("Use op - to use your own password, rp -to generate a random password")
                password_option = input().lower().strip()

                if password_option == 'op':
                    print("Enter your account password")
                    account_password = input().strip()

                elif password_option == 'rp':
                    account_password = generate_pwd()

                else:
                    print("invalid choice, please select 'op' or 'rp'")

                save_acc(create_new_acc(account_name, account_username, account_password))#save new credentials
                print ('\n')
                print(f"Your {account_name} account has been created successfuly. Your username is {account_username} and your password in {account_password}")
                print ('\n')

            elif short_code == 'vc':
                if view_acc():
                    print("This is a list of your accounts:")
                    print('-'*40)
                    for accounts in view_acc():
                        print(f"Account:{account_name} \n User name: {account_username} \n Password: {account_password}")

                else:
                    print("Account does not exist")

            elif short_code == 'dc':

                print("Please enter the account name of the account you want to delete")
                delete_name = input().strip()
                if find_acc(delete_name):
                    search_acc = find_acc(delete_name)
                    print("-"*40)
                    search_acc.delete_acc()
                    print(f"\n Your {search_acc.account_name} account credentials have been deleted")
                    
                else:
                    print("Account does not exist")
        else:
            print("Please use the appropriate short codes")
            print("-"*20)


if __name__ == '__main__':

    main()





