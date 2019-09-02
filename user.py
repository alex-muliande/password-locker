import string
import secrets
import pyperclip


class User:
    """
    Class that generates new instances of user
    """

    users_list = []

    def __init__(self, first_name, last_name, email, phone_number, password):
        '''
        Method to define the properties for each user object will hold.
        '''

        # instance variables
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.password = password

    def save_user(self):
        '''
        Function to save a newly created user instance
        '''
        User.users_list.append(self)

    def delete_user(self):
        '''
        Function to delete user information
        '''
        User.users_list.remove(self)


class Credential:
    '''
    class to create account credentials,generate passwords and save there information
    '''
    credential_list = []
    user_crediatials_list = []
    @classmethod
    def check_user(cls, first_name, password):
        '''
        Method that checks if the name and password entered match entries in the user_list
        '''
        current_user = ''
        for user in User.users_list:
            if (user.first_name == first_name and user.password == password):
                current_user = user.first_name
                return current_user

    def __init__(self, user_name, site_name, account_name, password):
        '''
        Method to define the properties for each user object will hold.
        '''

        # instance variables
        self.user_name = user_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):

        Credential.credential_list.append(self)

    def delete_credentials(self):

        Credential.credential_list.remove(self)

    def generate_password(self, pass_len=6):

        password_chars = string.ascii_letters + string.digits + string.punctuation

        return ''.join(secrets.choice(password_chars) for i in range(int(pass_len)))

    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        A method to search for credentials associated with a given account type.
        '''
        for credential in cls.credential_list:
            if credential.site_name == site_name:

                return credential

    @classmethod
    def copy_credentials(cls, site_name):
        '''
        Class method that copies a credential's info after the credential's account site is entered
        '''
        found_credential = cls.find_by_site_name(site_name)
        return pyperclip.copy(found_credential.account_password)
