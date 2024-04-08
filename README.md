# Chitter Challenge

Chitter Challenge is a basic social media application that allows users to post messages (called "peeps") and view peeps from other users. It is built using Python, Flask, and Peewee ORM for database management.

## Features

-   User Registration: Users can create an account by providing their name, username, email, and password.
-   User Login: Registered users can log in using their username and password.
-   Peep Creation: Logged-in users can post peeps by submitting a form with the peep content.
-   Peep Viewing: All peeps are displayed in reverse chronological order on the home page and the user's home page.
-   User Logout: Logged-in users can log out of the application.

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

## Usage

-   Register a new account by providing the required information on the registration page.
-   Log in using your registered username and password.
-   On the home page, you can view all the peeps posted by users.
-   To post a new peep, enter the peep content in the provided form on the home page and click "Post".
-   To log out, click the "Logout" button.

## Testing

The project includes unit tests to ensure the correctness of the implemented features. To run the tests, use the following command:

```
pytest
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

-   [Flask](https://flask.palletsprojects.com/) - The web framework used.
-   [Peewee](http://docs.peewee-orm.com/) - The ORM library used for database management.
-   [Pytest](https://docs.pytest.org/) - The testing framework used.

## Contact

If you have any questions or feedback, please contact the project maintainer at [your-email@example.com](mailto:your-email@example.com).
