# Step 2
# this function should inspect 'data' folder and return list of paths to cpp files
import os

def get_cpps_list (data_address):
    cpp_files = []

    for root, dirs, files in os.walk(data_address):
        for file in files:
            if file.endswith(".cc") or file.endswith(".cpp"):
                cpp_files.append(str(os.path.join(root, file)))

    return cpp_files