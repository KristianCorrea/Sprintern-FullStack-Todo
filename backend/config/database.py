import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session

# Load environment variables from .env file
load_dotenv()

# Load database credentials from environment variables
mysql_name = os.getenv("MYSQL_NAME")
mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_host = os.getenv("MYSQL_HOST")
mysql_port = os.getenv("MYSQL_PORT")

# Construct MySQL connection URL using PyMySQL driver
# Format: mysql+pymysql://username:password@host:port/database_name
mysql_url = f"mysql+pymysql://{mysql_user}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_name}"

# Create database engine using the connection URL
# This establishes a connection pool to the database
engine = create_engine(mysql_url)

def create_db_and_tables():
    # This will create all tables that don't exist yet based on the SQLModel metadata
    SQLModel.metadata.create_all(engine)

# Function to provide a database session context
def get_session():
    # Create a new session using the engine
    with Session(engine) as session:
        # Yield the session to the caller
        # This allows the session to be used as a context manager or dependency
        yield session