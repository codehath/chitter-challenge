# Chitter Challenge: A Twitter Clone

Chitter Challenge is a portfolio project developed as part of the Makers Academy software engineering course. It showcases the skills and knowledge acquired during the course by building a full-stack web application that mimics the basic functionality of Twitter. The project was completed individually, demonstrating the ability to plan, design, and implement a functional web application from scratch. It is built using Python, Flask, and Peewee ORM for database management.

## Features

-   **User Registration**: Users can create an account by providing their name, username, email, and password.
-   User Login: Registered users can log in using their username and password.
-   **Authentication:** Passwords are securely hashed using bcrypt before storing them in the database.
-   **Security:** User sessions are managed using Flask's session functionality.
-   **Peep Creation**: Only authenticated users can access the home page to post peeps.
-   **Peep Viewing**: All peeps are displayed in reverse chronological order on the home page and the user's home page.
-   **User Logout**: Logged-in users can log out of the application.
-   **Responsiveness:** The application is built with a responsive layout that adapts to different screen sizes.
-   **Redirect**: Unauthenticated users are redirected to the login page.

## Tech Stack

| Layer    | Technology                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Backend  | ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%23316192.svg?style=flat&logo=postgresql&logoColor=white) ![Peewee](https://img.shields.io/badge/Peewee-ORM-blue) ![Bcrypt](https://img.shields.io/badge/Bcrypt-Password%20Hashing-blue) |
| Frontend | ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=flat&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=flat&logo=css3&logoColor=white) ![Jinja](https://img.shields.io/badge/Jinja-Templating-red) ![Bootstrap](https://img.shields.io/badge/Bootstrap-CSS%20Framework-blueviolet)                                                                                                 |
| Testing  | ![Pytest](https://img.shields.io/badge/Pytest-Testing-blue) ![Playwright](https://img.shields.io/badge/Playwright-End--to--End%20Testing-green)                                                                                                                                                                                                                                                                                            |
| Tools    | ![TablePlus](https://img.shields.io/badge/TablePlus-Database%20GUI-blue)                                                                                                                                                                                                                                                                                                                                                                   |

## Skills Demonstrated

Through the development of the Chitter Challenge project, the following skills were demonstrated:

-   Designing and structuring a relational database schema using PostgreSQL

## Technical Approach and Skills Demonstrated

The Chitter Challenge project was developed using a full-stack approach, utilizing Python and the Flask framework for the backend and HTML, CSS, and JavaScript for the frontend. The project showcases the following technical skills and development processes:

-   **User Authentication and Authorization:** Implemented user registration, authentication, and authorization mechanisms to ensure secure access to the application. Passwords are securely hashed using bcrypt for added security.
-   **Schema Design:** Designed and structured a relational database schema using PostgreSQL, ensuring efficient data storage and retrieval.
-   **Database Management:** Utilized the Peewee ORM for database management and querying, effectively interacting with the PostgreSQL database to store and retrieve user data and peeps.
-   **Responsive Web Design:** Designed and developed responsive web pages using HTML Jinja templates, Bootstrap and CSS ensuring a seamless user experience across different devices and screen sizes.
-   **Testing and Quality Assurance:** Implemented unit tests using the Pytest testing framework and Playwright to ensure the correctness and functionality of the application's codebase.
-   **Dependency Management:** Managed project dependencies effectively using Pipenv, ensuring a consistent and isolated development environment.
-   **Version Control and Collaboration:** Utilized Git for version control and hosted the codebase on GitHub, enabling collaborative development and version tracking.

Through the development of this project, I have demonstrated proficiency in these technical skills and a systematic approach to software development, including design, implementation, testing, and deployment.

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

4. Set up the environment variables:

    - Create a `.env` file in the project root.
    - Add the following variables to the `.env` file:

        ```
        DB_NAME=your_database_name
        DB_USER=your_database_username
        DB_PASSWORD=your_database_password
        DB_HOST=your_database_host
        SECRET_KEY=your_secret_key
        ```

        Replace `your_database_name`, `your_database_username`, `your_database_password`, `your_database_host`, and `your_secret_key` with your actual database and secret key values.

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

8. Access the application in your web browser at `http://localhost:5001`.

## Testing

To run the unit tests for the Chitter Challenge application, use the following command:

```
pytest
```

## Future Developement

Some additional features I may implement for Chitter:

-   Implementing user profiles with profile pictures and bio information.
-   Adding the ability to follow other users and view their peeps.
-   Introducing features like liking and commenting on peeps.
-   Implementing real-time updates using WebSocket technology.
-   Enhancing the user interface with more advanced styling and animations.
