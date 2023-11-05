from typing import List
import sqlalchemy
import os
import urllib

#DATABASE_URL = "sqlite:///./test.db"

host_server = os.environ.get('HOST_SERVER', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('DB_SERVER_PORT', '5432')))
database_name = os.environ.get('DB_NAME', 'fastapi')
db_username = urllib.parse.quote_plus(str(os.environ.get('DB_USERNAME', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('DB_PASSWORD', 'secret')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('SSL_MODE','prefer')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}?sslmode={}'.format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)

print(DATABASE_URL)