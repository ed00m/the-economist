import flask
from tools import Tools

# enable services with Blueprints
import services.origins as origins
import services.alive as alive
import services.scripts as scripts
import services.root as root


logger = Tools().debujer

app = flask.Flask(__name__)
app.register_blueprint(root.bp)
app.register_blueprint(alive.bp)
app.register_blueprint(origins.bp)
app.register_blueprint(scripts.bp)

logger(app.config)

app.run(host='0.0.0.0', port=3000)
