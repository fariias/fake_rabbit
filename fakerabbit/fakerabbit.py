import datetime
import random
import string
import typing
from typing import List

from sqlalchemy import Integer, String, DateTime, LargeBinary, inspect, Boolean, Column
from sqlalchemy.ext.declarative import declarative_base
T = typing.TypeVar("T")


class FakeRabbit:
    """A simple lib to make fake objects using SQLAlchemy"""

    def __init__(self, base_model_class: declarative_base, db_session):
        self.base_model_class = base_model_class
        self.db_session = db_session

    # Factory
    def make(self, cls, quantity: int = 1, recursive_mode: bool = True, *args, **kwargs):

        # make (quantity) (cls) objects
        for i in range(quantity):
            obj = self.instantiate_object(cls, recursive_mode, *args, **kwargs)
            self.db_session.add(obj)

        self.db_session.commit()
        return obj

    def instantiate_object(self, cls, recursive_mode: bool, *args, **kwargs):
        obj = cls(*args, **kwargs)
        attr_names = self.get_model_class_attribute_names(cls)

        for column in attr_names:
            column = column.columns[0]

            if getattr(obj, column.name):
                continue

            if column.primary_key:
                continue

            if column.foreign_keys:
                if recursive_mode:
                    foreign_cls = self.get_foreign_key_class_by_column(column)
                    foreign_obj = self.make(foreign_cls)

                    foreign_primary_key = inspect(foreign_obj).identity[0]
                    setattr(obj, column.key, foreign_primary_key)
            else:

                # Getting a fake value by class type, ex: Integer = 3
                fake_value = self.alchemy_type_generator(column.type.__class__)
                setattr(obj, column.key, fake_value)

        return obj

    ##########################
    # SQLAlchemy extra methods
    ##########################
    @staticmethod
    def get_all_model_classes(base_model_class: declarative_base,
                              ) -> List[declarative_base]:

        # Get SQLAlchemy Class Registry
        sa_class_registry: dict = getattr(base_model_class, "_decl_class_registry")

        # List of all model classes from SQLAlchemy
        model_classes = [x for x in sa_class_registry.values() if hasattr(x, "__table__")]

        return model_classes

    @staticmethod
    def get_model_class_attribute_names(cls: T):

        inst = inspect(cls)
        attr_names = [c_attr for c_attr in inst.mapper.column_attrs]

        return attr_names

    def get_foreign_key_class_by_column(self, column: Column):
        model_classes = self.get_all_model_classes(self.base_model_class)

        table = list(column.foreign_keys)[0].column.table
        classes = [c for c in model_classes if c.__table__ == table]

        if classes:
            cls = classes[0]
        else:
            cls = None

        return cls

    #################
    # Fake generators
    #################
    @staticmethod
    def make_int():
        return random.randint(1, 9999)

    @staticmethod
    def make_str(length=10):
        fake_string = ''.join(random.choice(string.ascii_lowercase) for i in range(length))
        return fake_string

    @staticmethod
    def make_datetime():
        return datetime.datetime.now()

    @staticmethod
    def make_large_binary():
        return bytes(2020)

    @staticmethod
    def make_boolean():
        return random.choice([True, False])

    def alchemy_type_generator(self, class_type: T):

        alchemy_types = {
            Integer: self.make_int,
            String: self.make_str,
            DateTime: self.make_datetime,
            LargeBinary: self.make_large_binary,
            Boolean: self.make_boolean
        }

        alchemy_type = alchemy_types.get(class_type)

        if alchemy_type:
            fake_value = alchemy_type()
        else:
            fake_value = None

        return fake_value
