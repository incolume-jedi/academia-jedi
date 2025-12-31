""" "Module."""

import zipfile
from io import BytesIO

from icecream import ic


def main():
    ic('Hello from ajedi20251206-zipfile!')

    # Assuming you have a ZIP file, either on disk or as bytes in memory
    # For demonstration, let's create a dummy in-memory zip file
    # In a real scenario, you'd open an existing zip file from a path
    # or from a BytesIO object if you received it over a network, for example.

    # Create a dummy in-memory zip file for demonstration
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf_out:
        zf_out.writestr('my_file.txt', b'This is the content of my file.')
        zf_out.writestr('another_file.bin', b'\x01\x02\x03\x04')

    # Now, read from the in-memory zip file
    zip_buffer.seek(0)  # Rewind the buffer to the beginning

    with zipfile.ZipFile(zip_buffer, 'r') as zf_in:
        # Get the list of files in the archive
        file_names = zf_in.namelist()
        ic(f'Files in zip: {file_names}')

        # Read a specific file without extracting
        file_to_read = 'my_file.txt'
        if file_to_read in file_names:
            with zf_in.open(file_to_read, 'r') as file_in_zip:
                # Read the content of the file into a BytesIO object
                file_content_bytes = file_in_zip.read()
                in_memory_file = BytesIO(file_content_bytes)

                # Now you can work with in_memory_file as a file-like object
                ic(
                    f"Content of '{file_to_read}': {in_memory_file.read().decode('utf-8')}",
                )
        else:
            ic(f"File '{file_to_read}' not found in the archive.")

        # Example for a binary file
        file_to_read_bin = 'another_file.bin'
        if file_to_read_bin in file_names:
            with zf_in.open(file_to_read_bin, 'r') as file_in_zip:
                binary_content = file_in_zip.read()
                in_memory_binary_file = BytesIO(binary_content)
                ic(
                    f"Binary content of '{file_to_read_bin}': {in_memory_binary_file.read()}",
                )


if __name__ == '__main__':
    main()
