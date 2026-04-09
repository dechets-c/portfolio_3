import os
import ssl

from dotenv import load_dotenv
from sqlalchemy import URL

load_dotenv()

db_name = os.getenv("db_name")
db_host = os.getenv("db_host")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_port = os.getenv("db_port")
db_ssl = os.getenv("db_ssl")


DATABASE_URL = URL.create(
    "postgresql+pg8000",
    username=db_user,
    password=db_password,
    host=db_host,
    database=db_name,
    port=db_port,
    ssl=db_ssl,
)

SECRET_KEY = os.getenv("secret_key")
