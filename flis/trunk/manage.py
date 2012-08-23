import flask
import database
import flaskext.script
from path import path
from werkzeug import SharedDataMiddleware
import views

default_config = {
        'HTABLES_ENGINE': 'sqlite',
    }

def create_app():
    instance_path = path(__file__).abspath().parent/'instance'
    app = flask.Flask(__name__,
                      instance_path=instance_path,
                      instance_relative_config=True)
    app.config.update(default_config)
    app.config.from_pyfile("settings.py", silent=True)
    app.register_blueprint(views.lists)
    app.register_blueprint(views.flis)
    _my_extensions = app.jinja_options["extensions"] + ["jinja2.ext.do"]
    app.jinja_options = dict(app.jinja_options, extensions=_my_extensions)
    database.initialize_app(app)
    if app.config['DEBUG']:
        files_path = path(app.root_path)
        files_path = flask.safe_join(files_path, "instance/files")
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            "/static/files": files_path,
        })
    return app

manager = flaskext.script.Manager(create_app)

if __name__ == '__main__':
    manager.run()
