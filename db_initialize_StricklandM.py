"""
ddb_initialize_StricklandM.py

This script initializes the database by creating tables and populating them with initial data.
"""

import os
import sqlite3
import pandas
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
    
    # Get the current working directory
    current_dir = os.getcwd()
    
    # Construct the relative paths to the SQL files
    create_tables_path = os.path.join(current_dir, 'create_tables.sql')
    insert_records_path = os.path.join(current_dir, 'insert_records.sql')
    
    # Check if the files exist before executing
    if not os.path.isfile(create_tables_path):
        logging.error(f"File not found: {create_tables_path}")
        return
    if not os.path.isfile(insert_records_path):
        logging.error(f"File not found: {insert_records_path}")
        return
    
    # Create database
    create_database()
    
    # Execute SQL files with constructed paths
    execute_sql_from_file(db_filepath, create_tables_path)
    execute_sql_from_file(db_filepath, insert_records_path)
    
    logging.info("Program ended")

if __name__ == "__main__":
    main()
