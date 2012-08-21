#import flask
#import database
#import flaskext.script
#import os.path

default_config = {"DATABASE_URI": "postgresql://localhost/flis",
                }

def create_app(instance_path=None):
    instance_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                'instance'))
    app = flask.Flask(__name__,
                      instance_path=instance_path,
                      instance_relative_config=True)
    app.config.update(default_config)
    app.config.from_pyfile("settings.py", silent=True)
    database.initialize_app(app)
    return app

manager = flaskext.script.Manager(create_app)

if __name__ == '__main__':
    manager.run()

