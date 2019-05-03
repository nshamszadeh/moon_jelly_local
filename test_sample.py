# content of test_sample.py
#
import pytest
from app import User

@pytest.fixture(scope='module')
def new_user():
    user = User('hi@gmail.com', 'first', 'last', 'specialty')
    return user

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, name, and specialty are good to go
    """
    assert new_user.email == 'hi@gmail.com'
    assert new_user.first_name == 'first'
    assert new_user.last_name == 'last'
    assert new_user.specialty == 'specialty'

    
