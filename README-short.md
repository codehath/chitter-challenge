# Chitter: A Twitter Clone

Chitter is a portfolio project developed in Week 4 of the Makers Academy software engineering course. It showcases the skills and knowledge acquired by building a full-stack web application that mimics the basic functionality of Twitter. The project demonstrates the ability to plan, design, and implement a functional web application from scratch using Python, Flask, and Peewee ORM for database management.

## Features

-   User Registration and Authentication
-   Secure Password Hashing with Bcrypt
-   User Session Management
-   Peep Creation and Viewing
-   User Authorization and Redirection
-   Responsive Web Design
-   User Logout

## Tech Stack

| Layer    | Technology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Backend  | ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![Peewee](https://img.shields.io/badge/Peewee-ORM-black?style=for-the-badge) ![Bcrypt](https://img.shields.io/badge/Bcrypt-Password%20Hashing-yellow?style=for-the-badge) |
| Frontend | ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white) ![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black) ![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)                                                                     |
| Testing  | ![Pytest](https://img.shields.io/badge/Pytest-Testing-red?style=for-the-badge) ![Playwright](https://img.shields.io/badge/Playwright-45ba4b?style=for-the-badge&logo=Playwright&logoColor=white)                                                                                                                                                                                                                                                                                                                 |
| Tools    | ![TablePlus](https://img.shields.io/badge/TablePlus-Database%20GUI-orange?style=for-the-badge)                                                                                                                                                                                                                                                                                                                                                                                                                   |

## Technical Approach and Skills Demonstrated

-   Full-stack development with Python, Flask, and HTML/CSS/JavaScript
-   User authentication, authorization, and secure password hashing
-   PostgreSQL database schema design and management with Peewee ORM
-   Responsive web design using HTML Jinja templates, Bootstrap, and CSS
-   Unit testing with Pytest and end-to-end testing with Playwright
-   Dependency management with Pipenv
-   Version control and collaboration using Git and GitHub

## Prerequisites

-   Python 3.x
-   Pipenv

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/your-username/chitter-challenge.git
    ```

2. Navigate to the project directory:

    ```
    cd chitter-challenge
    ```

3. Install the project dependencies using Pipenv:

    ```
    pipenv install
    ```

4. Set up the environment variables in a `.env` file:

    ```
    DB_NAME=your_database_name
    DB_USER=your_database_username
    DB_PASSWORD=your_database_password
    DB_HOST=your_database_host
    SECRET_KEY=your_secret_key
    ```

5. Activate the virtual environment:

    ```
    pipenv shell
    ```

6. Run the database migrations:

    ```
    python seed_dev_database.py
    ```

7. Start the application:

    ```
    python app.py
    ```

8. Access the application at `http://localhost:5001`.

## Testing

Run unit tests:

```
pytest
```

## Future Development

-   User
