
#! /usr/bin/env python3
import pyperclip
from user import User
from user import Credential


def create_user(first_name, last_name, email, phone_number, password):
    '''
    Function to create a new user account
    '''
    new_user = User(first_name, last_name, email, phone_number, password)
    return new_user


def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)


def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = Credential.check_user(first_name, password)
    return checking_user


def generate_password(pass_len):
    '''
    A funtion to generate password, combining random letters and digits
    '''
    return Credential.generate_password(pass_len)
    # @classmethod
    # def display_credentials(cls,uname):
    #     '''
    #     A class method that displays all credentials of a given username.
    #     '''
    #     return Credentials.display_credentials(cls, uname)
@classmethod
def find_by_site_name(cls, site_name):
    '''
    A function to search for credentials when given an account site search as google, or twitter.
    '''
    return cls.find_by_site_name(cls, site_name)

@classmethod
def copy_credentials(cls, site_name):
    '''
    A class method to enable us to copy credentials of a given site name.
    '''
    return cls.copy_credentials(cls, site_name)


def main():
