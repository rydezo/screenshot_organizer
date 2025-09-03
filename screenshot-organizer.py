# import modules for file and datetime management
import os
import shutil
from datetime import datetime

source_folder = r"C:\Users\<ryder>\Pictures\Screenshots"
destination_folder = r"C:\Users\<ryder>\Pictures\organized-screenshots"

os.makedirs(destination_folder, exist_ok=True)

# go through all files in source folder
for filename in os.listdir(source_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        file_path = os.path.join(source_folder, filename)

        # Get creation time
        timestamp = os.path.getctime(file_path)
        dt = datetime.fromtimestamp(timestamp)

        # Format new filename
        new_filename = dt.strftime("%Y-%m-%d_%H-%M-%S") + os.path.splitext(filename)[1]
        new_path = os.path.join(destination_folder, new_filename)
        
        # If file with same name exists, append a counter
        counter = 1
        while os.path.exists(new_path):
            new_filename = dt.strftime("%Y-%m-%d_%H-%M-%S") + f"_{counter}" + os.path.splitext(filename)[1]
            new_path = os.path.join(destination_folder, new_filename)
            counter += 1

        # Move and rename file
        shutil.move(file_path, new_path)
        print(f"Moved: {filename} → {new_filename}")

print("all screenshots processed!")
