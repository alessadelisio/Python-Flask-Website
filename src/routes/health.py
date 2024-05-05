from flask import Blueprint

router = Blueprint("health", __name__)

@router.route("/health", methods=["GET"])
def health() -> dict:
    """
    Health endpoint to check if the service
    is up and running.
    """

    return {"status": "ok"}
