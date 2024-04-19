import shutil
import os
from datetime import datetime

def create_backup(source_file, backup_dir):
    
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)


    now = datetime.now()
    date_folder = now.strftime("%Y.%m.%d")

    backup_path = os.path.join(backup_dir, date_folder)

    if not os.path.exists(backup_path):
        os.makedirs(backup_path)

        # Copy the file to the backup folder
    shutil.copy(source_file, backup_path)

if __name__ == "__main__":
    # Replace 'source_file_path' with the path to your source file
    source_file_path = r"C:\Users\lucag\OneDrive\Área de Trabalho\2024.1\Data Mining\ACOMPANHAMENTO FIDC.xlsx"
    
    # Replace 'backup_directory' with the path to the directory where you want to store backups
    backup_directory = r"C:\Users\lucag\OneDrive\Área de Trabalho\2024.1\Data Mining\backups"
    
    create_backup(source_file_path, backup_directory)
