import json
import os
import unittest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from fakerabbit import FakeRabbit
from tests.modeltest import MyBaseModel


class BaseTest(unittest.TestCase):

    def setUp(self) -> None:
        db = create_engine("sqlite:///dbtest.sqlite",
                           connect_args={'check_same_thread': False})

        MyBaseModel.metadata.create_all(db)

        self.session = scoped_session(sessionmaker(bind=db))

        self.fake_rabbit = FakeRabbit(MyBaseModel, db_session=self.session)

        # Run SetUpCustom
        self.setUpCustom()

    def tearDown(self) -> None:
        os.remove('dbtest.sqlite')

    def setUpCustom(self):
        pass
