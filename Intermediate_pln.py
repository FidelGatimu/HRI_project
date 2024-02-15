# YourNewFile.py

import Database
import os

# Construct the full path to your text file
directory_path = r'#insert your file path here'
file_name = 'Sample_data.txt'
file_path = os.path.join(directory_path, file_name)

# Call the insert_data_from_file function, specifying the table columns
Database.insert_data_from_file(file_path, 'kuka.db', 'robot_data', 'intermediate_pln')

