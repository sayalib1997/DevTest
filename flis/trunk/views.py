import flask
import flatland.out.markup
import schema
import database

flis = flask.Blueprint('flis', __name__)

@flis.route('/')
def home():
    return flask.render_template('interlinks.html')

@flis.route('/gmts/new/', methods=['GET', 'POST'])
@flis.route('/gmts/<int:gmt_id>/edit', methods=['GET', 'POST'])
def gmt_edit(gmt_id=None):
    app = flask.current_app
    session = database.session

    if gmt_id is None:
        gmts_row = None
    else:
        gmts_row = database.get_or_404("gmts", gmt_id)
        gmt_schema = schema.GMT.from_flat(gmts_row)

    if flask.request.method == "POST":
        form_data = dict(schema.GMTsSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        gmt_schema = schema.GMTsSchema.from_flat(form_data)

        if gmt_schema.validate():
            if gmts_row is None:
                gmts_row = session['gmts'].new()
            gmts_row.update(gmt_schema.flatten())

            session.save(gmts_row)
            session.commit()

            flask.flash("GMT saved", "success")
            location = flask.url_for("flis.gmt_view", gmt_id=gmts_row.id)
            return flask.redirect(location)
        else:
            flask.flash(u"Errors in GMT information", "error")
    else:
        if gmt_id:
            gmt_schema = schema.GMTsSchema.from_flat(gmts_row)
        else:
            gmt_schema = schema.GMTsSchema()

    return flask.render_template('gmt_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'gmt_schema': gmt_schema,
        'gmt_id': gmt_id,
    })

@flis.route('/gmts/<int:gmt_id>/')
def gmt_view(gmt_id):
    app = flask.current_app
    gmts_row = database.get_or_404("gmts", gmt_id)
    gmt = schema.GMTsSchema.from_flat(gmts_row)
    return flask.render_template('gmt_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'gmt': gmt,
        'gmt_id': gmt_id,
    })

@flis.route('/gmts/<int:gmt_id>/delete', methods=["POST"])
def gmt_delete(gmt_id):
    session = database.session
    session['gmts'].delete(gmt_id)
    session.commit()
    return flask.redirect(flask.url_for("flis.gmts_listing"))

@flis.route('/gmts/')
def gmts_listing():
    gmts_rows = database.get_all("gmts")
    gmts = [schema.GMT.from_flat(gmts_row)
        for gmts_row in gmts_rows]
    return flask.render_template('gmts_listing.html', **{
        'gmts': gmts,
    })


lists = flask.Blueprint('lists', __name__)

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

@lists.route('/trends/new/', methods=['GET', 'POST'])
@lists.route('/trends/<int:trend_id>/edit', methods=['GET', 'POST'])
def trend_edit(trend_id=None):
    app = flask.current_app
    session = database.session

    if trend_id is None:
        trends_row = None
    else:
        trends_row = database.get_or_404("trends", trend_id)
        trend_schema = schema.TrendsSchema.from_flat(trends_row)

    if flask.request.method == "POST":
        form_data = dict(schema.TrendsSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        trend_schema = schema.TrendsSchema.from_flat(form_data)

        if trend_schema.validate():
            if trends_row is None:
                trends_row = session['trends'].new()
            trends_row.update(trend_schema.flatten())

            session.save(trends_row)
            session.commit()

            flask.flash("Trend saved", "success")
            location = flask.url_for("lists.trend_view", trend_id=trends_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u"Errors in trends information", "error")
    else:
        if trend_id:
            trend_schema = schema.TrendsSchema.from_flat(trends_row)
        else:
            trend_schema = schema.TrendsSchema()

    return flask.render_template('trend_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'trend_schema': trend_schema,
        'trend_id': trend_id,
    })

@lists.route("/trends/<int:trend_id>/")
def trend_view(trend_id):
    app = flask.current_app
    trends_row = database.get_or_404("trends", trend_id)
    trend = schema.TrendsSchema.from_flat(trends_row)
    return flask.render_template('trend_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'trend': trend,
        'trend_id': trend_id,
    })

@lists.route("/trends/<int:trend_id>/delete", methods=["POST"])
def trend_delete(trend_id):
    #trends_row = database.get_or_404("trends", trend_id)

    session = database.session
    session['trends'].delete(trend_id)
    session.commit()
    return flask.redirect(flask.url_for("lists.trends_view"))

@lists.route("/trends/")
def trends_view():
    trends_rows = database.get_all("trends")
    trends = [schema.Trend.from_flat(trends_row)
        for trends_row in trends_rows]
    return flask.render_template('trends_view.html', **{
        'trends': trends,
    })

@lists.route('/thematic_categories/new/', methods=['GET', 'POST'])
@lists.route('/thematic_categories/<int:thematic_category_id>/edit',
        methods=['GET', 'POST'])
def thematic_category_edit(thematic_category_id=None):
    app = flask.current_app
    session = database.session

    if thematic_category_id is None:
        thematic_categories_row = None
    else:
        thematic_categories_row = database.get_or_404("thematic_categories",
                thematic_category_id)
        thematic_category_schema = schema.ThematicCategoriesSchema.from_flat(
                thematic_categories_row)

    if flask.request.method == "POST":
        form_data = dict(schema.ThematicCategoriesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        thematic_category_schema = schema.ThematicCategoriesSchema.from_flat(
                form_data)

        if thematic_category_schema.validate():
            if thematic_categories_row is None:
                thematic_categories_row = session['thematic_categories'].new()
            thematic_categories_row.update(thematic_category_schema.flatten())

            session.save(thematic_categories_row)
            session.commit()

            flask.flash("Category saved", "success")
            location = flask.url_for("lists.thematic_category_view",
                    thematic_category_id=thematic_categories_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u"Errors in trends information", "error")
    else:
        if thematic_category_id:
            thematic_category_schema = schema.ThematicCategoriesSchema.from_flat(
                    thematic_categories_row)
        else:
            thematic_category_schema = schema.ThematicCategoriesSchema()

    return flask.render_template('thematic_category_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'thematic_category_schema': thematic_category_schema,
        'thematic_category_id': thematic_category_id,
    })

@lists.route("/thematic_categories/<int:thematic_category_id>/")
def thematic_category_view(thematic_category_id):
    app = flask.current_app
    thematic_categories_row = database.get_or_404("thematic_categories",
            thematic_category_id)
    thematic_category = schema.ThematicCategoriesSchema.from_flat(
            thematic_categories_row)
    return flask.render_template('thematic_category_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'thematic_category': thematic_category,
        'thematic_category_id': thematic_category_id,
    })

@lists.route("/thematic_categories/<int:thematic_category_id>/delete",
        methods=["POST"])
def thematic_category_delete(thematic_category_id):
    session = database.session
    session['thematic_categories'].delete(thematic_category_id)
    session.commit()
    return flask.redirect(flask.url_for("lists.thematic_categories_view"))

@lists.route("/thematic_categories/")
def thematic_categories_view():
    thematic_categories_rows = database.get_all("thematic_categories")
    thematic_categories = [
            schema.ThematicCategory.from_flat(thematic_categories_row)
            for thematic_categories_row in thematic_categories_rows]
    return flask.render_template('thematic_categories_view.html', **{
        'thematic_categories': thematic_categories,
    })

@lists.route('/geographical_scales/new/', methods=['GET', 'POST'])
@lists.route('/geographical_scales/<int:geographical_scale_id>/edit',
        methods=['GET', 'POST'])
def geographical_scale_edit(geographical_scale_id=None):
    app = flask.current_app
    session = database.session

    if geographical_scale_id is None:
        geographical_scales_row = None
    else:
        geographical_scales_row = database.get_or_404("geographical_scale",
                geographical_scale_id)
        geographical_scale_schema = schema.GeographicalScalesSchema.from_flat(
                geographical_scales_row)

    if flask.request.method == "POST":
        form_data = dict(schema.GeographicalScalesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        geographical_scale_schema = schema.GeographicalScalesSchema.from_flat(
                form_data)

        if geographical_scale_schema.validate():
            if geographical_scales_row is None:
                geographical_scales_row = session['geographical_scales'].new()
            geographical_scales_row.update(geographical_scale_schema.flatten())

            session.save(geographical_scales_row)
            session.commit()

            flask.flash("Geographical scale saved", "success")
            location = flask.url_for("lists.geographical_scale_view",
                    geographical_scale_id=geographical_scales_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u"Errors in trends information", "error")
    else:
        if geographical_scale_id:
            geographical_scale_schema = schema.GeographicalScalesSchema.from_flat(
                    geographical_scales_row)
        else:
            geographical_scale_schema = schema.GeographicalScalesSchema()

    return flask.render_template('geographical_scale_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'geographical_scale_schema': geographical_scale_schema,
        'geographical_scale_id': geographical_scale_id,
    })

@lists.route("/geographical_scales/<int:geographical_scale_id>/")
def geographical_scale_view(geographical_scale_id):
    app = flask.current_app
    geographical_scales_row = database.get_or_404("geographical_scales",
            geographical_scale_id)
    geographical_scale = schema.GeographicalScalesSchema.from_flat(
            geographical_scales_row)
    return flask.render_template('geographical_scale_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'geographical_scale': geographical_scale,
        'geographical_scale_id': geographical_scale_id,
    })

@lists.route("/geographical_scales/<int:geographical_scale_id>/delete",
        methods=["POST"])
def geographical_scale_delete(geographical_scale_id):
    session = database.session
    session['geographical_scales'].delete(geographical_scale_id)
    session.commit()
    return flask.redirect(flask.url_for("lists.geographical_scales_view"))

@lists.route("/geographical_scales/")
def geographical_scales_view():
    geographical_scales_rows = database.get_all("geographical_scales")
    geographical_scales = [
            schema.GeographicalScale.from_flat(geographical_scales_row)
            for geographical_scales_row in geographical_scales_rows]
    return flask.render_template('geographical_scales_view.html', **{
        'geographical_scales': geographical_scales,
    })

@lists.route('/geographical_coverages/new/', methods=['GET', 'POST'])
@lists.route('/geographical_coverages/<int:geographical_coverage_id>/edit',
        methods=['GET', 'POST'])
def geographical_coverage_edit(geographical_coverage_id=None):
    app = flask.current_app
    session = database.session

    if geographical_coverage_id is None:
        geographical_coverages_row = None
    else:
        geographical_coverages_row = database.get_or_404("geographical_coverages",
                geographical_coverage_id)
        geographical_coverage_schema = schema.GeographicalCoveragesSchema.from_flat(
                geographical_coverages_row)

    if flask.request.method == "POST":
        form_data = dict(schema.GeographicalCoveragesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        geographical_coverage_schema = schema.GeographicalCoveragesSchema.from_flat(
                form_data)

        if geographical_coverage_schema.validate():
            if geographical_coverages_row is None:
                geographical_coverages_row = session['geographical_coverages'].new()
            geographical_coverages_row.update(geographical_coverage_schema.flatten())

            session.save(geographical_coverages_row)
            session.commit()

            flask.flash("Geographical coverage saved", "success")
            location = flask.url_for("lists.geographical_coverage_view",
                    geographical_coverage_id=geographical_coverages_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u"Errors in trends information", "error")
    else:
        if geographical_coverage_id:
            geographical_coverage_schema = schema.GeographicalCoveragesSchema.from_flat(
                    geographical_coverages_row)
        else:
            geographical_coverage_schema = schema.GeographicalCoveragesSchema()

    return flask.render_template('geographical_coverage_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'geographical_coverage_schema': geographical_coverage_schema,
        'geographical_coverage_id': geographical_coverage_id,
    })

@lists.route("/geographical_coverages/<int:geographical_coverage_id>/")
def geographical_coverage_view(geographical_coverage_id):
    app = flask.current_app
    geographical_coverages_row = database.get_or_404("geographical_coverages",
            geographical_coverage_id)
    geographical_coverage = schema.GeographicalCoveragesSchema.from_flat(
            geographical_coverages_row)
    return flask.render_template('geographical_coverage_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'geographical_coverage': geographical_coverage,
        'geographical_coverage_id': geographical_coverage_id,
    })

@lists.route("/geographical_coverages/<int:geographical_coverage_id>/delete",
        methods=["POST"])
def geographical_coverage_delete(geographical_coverage_id):
    session = database.session
    session['geographical_coverages'].delete(geographical_coverage_id)
    session.commit()
    return flask.redirect(flask.url_for("lists.geographical_coverages_view"))

@lists.route("/geographical_coverages/")
def geographical_coverages_view():
    geographical_coverages_rows = database.get_all("geographical_coverages")
    geographical_coverages = [
            schema.GeographicalCoverage.from_flat(geographical_coverages_row)
            for geographical_coverages_row in geographical_coverages_rows]
    return flask.render_template('geographical_coverages_view.html', **{
        'geographical_coverages': geographical_coverages,
    })

@lists.route('/steep_categories/new/', methods=['GET', 'POST'])
@lists.route('/steep_categories/<int:steep_category_id>/edit',
        methods=['GET', 'POST'])
def steep_category_edit(steep_category_id=None):
    app = flask.current_app
    session = database.session

    if steep_category_id is None:
        steep_categories_row = None
    else:
        steep_categories_row = database.get_or_404("steep_categories",
                steep_category_id)
        steep_category_schema = schema.SteepCategoriesSchema.from_flat(
                steep_categories_row)

    if flask.request.method == "POST":
        form_data = dict(schema.SteepCategoriesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        steep_category_schema = schema.SteepCategoriesSchema.from_flat(
                form_data)

        if steep_category_schema.validate():
            if steep_categories_row is None:
                steep_categories_row = session['steep_categories'].new()
            steep_categories_row.update(steep_category_schema.flatten())

            session.save(steep_categories_row)
            session.commit()

            flask.flash("Geographical coverage saved", "success")
            location = flask.url_for("lists.steep_category_view",
                    steep_category_id=steep_categories_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u"Errors in trends information", "error")
    else:
        if steep_category_id:
            steep_category_schema = schema.SteepCategoriesSchema.from_flat(
                    steep_categories_row)
        else:
            steep_category_schema = schema.SteepCategoriesSchema()

    return flask.render_template('steep_category_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'steep_category_schema': steep_category_schema,
        'steep_category_id': steep_category_id,
    })

@lists.route("/steep_categories/<int:steep_category_id>/")
def steep_category_view(steep_category_id):
    app = flask.current_app
    steep_categories_row = database.get_or_404("steep_categories",
            steep_category_id)
    steep_category = schema.SteepCategoriesSchema.from_flat(
            steep_categories_row)
    return flask.render_template('steep_category_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'steep_category': steep_category,
        'steep_category_id': steep_category_id,
    })

@lists.route("/steep_categories/<int:steep_category_id>/delete",
        methods=["POST"])
def steep_category_delete(steep_category_id):
    session = database.session
    session['steep_categories'].delete(steep_category_id)
    session.commit()
    return flask.redirect(flask.url_for("lists.steep_categories_listing"))

@lists.route("/steep_categories/")
def steep_categories_listing():
    steep_categories_rows = database.get_all("steep_categories")
    steep_categories = [
            schema.GeographicalCoverage.from_flat(steep_categories_row)
            for steep_categories_row in steep_categories_rows]
    return flask.render_template('steep_categories_listing.html', **{
        'steep_categories': steep_categories,
    })

@lists.route('/timelines/new/', methods=['GET', 'POST'])
@lists.route('/timelines/<int:timeline_id>/edit', methods=['GET', 'POST'])
def timeline_edit(timeline_id=None):
    app = flask.current_app
    session = database.session

    if timeline_id is None:
        timelines_row = None
    else:
        timelines_row = database.get_or_404("timelines", timeline_id)
        timeline_schema = schema.TimelinesSchema.from_flat(timelines_row)

    if flask.request.method == "POST":
        form_data = dict(schema.TimelinesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        timeline_schema = schema.TimelinesSchema.from_flat(form_data)

        if timeline_schema.validate():
            if timelines_row is None:
                timelines_row = session['timelines'].new()
            timelines_row.update(timeline_schema.flatten())

            session.save(timelines_row)
            session.commit()

            flask.flash("Timeline saved", "success")
            location = flask.url_for("lists.timeline_view",
                                     timeline_id=timelines_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u"Errors in timeline information", "error")
    else:
        if timeline_id:
            timeline_schema = schema.TimelinesSchema.from_flat(
                timelines_row)
        else:
            timeline_schema = schema.TimelinesSchema()

    return flask.render_template('timeline_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'timeline_schema': timeline_schema,
        'timeline_id': timeline_id,
    })

@lists.route("/timelines/<int:timeline_id>/")
def timeline_view(timeline_id):
    app = flask.current_app
    timelines_row = database.get_or_404("timelines", timeline_id)
    timeline = schema.TimelinesSchema.from_flat(timelines_row)
    return flask.render_template('timeline_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'timeline': timeline,
        'timeline_id': timeline_id,
    })

@lists.route("/timelines/<int:timeline_id>/delete", methods=["POST"])
def timeline_delete(timeline_id):
    session = database.session
    session['timelines'].delete(timeline_id)
    session.commit()
    return flask.redirect(flask.url_for("lists.timelines_listing"))

@lists.route("/timelines/")
def timelines_listing():
    timelines_rows = database.get_all("timelines")
    timelines = [
        schema.Timeline.from_flat(timelines_row)
        for timelines_row in timelines_rows]
    return flask.render_template('timelines_listing.html', **{
        'timelines': timelines
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
