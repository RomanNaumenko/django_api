import pytest
from core.user.models import User

user_data = {"username": "test_user",
             "email": "test@gmail.com",
             "first_name": "Test",
             "last_name": "User",
             "password": "test_password"}

superuser_data = {"username": "test_superuser",
                  "email": "testsuperuser@gmail.com",
                  "first_name": "Test",
                  "last_name": "Superuser",
                  "password": "test_password"}


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**user_data)
    assert user.username == 'test_user'
    assert user.username == user_data['username']
    assert user.email == 'test@gmail.com'
    assert user.email == user_data['email']
    assert user.first_name == 'Test'
    assert user.first_name == user_data['first_name']
    assert user.last_name == 'User'
    assert user.last_name == user_data['last_name']
    # assert user.password == 'test_password'  Через шифрування паролів тест не пройде
    # assert user.password == user_data['password']


@pytest.mark.django_db
def test_create_superuser():
    user = User.objects.create_superuser(**superuser_data)
    assert user.username == superuser_data["username"]
    assert user.email == superuser_data["email"]
    assert user.first_name == superuser_data["first_name"]
    assert user.last_name == superuser_data["last_name"]
    assert user.is_superuser == True
    assert user.is_staff == True
