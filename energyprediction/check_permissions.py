import os

def check_file_permissions(file_path):
    # Check if the file exists
    if os.path.exists(file_path):
        # Get the file permissions
        permissions = os.stat(file_path).st_mode

        # Check if the file is readable
        if os.access(file_path, os.R_OK):
            print(f"The file at '{file_path}' is readable.")
        else:
            print(f"The file at '{file_path}' is not readable.")

        # Check if the file is writable
        if os.access(file_path, os.W_OK):
            print(f"The file at '{file_path}' is writable.")
        else:
            print(f"The file at '{file_path}' is not writable.")

        # Check if the file is executable
        if os.access(file_path, os.X_OK):
            print(f"The file at '{file_path}' is executable.")
        else:
            print(f"The file at '{file_path}' is not executable.")
    else:
        print(f"The file at '{file_path}' does not exist.")

# Replace 'model.pkl' with the actual file name and path
file_path = r'C:\Users\User\Documents\Agile Data Science\energyconsumption\energyprediction\model.pkl'
check_file_permissions(file_path)