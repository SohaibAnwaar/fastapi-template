from fastapi.testclient import TestClient
from app.main import app
import pytest

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.databasecon import get_db
from app.databasecon import Base

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Fixture connects to the Database, drops all old data in tables and creates a new one


@pytest.fixture
def session():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Fixture is a fresh database client


@pytest.fixture
def client(session):
    def override_get_db():
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)

# Fixture used to add the needed data into the DB before attempting the test_create_user


@pytest.fixture
def test_createdata(client):

    enterprise_data = {"name": "iiot"}
    res = client.post("/enterprises/", json=enterprise_data)
    assert res.status_code == 201

# Fixture creates a User before attempting the test_login_user


@pytest.fixture
def test_user(client, test_createdata):
    user_data = {"fname": "Aadil",
                 "lname": "Feroze",
                 "email": "aadil@gmail.com",
                 "role": "admin",
                 "department": "admin",
                 "enterprise_id": 1,
                 "password": "cmms123"
                 }
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user

# Fixture creates a User with admin role, authenticates it and returns headers for authentication for all API calls


@pytest.fixture
def test_headers(client, test_createdata):
    user_data = {"fname": "Aadil",
                 "lname": "Feroze",
                 "email": "aadil@gmail.com",
                 "role": "admin",
                 "department": "admin",
                 "enterprise_id": 1,
                 "password": "cmms123"
                 }
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201

    new_user = res.json()
    new_user['password'] = user_data['password']
    res = client.post(
        "/authenticate/", data={"username": new_user['email'], "password": new_user['password']})
    token = res.json()['access_token']
    headers = {}
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer "+token
    return headers

# Fixture creates a User with developer role, authenticates it and returns headers for authentication for all API calls


@pytest.fixture
def test_header(client, test_createdata):
    user_data = {"fname": "Test",
                 "lname": "User",
                 "email": "test_user@gmail.com",
                 "role": "developer",
                 "department": "maintenance",
                 "enterprise_id": 1,
                 "password": "cmms123"
                 }
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    print(res)

    new_user = res.json()
    new_user['password'] = user_data['password']
    res = client.post(
        "/authenticate/", data={"username": new_user['email'], "password": new_user['password']})
    token = res.json()['access_token']
    headers = {}
    headers["Accept"] = "application/json"
    headers["Authorization"] = "Bearer "+token
    return headers
