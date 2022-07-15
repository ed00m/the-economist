"""
the-economist - Project X_periment.

Python3.x
"""

import flask
from flask_cors import CORS, cross_origin
from tools import Tools

# enable services with Blueprints
import services.origins as origins
import services.alive as alive
import services.scripts as scripts
import services.root as root
import services.indecon as indecon
import services.abacus as abacus
import services.profiles as profiles


logger = Tools().debujer

app = flask.Flask(__name__)
cors = CORS(app)

app.register_blueprint(root.bp)
app.register_blueprint(alive.bp)
app.register_blueprint(origins.bp)
app.register_blueprint(scripts.bp)
app.register_blueprint(indecon.bp)
app.register_blueprint(abacus.bp)
app.register_blueprint(profiles.bp)

logger(app.config)

app.run(host='0.0.0.0', port=3000)
