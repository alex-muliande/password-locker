from user import User
from user import Credential
import unittest


class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User(
            'alex', 'nad', 'alexnad425@gmail.com', '0727719206', '1234')

    def test__init__(self):
        self.assertEqual(self.new_user.first_name, 'alex')
        self.assertEqual(self.new_user.last_name, 'nad')
        self.assertEqual(self.new_user.email, 'alexnad425@gmail.com')
        self.assertEqual(self.new_user.phone_number, '0727719206')
        self.assertEqual(self.new_user.password, 'alex')

    def tearDown(self):
        credential_list = []
        users_list = []

    def test_save_user(self):
        '''
        Method to taste if we can save the uswer details

        '''
        self.new_user.save_user()
        test_user = User('alex', 'nad', 'alexnad425@gmail.com',
                         '0727719206', '1234')
        test_user.save_user()
        self.assertEqual(User.users_list, 2)


class TestCredential(unittest.TestCase):
    def setUp(self):
        self.new_credential = Credential(
            'alex', 'muli', 'alexmuli@gmail.com', '0727719206' '12345')

    def test__init__(self):
        self.assertEqual(self.new_credential.user_name, 'alex')
        self.assertEqual(self.new_credential.site_name, 'twitter')
        self.assertEqual(self.new_credential.account_name, 'alex-muliande')
        self.assertEqual(self.new_credential.password, '12345')


if __name__ == '__main__':
    unittest.main()
