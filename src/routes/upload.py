from flask import Blueprint, request
from src.services.service import (
    files_to_dict,
    unzip_files,
    validate_files_exists
)

router = Blueprint("upload", __name__)

@router.route("/upload", methods=["POST"])
def upload_file():
    # Corrige cómo se acceden a los archivos subidos
    zip_folder = request.files['zipFile']
    csv_file_handler = request.files['csvFile']

    # Usa las funciones de servicio adecuadamente
    my_list = unzip_files(zip_folder)
    my_dict = files_to_dict(csv_file_handler)

    validate_files_exists(my_list, my_dict)
    return "Archivos subidos y procesados correctamente", 200