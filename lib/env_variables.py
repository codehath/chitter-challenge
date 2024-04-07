from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get database configuration from environment variables or use default values
db_name = os.environ.get("DB_NAME", "default_db_name")
db_user = os.environ.get("DB_USER", "default_user")
db_password = os.environ.get("DB_PASSWORD", "")
db_host = os.environ.get("DB_HOST", "localhost")
