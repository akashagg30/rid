# In settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db1',
        'USER': 'main_user',
        'PASSWORD': 'main_pass',
        'HOST': 'localhost',  # Or your PostgreSQL host
        'PORT': '5432',       # Or your PostgreSQL port
    }
}

PRINT_QUERY = True
PRINT_QUERY = False




# CREATE DATABASE db1;
# CREATE USER main_user WITH PASSWORD 'main_pass';
# ALTER ROLE main_user SET client_encoding TO 'utf8';
# ALTER ROLE main_user SET default_transaction_isolation TO 'read committed';
# ALTER ROLE main_user SET timezone TO 'UTC';
# GRANT ALL PRIVILEGES ON DATABASE db1 TO main_user;
# GRANT ALL PRIVILEGES TO main_user;
