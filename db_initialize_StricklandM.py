"""
db_initialize_StricklandM.py

This script initializes the database by creating tables and populating them with initial data.
"""

import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def create_database():
    logging.info("Creating database...")
    with sqlite3.connect('your_database.db') as conn:
        logging.info("Database created successfully.")

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        logging.info(f"Executed SQL from {sql_file}")

def main():
    logging.info("Program started")
    
    db_filepath = 'your_database.db'
    
    # Create database
    create_database()
    
    # Execute SQL files
    execute_sql_from_file(db_filepath, 'create_tables.sql')
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    
    logging.info("Program ended")

if __name__ == "__main__":
    main()
