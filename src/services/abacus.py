"""
the-economist - Project X_periment.

Python3.x
"""

import time
from flask import jsonify, Blueprint
from factory.abacus import Abacus

time_init = time.time()
name = "abacus"

bp = Blueprint(
    name=name,
    import_name=__name__,
    url_prefix="/abacus"
)


@bp.route("/")
def index_page():
    """Index page template."""
    response = Abacus(name).index_page()
    response["time"] = (time.time() - time_init)
    return jsonify(response)


@bp.route("/date/<string:key>/<string:date>")
def date_page(key, date):
    """Date page template."""
    response = Abacus(name).date_page(key, date)
    response["time"] = (time.time() - time_init)
    return jsonify(response)


@bp.route("/last")
def last_page():
    """Last page template."""
    response = Abacus(name).last_page()
    response["time"] = (time.time() - time_init)
    return jsonify(response)


@bp.route("/values/<string:key>")
def values_page(key):
    """Values page template."""
    response = Abacus(name).values_page(key)
    response["time"] = (time.time() - time_init)
    return jsonify(response)


@bp.route("/statistics/element/<string:key>")
def statistics_element(key):
    """Statistics element page template."""
    response = Abacus(name).statistics_element(key)
    response["time"] = (time.time() - time_init)
    return jsonify(response)
