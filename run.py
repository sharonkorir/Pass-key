#!/usr/bin/env python3.8

from user import User
from credentials import Credentials

#create user account
def create_user_acc(fullname, username, email, password):
    '''
    Function to create a pass key account
    '''
    new_user = User(fullname, email, username, password)
    return new_user

#verify and login to account
def verify_acc(user):
    '''
    Function to log in to account
    '''
    user.verify_account()
    return User.verify_account

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





