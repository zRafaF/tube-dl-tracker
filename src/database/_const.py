# Copyright (c) 2024 Rafael F. Meneses
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT
from peewee import SqliteDatabase
import os

# Define the directory for the database file
db_directory = "app-data"
db_file = "db.db"

# Create the directory if it doesn't exist
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

db_path = os.path.join(db_directory, db_file)
DATABASE = SqliteDatabase(db_path)
