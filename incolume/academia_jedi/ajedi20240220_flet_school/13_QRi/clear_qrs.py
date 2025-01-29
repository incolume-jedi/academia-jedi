"""Clear qrs."""

import logging
import os
from pathlib import Path


def clear_qr_codes():
    """Clear."""
    folder_path = 'assets/qr'
    # Check if the folder exists
    if Path.exists(folder_path):
        # Get a list of all files in the folder
        files_in_folder = os.listdir(folder_path)

        # Iterate through the files and delete them
        for file in files_in_folder:
            file_path = os.path.join(folder_path, file)
            try:
                if Path(file_path).is_file():
                    Path(file_path)
            except Exception:
                logging.exception('Exception occurred')
    else:
        pass
