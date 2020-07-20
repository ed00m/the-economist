"""
the-economist - Project X_periment.

Python3.x
"""

from flask import jsonify, Blueprint


bp = Blueprint(
    name='root',
    import_name=__name__,
    url_prefix="/"
)

response = {"OK": True}


@bp.route("/")
def index_page():
    """Index page template."""
    response["data"] = "This is a root from {}".format(bp.name)
    return jsonify(response)


@bp.route("/health")
def health_page():
    """Health page template."""
    response["data"] = "This is a /health from {}".format(bp.name)
    return jsonify(response)
