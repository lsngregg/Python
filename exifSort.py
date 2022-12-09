"""

 Code generated with openai.com
 Promt: write a python script using exif 1.4.0 to sort raw image files
    in all subdirectories into folders by YYYY/Month

"""

import os
import exifread
from datetime import datetime

# Set the directory to search for files
directory = "C:\\my\\directory"

# Get a list of all raw image files in the specified directory and its subdirectories
raw_image_files = [
    os.path.join(root, filename)
    for root, _, filenames in os.walk(directory)
    for filename in filenames
    if filename.endswith(".raw")
]

# Loop through each raw image file
for filepath in raw_image_files:
    # Open the file and read its EXIF data
    with open(filepath, "rb") as f:
        exif_data = exifread.process_file(f, details=False)

    # Get the date and time when the photo was taken
    datetime_str = exif_data["EXIF DateTimeOriginal"]
    datetime_obj = datetime.strptime(str(datetime_str), "%Y:%m:%d %H:%M:%S")

    # Create a folder for the year and month when the photo was taken
    year = datetime_obj.strftime("%Y")
    month = datetime_obj.strftime("%B")
    folder = os.path.join(directory, year, month)
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Move the file to the new folder
    new_filepath = os.path.join(folder, os.path.basename(filepath))
    os.rename(filepath, new_filepath)
