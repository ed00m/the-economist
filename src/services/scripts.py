from flask import jsonify, Blueprint
import subprocess


bp = Blueprint(
    name='scripts',
    import_name=__name__,
    url_prefix="/scripts"
)

response = {"OK": True}


@bp.route("/")
def index_page():
    response["data"] = "This is a root from scripts"
    return jsonify(response)


@bp.route('/date/<string:when>')
def date(when):

    if when == "today":
        format = "+%Y%m%d"
    else:
        format = "+%Y%m%d_%H%M%S"

    process = subprocess.Popen(
        ["date", format],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()

    response["stdout"] = str(stdout)
    response["stderr"] = str(stderr)

    return jsonify(response)
