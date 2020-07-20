"""
the-economist - Project X_periment.

Python3.x
"""

import time
from flask import jsonify, Blueprint
from factory.profiles import Profiles

time_init = time.time()
name = "profiles"

bp = Blueprint(
    name=name,
    import_name=__name__,
    url_prefix="/profiles"
)


@bp.route("/")
def index_page():
    """Index page template."""
    response = Profiles(name).index_page()
    response["time"] = (time.time() - time_init)
    return jsonify(response)


# @bp.route("/statistics/element/<string:key>")
# def statistics_element(key):
#     """Statistics element page template."""
#     response = Profiles(name).statistics_element(key)
#     response["time"] = (time.time() - time_init)
#     return jsonify(response)
