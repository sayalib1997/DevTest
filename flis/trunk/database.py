import flask
from path import path
from werkzeug.local import LocalProxy
from flask_htables import HTables


_tables = ['sources', 'trends', 'thematic_categories', 'geographical_scales',
            'geographical_coverages', 'steep_categories', 'timelines', 'gmts',
            'indicators']

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

def get_or_404(name, row_id):
    table = session[name]
    try:
        return table.get(row_id)
    except table.RowNotFound:
        flask.abort(404)

def get_all(name):
    table = session[name]
    return table.get_all()
