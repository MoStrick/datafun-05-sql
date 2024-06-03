"""
db_operations_StricklandM.py

This script performs various SQL operations such as updates, deletions, and queries on the database.
"""

import sqlite3
import logging
import os

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s')




def execute_sql_from_file(db_filepath, sql_file):
    # Log the value of db_filepath
    logging.info(f"Database file path: {db_filepath}")
    
    # Check if the database file exists
    if not os.path.isfile(db_filepath):
        logging.error(f"Database file '{db_filepath}' not found")
        return
    
    try:
        with sqlite3.connect(db_filepath) as conn:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            logging.info(f"Executed SQL from {sql_file}")
    except sqlite3.Error as e:
        logging.error(f"Error executing SQL from {sql_file}: {e}")

# Generate SQL commands and write to delete_records.sql
with open('delete_records.sql', 'w') as file:
    file.write("""
    -- delete_records.sql

    DELETE FROM books WHERE book_id = '1';
    DELETE FROM authors WHERE author_id = '2';
    """)


def main():
    logging.info("SQL operations started")
    
    db_filepath = 'your_database.db'

    # Execute SQL files for various operations
    execute_sql_from_file(db_filepath, 'update_records.sql')
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    execute_sql_from_file(db_filepath, 'query_aggregation.sql')
    execute_sql_from_file(db_filepath, 'query_filter.sql')
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    execute_sql_from_file(db_filepath, 'query_join.sql')
    

    logging.info("All SQL operations completed successfully")

if __name__ == "__main__":
    main()
