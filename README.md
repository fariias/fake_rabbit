Fake Rabbit
===========

Fake Rabbit is a simple lib to make fake objects using SQLAlchemy. 

Installing
--------

```shell script 
$ pip install fakerabbit
```    
 
Using
--------

```python 
    
    # First, we need to instantiate the library
    fake_rabbit = FakeRabbit(my_base_model, my_db_session)
    
    # EX: creating a new user object
    user = fake_rabbit.make(User)
```
    
    
    