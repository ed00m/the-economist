"""
the-economist - Project X_periment.

Python3.x
"""

import time
from flask import jsonify, Blueprint
from factory.indecon import Indecon

time_init = time.time()
name = "indecon"

bp = Blueprint(
    name=name,
    import_name=__name__,
    url_prefix="/indecon"
)


@bp.route("/")
def index_page():
    """Index page template."""
    response = Indecon(name).index_page()
    response["time"] = (time.time() - time_init)
    return jsonify(response)


@bp.route("/date/<string:key>/<string:date>")
def date_page(key, date):
    """Date page template."""
    response = Indecon(name).date_page(key, date)
    response["time"] = (time.time() - time_init)
    return jsonify(response)


@bp.route("/last")
def last_page():
    """Last page template."""
    response = Indecon(name).last_page()
    response["time"] = (time.time() - time_init)
    return jsonify(response)


@bp.route("/values/<string:key>")
def values_page(key):
    """Values page template."""
    response = Indecon(name).values_page(key)
    response["time"] = (time.time() - time_init)
    return jsonify(response)
