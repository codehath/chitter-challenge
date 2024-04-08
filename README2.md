# Chitter Challenge: A Twitter Clone

Chitter Challenge is a portfolio project that demonstrates my skills in building a full-stack web application. It is a Twitter-like social media platform that allows users to post messages (called "peeps"), view peeps from other users, and interact with the application through user authentication and authorization.

## Features

-   User Registration and Authentication:

    -   Users can create an account by providing their name, username, email, and password.
    -   Passwords are securely hashed using bcrypt before storing them in the database.
    -   Registered users can log in using their username and password.
    -   User sessions are managed using Flask's session functionality.

-   Peep Creation and Viewing:

    -   Logged-in users can post peeps by submitting a form with the peep content.
    -   Peeps are displayed in reverse chronological order on the home page and the user's home page.
    -   Each peep includes the content, timestamp, and the username of the author.

-   User Authorization:

    -   Only authenticated users can access the home page and post peeps.
    -   Unauthenticated users are redirected to the login page.

-   Responsive Web Design:
    -   The application is built with a responsive layout that adapts to different screen sizes.
    -   It provides a seamless user experience across desktop and mobile devices.

## Tech Stack

-   Backend:

    -   Python
    -   Flask (Web Framework)
    -   Peewee (ORM)
    -   PostgreSQL (Database)
    -   bcrypt (Password Hashing)

-   Frontend:

    -   HTML
    -   CSS
    -   JavaScript

-   Testing:

    -   Pytest (Testing Framework)
    -   Pytest-Flask (Flask Testing Utilities)

-   Version Control:
    -   Git

## Skills Demonstrated

Through the development of this project, I have demonstrated the following skills:

-   Building a full-stack web application using Python and Flask.
-   Implementing user authentication and authorization.
-   Securely storing and handling user passwords using bcrypt hashing.
-   Utilizing an ORM (Peewee) for database management and querying.
-   Designing and structuring a relational database schema.
-   Creating responsive web pages using HTML, CSS, and JavaScript.
-   Writing unit tests to ensure the correctness of the application's functionality.
-   Managing project dependencies using Pipenv.
-   Deploying a Flask application to a production environment.
-   Using version control (Git) for code management and collaboration.

## Getting Started

To run the Chitter Challenge application locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/chitter-challenge.git`
2. Install the project dependencies: `pipenv install`
3. Set up the environment variables in the `.env` file.
4. Run the database migrations: `python seed_dev_database.py`
5. Start the application: `python app.py`
6. Access the application in your web browser at `http://localhost:5001`.

For detailed installation instructions and usage guidelines, please refer to the [Installation](INSTALLATION.md) and [Usage](USAGE.md) documents.

## Testing

To run the unit tests for the Chitter Challenge application, use the following command:

```
pytest
```

The tests cover various aspects of the application, including user registration, login, peep creation, and authentication.

## Future Enhancements

Some potential enhancements for the Chitter Challenge application include:

-   Implementing user profiles with profile pictures and bio information.
-   Adding the ability to follow other users and view their peeps.
-   Introducing features like liking and commenting on peeps.
-   Implementing real-time updates using WebSocket technology.
-   Enhancing the user interface with more advanced styling and animations.

## Contact

If you have any questions, feedback, or suggestions regarding this project, please feel free to reach out to me at [your-email@example.com](mailto:your-email@example.com). I would be happy to discuss further or provide additional information.

Thank you for considering my Chitter Challenge project. I hope it demonstrates my skills and passion for web development.
