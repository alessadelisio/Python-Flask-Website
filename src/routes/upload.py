from flask import Blueprint, jsonify, request

from src.services.service import files_to_dict, unzip_files, validate_files_exists

router = Blueprint("upload", __name__)


@router.route("/upload", methods=["POST"])
def upload_file() -> jsonify:
    """
    This function XXX.

    Args:
    - xxxx

    Returns:
    - xxxx


    Raises:
    - Exception: If an error occurs.
    """

    zip_folder = request.files["zipFile"]
    csv_file_handler = request.files["csvFile"]

    my_list = unzip_files(zip_folder)
    my_dict = files_to_dict(csv_file_handler)

    result = validate_files_exists(my_list, my_dict)

    return jsonify(result)
