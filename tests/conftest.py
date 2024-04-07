import pytest
from app import app, db, Person, Peep
from seed_dev_database import *
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def test_client():
    """Create a test client for the Flask application."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@pytest.fixture(scope="session")
def test_web_address():
    """Provide the test web address."""
    return "localhost:5001"  # Change this port if your application runs on a different port


@pytest.fixture(scope="session")
def database():
    """Initialize and manage the database for testing."""
    db.connect()
    db.create_tables([Person, Peep], safe=True)
    seed_dev_database(db)

    yield db

    db.drop_tables([Person, Peep])
    db.close()


@pytest.fixture(scope="function")
def database_connection(database):
    """Provide a database connection for each test function."""
    yield database
