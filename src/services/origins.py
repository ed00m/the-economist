from flask import jsonify, Blueprint


bp = Blueprint(
    name='origins',
    import_name=__name__,
    url_prefix="/origins"
)

response = {"OK": True}


@bp.route("/")
def index_page():
    response["data"] = "This is a root from {}".format(bp.name)
    return jsonify(response)


@bp.route("/about")
def about_page():
    response["data"] = "This is a about from {}".format(bp.name)
    return jsonify(response)


@bp.route("/hello/<string:hello>")
def hello_page(hello):
    response["data"] = "This is a greeting to " + hello + " from {}".\
        format(bp.name)
    return jsonify(response)
