from playwright.sync_api import Page, expect

# Tests for your routes go here

# === Example Code Below ===

"""
We can get an emoji from the /emoji page
"""
# def test_get_emoji(page, test_web_address): # Note new parameters
#     # We load a virtual browser and navigate to the /emoji page
#     page.goto(f"http://{test_web_address}/emoji")

#     # We look at the <strong> tag
#     strong_tag = page.locator("strong")

#     # We assert that it has the text ":)"
#     expect(strong_tag).to_have_text(":)")

# # === End Example Code ===


# Integration/Functional Tests
def test_home_page(test_client):
    """Test the home page."""
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Chitter!" in response.data


def test_register_page(test_client):
    """Test the register page."""
    response = test_client.get("/register")
    assert response.status_code == 200
    assert b"Welcome to Chitter!" in response.data


def test_login_page(test_client):
    """Test the login page."""
    response = test_client.get("/login")
    assert response.status_code == 200
    assert b"Login!" in response.data


def test_invalid_login(test_client):
    """Test invalid login."""
    response = test_client.post(
        "/login", data={"username": "invalid", "password": "invalid"}
    )
    assert response.status_code == 200
    assert b"Invalid username" in response.data


def test_valid_login(test_client):
    """Test valid login."""
    response = test_client.post("/login", data={"username": "user", "password": "pass"})
    assert response.status_code == 302  # Redirect to home page after successful login


def test_logout(test_client):
    """Test logout."""
    response = test_client.delete("/home")
    assert response.status_code == 302  # Redirect to home page after logout


def test_create_peep(test_client):
    """Test creating a peep."""
    response = test_client.post("/home", data={"content": "Test Peep"})
    assert response.status_code == 200
    assert b"Test Peep" in response.data


def test_view_home_logged_in(test_client):
    """Test viewing home page when logged in."""
    test_client.post("/login", data={"username": "user", "password": "pass"})
    response = test_client.get("/home")
    assert response.status_code == 200
    assert b"Welcome to Chitter" in response.data
