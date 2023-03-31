## Open all Google Docs in a folder from Drive synced to local machine

import os
import webbrowser
import sys

# Specify the folder ID of the folder containing the Google Docs
FOLDER_ID = sys.argv[1]

# Specify the path to the folder containing the Google Docs
folder_path = "G:/My Drive/" + FOLDER_ID

# Check if the folder exists
if not os.path.isdir(folder_path):
    print("Error: Google Drive folder not found at", folder_path)
    exit()

# Open all Google Docs files in the folder in the default browser
for file in os.listdir(folder_path):
    if file.endswith(".gdoc"):
        file_path = folder_path + "/" + file
        webbrowser.open(file_path)
