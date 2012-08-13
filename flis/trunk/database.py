from path import path
from werkzeug.local import LocalProxy
from flask_htables import HTables


_tables = ['message']

htables_ext = HTables()

session = LocalProxy(lambda: htables_ext.session)


def initialize_app(app):
    app.config.setdefault('HTABLES_SQLITE_PATH',
                          path(app.instance_path) / 'db.sqlite')
    htables_ext.initialize_app(app)
    app.register_blueprint(htables_ext.admin, url_prefix='/htables')

    with app.test_request_context():
        for name in _tables:
            session[name].create_table()
