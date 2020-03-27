from tests.basetest import BaseTest
from tests.modeltest import User


class TestCreateObjects(BaseTest):

    def test_create_user(self):
        """ Test create a simple object"""

        # Creating a new user using Fake Rabbit
        self.user = self.fake_rabbit.make(User)

        users_in_db = self.session.query(User).all()

        self.assertEqual(1, len(users_in_db))

    def test_create_multiple_users(self):
        """Test create multiple objects"""

        self.users = self.fake_rabbit.make(User, 10)

        users_in_db = self.session.query(User).all()

        self.assertEqual(10, len(users_in_db))

    def test_create_user_with_recursive_mode(self):
        """Test create a object with foreign key objects (default)"""
        self.user = self.fake_rabbit.make(User)

        self.assertIsNotNone(self.user.addressid)

    def test_create_user_without_recursive_mode(self):
        """Test create a object without foreign key objects"""

        self.user = self.fake_rabbit.make(User, recursive_mode=False)

        self.assertIsNone(self.user.addressid)

    def test_create_user_with_default_values(self):
        """Test create a object using default values"""

        default_fullname = 'Tony Stark'

        self.user = self.fake_rabbit.make(User, recursive_mode=False, fullname=default_fullname)

        self.assertEqual(self.user.fullname, default_fullname)

        users_in_db = self.session.query(User).filter(User.fullname == default_fullname).all()
        self.assertEqual(1, len(users_in_db))






