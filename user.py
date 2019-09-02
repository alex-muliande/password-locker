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
