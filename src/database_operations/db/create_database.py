from pathlib import Path
import sqlite3

# Get the parent directory of the script (assuming the script is in the 'db' folder)
script_directory = Path(__file__).parent.parent.resolve()

# Define the path where you want to create the database
database_path = script_directory.parent.parent / 'data' / 'search_engine.db'

# Connect to the SQLite database
conn = sqlite3.connect(database_path)

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the 'documents' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        document_id INTEGER PRIMARY KEY,
        file_path TEXT UNIQUE NOT NULL,
        text_content TEXT NOT NULL,
        time_created TIMESTAMP NOT NULL
    )
''')

# Create the 'inverted_index' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inverted_index (
        term TEXT NOT NULL,
        document_id INTEGER,
        FOREIGN KEY (document_id) REFERENCES documents (document_id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
