import flask
import flatland.out.markup
import schema
import database

lists = flask.Blueprint('lists', __name__)

@lists.route('/')
def home():
    return flask.render_template('layout.html', **{
        'content': "Hello world!"
    })

@lists.route('/sources/new/', methods=['GET', 'POST'])
@lists.route('/sources/<int:source_id>/edit', methods=['GET', 'POST'])
def source_edit(source_id=None):
    app = flask.current_app
    session = database.session

    if source_id is None:
        sources_row = None
    else:
        sources_row = database.get_or_404("sources", source_id)
        source_schema = schema.SourcesSchema.from_flat(sources_row)

    if flask.request.method == "POST":
        form_data = dict(schema.SourcesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        source_schema = schema.SourcesSchema.from_flat(form_data)

        if source_schema.validate():
            if sources_row is None:
                sources_row = session['sources'].new()
            sources_row.update(source_schema.flatten())

            session.save(sources_row)
            session.commit()

            flask.flash("Source saved", "success")
            location = flask.url_for("lists.source_view", source_id=sources_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u"Errors in sources information", "error")
    else:
        if source_id:
            source_schema = schema.SourcesSchema.from_flat(sources_row)
        else:
            source_schema = schema.SourcesSchema()

    return flask.render_template('source_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'source_schema': source_schema,
        'source_id': source_id,
    })

@lists.route("/sources/<int:source_id>/")
def source_view(source_id):
    app = flask.current_app
    sources_row = database.get_or_404("sources", source_id)
    source = schema.SourcesSchema.from_flat(sources_row)
    return flask.render_template('source_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'source': source,
        'source_id': source_id,
    })

@lists.route("/sources/<int:source_id>/delete", methods=["POST"])
def source_delete(source_id):
    #sources_row = database.get_or_404("sources", source_id)

    session = database.session
    session['sources'].delete(source_id)
    session.commit()
    return flask.redirect(flask.url_for("lists.sources_view"))

@lists.route("/sources/")
def sources_view():
    sources_rows = database.get_all("sources")
    sources = [schema.Source.from_flat(sources_row)
        for sources_row in sources_rows]
    return flask.render_template('sources_view.html', **{
        'sources': sources,
    })

class MarkupGenerator(flatland.out.markup.Generator):

    def __init__(self, template):
        super(MarkupGenerator, self).__init__('html')
        self.template = template

    def children_order(self, field):
        if isinstance(field, flatland.Mapping):
            return [kid.name for kid in field.field_schema]
        else:
            return []

    def widget(self, element):
        widget_name = element.properties.get('widget', 'input')
        widget_macro = getattr(self.template.module, widget_name)
        return widget_macro(self, element)