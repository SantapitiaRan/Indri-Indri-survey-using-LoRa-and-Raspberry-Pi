import os

# Specify the directory path you want to list
directory_path = '/home/santapitia/Desktop/audio-compare-master/Territory marking/'

# List all files in the directory
files = os.listdir(directory_path)

# Filter out directories (if any) and keep only files
files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]

# Sort files by their modification time (most recent first)
files.sort(key=lambda x: os.path.getmtime(os.path.join(directory_path, x)), reverse=True)

if files:
    # Get the most recent file
    most_recent_file = files[0]
    print("Most recent file:", most_recent_file)
else:
    print("No files found in the directory.")

