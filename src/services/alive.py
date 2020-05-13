from flask import jsonify, Blueprint


bp = Blueprint(
    name='alive',
    import_name=__name__,
    url_prefix="/alive"
)

response = {"OK": True}


@bp.route("/")
def index_page():
    response["data"] = "This is a root from {}".format(bp.name)
    return jsonify(response)


@bp.route("/health")
def health_page():
    response["data"] = "This is a health from {}".format(bp.name)
    return jsonify(response)
