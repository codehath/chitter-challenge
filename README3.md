# Chitter Challenge: A Twitter Clone

Chitter Challenge is a portfolio project developed as part of the Makers Academy software engineering course. It showcases the skills and knowledge acquired during the course by building a full-stack web application that mimics the basic functionality of Twitter. The project was completed individually, demonstrating the ability to plan, design, and implement a functional web application from scratch.

## Features

The Chitter Challenge application offers the following features:

-   User Registration and Authentication:

    -   Users can create an account by providing their name, username, email, and password.
    -   Passwords are securely hashed using bcrypt before storing them in the database.
    -   Registered users can log in using their username and password.
    -   User sessions are managed using Flask's session functionality.

-   Peep Creation and Viewing:

    -   Logged-in users can post short messages called "peeps" by submitting a form with the peep content.
    -   Peeps are displayed in reverse chronological order on the home page and the user's profile page.
    -   Each peep includes the content, timestamp, and the username of the author.

-   User Authorization:

    -   Only authenticated users can access the home page and post peeps.
    -   Unauthenticated users are redirected to the login page.

-   Responsive Web Design:
    -   The application is built with a responsive layout that adapts to different screen sizes.
    -   It provides a seamless user experience across desktop and mobile devices.

## Tech Stack

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=flat&logo=javascript&logoColor=%23F7DF1E)
![Peewee](https://img.shields.io/badge/Peewee-ORM-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=flat&logo=postgresql&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-blue)
![Bcrypt](https://img.shields.io/badge/Bcrypt-Password%20Hashing-blue)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange)
![GitHub](https://img.shields.io/badge/GitHub-Code%20Hosting-black)

## Skills Demonstrated

Through the development of the Chitter Challenge project, the following skills were demonstrated:

-   Building a full-stack web application using Python and Flask framework
-   Implementing user registration, authentication, and authorization
-   Securely storing and handling user passwords using bcrypt hashing
-   Utilizing an ORM (Peewee) for database management and querying
-   Designing and structuring a relational database schema using PostgreSQL
-   Creating responsive web pages using HTML, CSS, and JavaScript
-   Writing unit tests using the Pytest testing framework to ensure code quality and functionality
-   Managing project dependencies using Pipenv
-   Implementing version control using Git and hosting the codebase on GitHub

## Getting Started

To run the Chitter Challenge application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/chitter-challenge.git`
2. Install the project dependencies: `pipenv install`
3. Set up the environment variables in the `.env` file.
4. Run the database migrations: `python seed_dev_database.py`
5. Start the application: `python app.py`
6. Access the application in your web browser at `http://localhost:5001`.

## Testing

To run the unit tests for the Chitter Challenge application, use the following command:

```
pytest
```

The tests cover various aspects of the application, including user registration, login, peep creation, and authentication.

## Future Enhancements
