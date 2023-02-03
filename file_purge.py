import os

directory = '/path/to/directory' # Replace with the path to the desired directory

for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
