"""
db_operations_StricklandM.py

This script performs various SQL operations such as updates, deletions, and queries on the database.
"""

import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        logging.info(f"Executed SQL from {sql_file}")

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
