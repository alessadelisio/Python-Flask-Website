import csv
import zipfile

from werkzeug.datastructures import FileStorage


def files_to_dict(csv_file: FileStorage) -> dict:
    """
    This function converts a CSV file data to a dictionary.

    Args:
    - csv_file (FileStorage): The CSV file stored in a 
    FileStorage object.

    Returns:
    - csv_dict (dict): A dictionary containing data from 
    the CSV file.

    Raises:
    - Exception: If an error occurs.
    """

    csv_dict = {}

    try:
        csv_stream = csv_file.stream
        csv_reader = csv.reader(csv_stream, delimiter=";")
    
        next(csv_reader)
    
    except Exception as e:
        raise Exception("Error: `csv_file` could not be read.") from e
    
    for row in csv_reader:
        # Asumir que la columna 1 es la key y la columna 2 es el value
        key = row[0]
        value = row[1]

        # Añadir los key-value al diccionario
        csv_dict[key] = value

    return csv_dict


def unzip_files(zip_file: FileStorage) -> list:
    """
    This function processes the content of a ZIP object.
    
    Args:
    - zip_file (FileStorage): The ZIP file stored in a 
    FileStorage object.
    
    Returns:
    - zip_list_files (list): A list of all the files
    within the ZIP object.

    Raises:
    - Exception: If an error occurs.
    """

    zip_list_files = []

    try:
        with zipfile.ZipFile(zip_file.stream, mode='r') as my_zip:
            zip_list_files = my_zip.namelist()
    
    except Exception as e:
        raise Exception("Error: `zip_file` could not be read.") from e

    return zip_list_files


def validate_files_exists(zip_list: list, csv_dict: dict) -> bool:
    """
    This function validates the information in
    a CVS file againts the content of a folder.

    Args:
    - zip_list (list): A list of files within a ZIP
    object.
    - csv_dict (dict): A dictionary containing data from 
    the CSV file.

    Returns:
    - True: If all files within the ZIP object are in
    the `csv_dict`.
    - False: If only one file within the ZIP object is
    not in the `csv_dict`.
    """

    for file in zip_list:
        if file in csv_dict.keys():
            print("file exists")
        else:
            print("file not exist")
