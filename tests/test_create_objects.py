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



