import sqlite3
import os
import json

# Create a connection
conn = sqlite3.connect('kuka.db')

# Create a cursor
c = conn.cursor()


#Create a table with the specified columns
# c.execute('''
#     CREATE TABLE IF NOT EXISTS robot_data (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         label TEXT,
#         rules TEXT,
#         intermediate_pln TEXT,
#         Structural_pln TEXT,
#         forces TEXT,
#         preference_script TEXT,
#         photo BLOB
#     )
# ''')

# Function that inserts data from a file
# Database.py



# Database.py


def insert_data_from_file(file_path, database_path='kuka.db', table_name='robot_data', *column_names):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    c = conn.cursor()

    # Check if the file exists
    if os.path.isfile(file_path):
        project_data = []  # List to accumulate data for each project

        with open(file_path, 'r') as file:
            for line in file:
                # Assuming your text file has a structured format, parse it here
                parts = line.strip().split(' ')
                
                # Extract values inside parentheses for 'O' and 'Z'
                o_values = [float(val) for val in parts[1][3:-1].split(',')]  # Extract values inside parentheses for 'O'
                z_values = [float(val) for val in parts[3][3:-1].split(',')]  # Extract values inside parentheses for 'Z'

                # Create a dictionary for 'O' and 'Z'
                data_dict = {'O': o_values, 'Z': z_values}

                # Convert the dictionary back to a JSON string before storing it in the project_data list
                data_str = json.dumps(data_dict)
                project_data.append(data_str)

        # Convert the accumulated project data into a single row entry
        row_data = ','.join(project_data)

        # Generate column names string for SQL query
        columns_str = ', '.join(column_names)

        # Generate placeholders for values in SQL query
        placeholders = ', '.join(['?' for _ in range(len(column_names))])

        # Insert data into the specified columns of the table
        c.execute(f'''
            INSERT INTO {table_name} ({columns_str})
            VALUES ({placeholders})
        ''', (row_data,))

        # Commit changes and close the connection
        conn.commit()
        conn.close()

    #     print(f"Data from '{file_path}' inserted into the '{table_name}' table.")
    # else:
    #     print(f"File '{file_path}' not found.")

# Function that deletes a record from table
# Use the id as a string so use '5' for instead of 5 i.e. delete_one('5')
def delete_one(id):
    conn = sqlite3.connect('kuka.db')
    c = conn.cursor()
    c.execute("DELETE from kuka WHERE rowid = (?)", id)
    conn.commit()
    conn.close()
# Add many records to a Table
def add_many(list):
    conn = sqlite3.connect('kuka.db')
    c = conn.cursor()
    c.executemany("INSERT INTO kuka VALUES (?,?,?)", (list))
    # Commit our command and Close Connection
    conn.commit()
    conn.close()


# Commit our command
conn.commit()

# Close our connection
conn.close()