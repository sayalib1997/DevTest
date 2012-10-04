import flask
import jinja2
import database
import flaskext.script
from path import path
from werkzeug import SharedDataMiddleware
import views
from raven.contrib.flask import Sentry
import frame

default_config = {
        'HTABLES_ENGINE': 'sqlite',
        'HTTP_PROXIED': False,
        'FRAME_URL': None,
    }

sentry = Sentry()

def create_app():
    instance_path = path(__file__).abspath().parent/'instance'
    app = flask.Flask(__name__,
                      instance_path=instance_path,
                      instance_relative_config=True)
    app.config.update(default_config)
    app.config.from_pyfile("settings.py", silent=True)

    sentry.init_app(app)

    app.register_blueprint(views.lists)
    app.register_blueprint(views.flis)
    _my_extensions = app.jinja_options["extensions"] + ["jinja2.ext.do"]
    template_loader = jinja2.ChoiceLoader([
        frame.FrameTemplateLoader(),
        app.create_global_jinja_loader(),
    ])
    app.jinja_options = dict(app.jinja_options,
                             extensions=_my_extensions,
                             loader=template_loader)
    database.initialize_app(app)
    if app.config['DEBUG']:
        files_path = path(app.root_path)
        files_path = flask.safe_join(files_path, "instance/files")
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            "/static/files": files_path,
        })
    if app.config["HTTP_PROXIED"]:
        from revproxy import ReverseProxied
        app.wsgi_app = ReverseProxied(app.wsgi_app)
    return app

manager = flaskext.script.Manager(create_app)

if __name__ == '__main__':
    manager.run()
