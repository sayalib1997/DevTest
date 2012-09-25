import flask
import flatland.out.markup
import schema
import database
import tempfile
from path import path

MByte = 1024*1024

flis = flask.Blueprint('flis', __name__)

@flis.route('/home')
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
        gmts_row = database.get_or_404('gmts', gmt_id)
        gmt_schema = schema.GMT.from_flat(gmts_row)

    if flask.request.method == 'POST':
        form_data = dict(schema.GMTsSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        gmt_schema = schema.GMTsSchema.from_flat(form_data)

        if gmt_schema.validate():
            if gmts_row is None:
                gmts_row = session['gmts'].new()
            gmts_row.update(gmt_schema.flatten())

            session.save(gmts_row)
            session.commit()

            flask.flash('GMT saved', 'success')
            location = flask.url_for('flis.gmt_view', gmt_id=gmts_row.id)
            return flask.redirect(location)
        else:
            flask.flash(u'Errors in GMT information', 'error')
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
    gmts_row = database.get_or_404('gmts', gmt_id)
    gmt = schema.GMTsSchema.from_flat(gmts_row)
    return flask.render_template('gmt_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'gmt': gmt,
        'gmt_id': gmt_id,
    })

@flis.route('/gmts/<int:gmt_id>/delete', methods=['POST'])
def gmt_delete(gmt_id):
    session = database.session
    session['gmts'].delete(gmt_id)
    session.commit()
    return flask.redirect(flask.url_for('flis.gmts_listing'))

@flis.route('/gmts/')
def gmts_listing():
    gmts_rows = database.get_all('gmts')
    gmts = [schema.GMT.from_flat(gmts_row)
        for gmts_row in gmts_rows]
    return flask.render_template('gmts_listing.html', **{
        'gmts': gmts,
    })

@flis.route('/interlinks/new/', methods=['GET', 'POST'])
@flis.route('/interlinks/<int:interlink_id>/edit', methods=['GET', 'POST'])
def interlink_edit(interlink_id=None):
    app = flask.current_app
    session = database.session

    if interlink_id is None:
        interlinks_row = None
    else:
        interlinks_row = database.get_or_404('interlinks', interlink_id)
        interlink_schema = schema.Interlink.from_flat(interlinks_row)

    if flask.request.method == 'POST':
        form_data = dict(schema.InterlinksSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        interlink_schema = schema.InterlinksSchema.from_flat(form_data)

        if interlink_schema.validate():
            if interlinks_row is None:
                interlinks_row = session['interlinks'].new()
            interlinks_row.update(interlink_schema.flatten())

            session.save(interlinks_row)
            session.commit()

            flask.flash('Interlink saved', 'success')
            location = flask.url_for('flis.interlink_view',
                    interlink_id=interlinks_row.id)
            return flask.redirect(location)
        else:
            flask.flash(u'Errors in Interlink information', 'error')
    else:
        if interlink_id:
            interlink_schema = schema.InterlinksSchema.from_flat(interlinks_row)
        else:
            interlink_schema = schema.InterlinksSchema()

    return flask.render_template('interlink_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'interlink_schema': interlink_schema,
        'interlink_id': interlink_id,
    })

@flis.route('/interlinks/<int:interlink_id>/')
def interlink_view(interlink_id):
    app = flask.current_app
    interlinks_row = database.get_or_404('interlinks', interlink_id)
    interlink = schema.InterlinksSchema.from_flat(interlinks_row)
    return flask.render_template('interlink_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'interlink': interlink,
        'interlink_id': interlink_id,
    })

@flis.route('/interlinks/<int:interlink_id>/delete', methods=['POST'])
def interlink_delete(interlink_id):
    session = database.session
    session['interlinks'].delete(interlink_id)
    session.commit()
    return flask.redirect(flask.url_for('flis.interlinks_listing'))

@flis.route('/')
@flis.route('/interlinks/')
def interlinks_listing():
    interlinks_rows = database.get_all('interlinks')
    interlinks = [schema.Interlink.from_flat(interlinks_row)
        for interlinks_row in interlinks_rows]
    return flask.render_template('interlinks_listing.html', **{
        'interlinks': interlinks,
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
        sources_row = database.get_or_404('sources', source_id)
        source_schema = schema.SourcesSchema.from_flat(sources_row)

    if flask.request.method == 'POST':
        form_data = dict(schema.SourcesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        source_schema = schema.SourcesSchema.from_flat(form_data)

        if source_schema.validate():
            if sources_row is None:
                sources_row = session['sources'].new()
            sources_row.update(source_schema.flatten())

            session.save(sources_row)
            session.commit()

            flask.flash('Source saved', 'success')
            location = flask.url_for('lists.source_view',
                                     source_id=sources_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in sources information', 'error')
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

@lists.route('/sources/<int:source_id>/')
def source_view(source_id):
    app = flask.current_app
    sources_row = database.get_or_404('sources', source_id)
    source = schema.SourcesSchema.from_flat(sources_row)
    return flask.render_template('source_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'source': source,
        'source_id': source_id,
    })

@lists.route('/sources/<int:source_id>/delete', methods=['POST'])
def source_delete(source_id):
    #sources_row = database.get_or_404('sources', source_id)

    session = database.session
    session['sources'].delete(source_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.sources_view'))

@lists.route('/sources/')
def sources_view():
    sources_rows = database.get_all('sources')
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
        trends_row = database.get_or_404('trends', trend_id)
        trend_schema = schema.TrendsSchema.from_flat(trends_row)

    if flask.request.method == 'POST':
        form_data = dict(schema.TrendsSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        trend_schema = schema.TrendsSchema.from_flat(form_data)

        if trend_schema.validate():
            if trends_row is None:
                trends_row = session['trends'].new()
            trends_row.update(trend_schema.flatten())

            session.save(trends_row)
            session.commit()

            flask.flash('Trend saved', 'success')
            location = flask.url_for('lists.trend_view', trend_id=trends_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in trends information', 'error')
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

@lists.route('/trends/<int:trend_id>/')
def trend_view(trend_id):
    app = flask.current_app
    trends_row = database.get_or_404('trends', trend_id)
    trend = schema.TrendsSchema.from_flat(trends_row)
    return flask.render_template('trend_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'trend': trend,
        'trend_id': trend_id,
    })

@lists.route('/trends/<int:trend_id>/delete', methods=['POST'])
def trend_delete(trend_id):
    #trends_row = database.get_or_404('trends', trend_id)

    session = database.session
    session['trends'].delete(trend_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.trends_view'))

@lists.route('/trends/')
def trends_view():
    trends_rows = database.get_all('trends')
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
        thematic_categories_row = database.get_or_404('thematic_categories',
                thematic_category_id)
        thematic_category_schema = schema.ThematicCategoriesSchema.from_flat(
                thematic_categories_row)

    if flask.request.method == 'POST':
        form_data = dict(
                schema.ThematicCategoriesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        thematic_category_schema = schema.ThematicCategoriesSchema.from_flat(
                form_data)

        if thematic_category_schema.validate():
            if thematic_categories_row is None:
                thematic_categories_row = session['thematic_categories'].new()
            thematic_categories_row.update(thematic_category_schema.flatten())

            session.save(thematic_categories_row)
            session.commit()

            flask.flash('Category saved', 'success')
            location = flask.url_for('lists.thematic_category_view',
                    thematic_category_id=thematic_categories_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in trends information', 'error')
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

@lists.route('/thematic_categories/<int:thematic_category_id>/')
def thematic_category_view(thematic_category_id):
    app = flask.current_app
    thematic_categories_row = database.get_or_404('thematic_categories',
            thematic_category_id)
    thematic_category = schema.ThematicCategoriesSchema.from_flat(
            thematic_categories_row)
    return flask.render_template('thematic_category_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'thematic_category': thematic_category,
        'thematic_category_id': thematic_category_id,
    })

@lists.route('/thematic_categories/<int:thematic_category_id>/delete',
        methods=['POST'])
def thematic_category_delete(thematic_category_id):
    session = database.session
    session['thematic_categories'].delete(thematic_category_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.thematic_categories_view'))

@lists.route('/thematic_categories/')
def thematic_categories_view():
    thematic_categories_rows = database.get_all('thematic_categories')
    thematic_categories = [
            schema.ThematicCategory.from_flat(thematic_categories_row)
            for thematic_categories_row in thematic_categories_rows]
    return flask.render_template('thematic_categories_view.html', **{
        'thematic_categories': thematic_categories,
    })

@lists.route('/geo_scales/new/', methods=['GET', 'POST'])
@lists.route('/geo_scales/<int:geo_scale_id>/edit',
        methods=['GET', 'POST'])
def geo_scale_edit(geo_scale_id=None):
    app = flask.current_app
    session = database.session

    if geo_scale_id is None:
        geo_scales_row = None
    else:
        geo_scales_row = database.get_or_404('geo_scales',
                geo_scale_id)
        geo_scale_schema = schema.GeographicalScalesSchema.from_flat(
                geo_scales_row)

    if flask.request.method == 'POST':
        form_data = dict(
                schema.GeographicalScalesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        geo_scale_schema = schema.GeographicalScalesSchema.from_flat(
                form_data)

        if geo_scale_schema.validate():
            if geo_scales_row is None:
                geo_scales_row = session['geo_scales'].new()
            geo_scales_row.update(geo_scale_schema.flatten())

            session.save(geo_scales_row)
            session.commit()

            flask.flash('Geographical scale saved', 'success')
            location = flask.url_for('lists.geo_scale_view',
                    geo_scale_id=geo_scales_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in trends information', 'error')
    else:
        if geo_scale_id:
            geo_scale_schema = schema.GeographicalScalesSchema.from_flat(
                    geo_scales_row)
        else:
            geo_scale_schema = schema.GeographicalScalesSchema()

    return flask.render_template('geo_scale_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'geo_scale_schema': geo_scale_schema,
        'geo_scale_id': geo_scale_id,
    })

@lists.route('/geo_scales/<int:geo_scale_id>/')
def geo_scale_view(geo_scale_id):
    app = flask.current_app
    geo_scales_row = database.get_or_404('geo_scales',
            geo_scale_id)
    geo_scale = schema.GeographicalScalesSchema.from_flat(
            geo_scales_row)
    return flask.render_template('geo_scale_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'geo_scale': geo_scale,
        'geo_scale_id': geo_scale_id,
    })

@lists.route('/geo_scales/<int:geo_scale_id>/delete',
        methods=['POST'])
def geo_scale_delete(geo_scale_id):
    session = database.session
    session['geo_scales'].delete(geo_scale_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.geo_scales_view'))

@lists.route('/geo_scales/')
def geo_scales_view():
    geo_scales_rows = database.get_all('geo_scales')
    geo_scales = [
            schema.GeographicalScale.from_flat(geo_scales_row)
            for geo_scales_row in geo_scales_rows]
    return flask.render_template('geo_scales_view.html', **{
        'geo_scales': geo_scales,
    })

@lists.route('/geo_coverages/new/', methods=['GET', 'POST'])
@lists.route('/geo_coverages/<int:geo_coverage_id>/edit',
        methods=['GET', 'POST'])
def geo_coverage_edit(geo_coverage_id=None):
    app = flask.current_app
    session = database.session

    if geo_coverage_id is None:
        geo_coverages_row = None
    else:
        geo_coverages_row = database.get_or_404(
                'geo_coverages', geo_coverage_id)
        geo_coverage_schema = schema.GeographicalCoveragesSchema.from_flat(
                geo_coverages_row)

    if flask.request.method == 'POST':
        form_data = dict(
                schema.GeographicalCoveragesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        geo_coverage_schema = schema.GeographicalCoveragesSchema.from_flat(
                form_data)

        if geo_coverage_schema.validate():
            if geo_coverages_row is None:
                geo_coverages_row = session['geo_coverages'].new()
            geo_coverages_row.update(
                    geo_coverage_schema.flatten())

            session.save(geo_coverages_row)
            session.commit()

            flask.flash('Geographical coverage saved', 'success')
            location = flask.url_for('lists.geo_coverage_view',
                    geo_coverage_id=geo_coverages_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in trends information', 'error')
    else:
        if geo_coverage_id:
            geo_coverage_schema = schema.GeographicalCoveragesSchema.from_flat(
                    geo_coverages_row)
        else:
            geo_coverage_schema = schema.GeographicalCoveragesSchema()

    return flask.render_template('geo_coverage_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'geo_coverage_schema': geo_coverage_schema,
        'geo_coverage_id': geo_coverage_id,
    })

@lists.route('/geo_coverages/<int:geo_coverage_id>/')
def geo_coverage_view(geo_coverage_id):
    app = flask.current_app
    geo_coverages_row = database.get_or_404('geo_coverages',
            geo_coverage_id)
    geo_coverage = schema.GeographicalCoveragesSchema.from_flat(
            geo_coverages_row)
    return flask.render_template('geo_coverage_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'geo_coverage': geo_coverage,
        'geo_coverage_id': geo_coverage_id,
    })

@lists.route('/geo_coverages/<int:geo_coverage_id>/delete',
        methods=['POST'])
def geo_coverage_delete(geo_coverage_id):
    session = database.session
    session['geo_coverages'].delete(geo_coverage_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.geo_coverages_view'))

@lists.route('/geo_coverages/')
def geo_coverages_view():
    geo_coverages_rows = database.get_all('geo_coverages')
    geo_coverages = [
            schema.GeographicalCoverage.from_flat(geo_coverages_row)
            for geo_coverages_row in geo_coverages_rows]
    return flask.render_template('geo_coverages_view.html', **{
        'geo_coverages': geo_coverages,
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
        steep_categories_row = database.get_or_404('steep_categories',
                steep_category_id)
        steep_category_schema = schema.SteepCategoriesSchema.from_flat(
                steep_categories_row)

    if flask.request.method == 'POST':
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

            flask.flash('Geographical coverage saved', 'success')
            location = flask.url_for('lists.steep_category_view',
                    steep_category_id=steep_categories_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in trends information', 'error')
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

@lists.route('/steep_categories/<int:steep_category_id>/')
def steep_category_view(steep_category_id):
    app = flask.current_app
    steep_categories_row = database.get_or_404('steep_categories',
            steep_category_id)
    steep_category = schema.SteepCategoriesSchema.from_flat(
            steep_categories_row)
    return flask.render_template('steep_category_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'steep_category': steep_category,
        'steep_category_id': steep_category_id,
    })

@lists.route('/steep_categories/<int:steep_category_id>/delete',
        methods=['POST'])
def steep_category_delete(steep_category_id):
    session = database.session
    session['steep_categories'].delete(steep_category_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.steep_categories_listing'))

@lists.route('/steep_categories/')
def steep_categories_listing():
    steep_categories_rows = database.get_all('steep_categories')
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
        timelines_row = database.get_or_404('timelines', timeline_id)
        timeline_schema = schema.TimelinesSchema.from_flat(timelines_row)

    if flask.request.method == 'POST':
        form_data = dict(schema.TimelinesSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())

        timeline_schema = schema.TimelinesSchema.from_flat(form_data)

        if timeline_schema.validate():
            if timelines_row is None:
                timelines_row = session['timelines'].new()
            timelines_row.update(timeline_schema.flatten())

            session.save(timelines_row)
            session.commit()

            flask.flash('Timeline saved', 'success')
            location = flask.url_for('lists.timeline_view',
                                     timeline_id=timelines_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in timeline information', 'error')
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

@lists.route('/timelines/<int:timeline_id>/')
def timeline_view(timeline_id):
    app = flask.current_app
    timelines_row = database.get_or_404('timelines', timeline_id)
    timeline = schema.TimelinesSchema.from_flat(timelines_row)
    return flask.render_template('timeline_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'timeline': timeline,
        'timeline_id': timeline_id,
    })

@lists.route('/timelines/<int:timeline_id>/delete', methods=['POST'])
def timeline_delete(timeline_id):
    session = database.session
    session['timelines'].delete(timeline_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.timelines_listing'))

@lists.route('/timelines/')
def timelines_listing():
    timelines_rows = database.get_all('timelines')
    timelines = [
        schema.Timeline.from_flat(timelines_row)
        for timelines_row in timelines_rows]
    return flask.render_template('timelines_listing.html', **{
        'timelines': timelines
    })

def _copy_file(src_file, dst_file):
    size = 0
    while True:
        buf = src_file.read(128*65535)
        if not buf:
            return size
        dst_file.write(buf)
        size += len(buf)

class FileSizeLimitExceeded(Exception):
    pass

def _save_file(form_data, uploaded_file, limit=None):
    app = flask.current_app

    with tempfile.TemporaryFile() as tmp:
        size = _copy_file(uploaded_file, tmp)
        if limit is not None and size > limit:
            raise FileSizeLimitExceeded
        tmp.seek(0)

        filename = uploaded_file.filename
        filename, ext = filename.rsplit('.', 1)
        user_files_folder = flask.safe_join(
            path(app.root_path), app.config['USER_FILES_PATH'])

        new_name = filename
        count = 0
        while path(flask.safe_join(user_files_folder, new_name+'.'+ext)).exists():
            count += 1
            new_name = filename + '_' + str(count)
        new_name = new_name + '.' + ext
        with open(flask.safe_join(user_files_folder, new_name), 'w+') as dst_file:
            _copy_file(tmp, dst_file)
    form_data['file_id'] = new_name

class IndicatorMissingFile(Exception):
    pass

def _delete_file(indicators_row):
    app = flask.current_app
    file_id = indicators_row.get('file_id', None)
    if file_id:
        user_files_folder = flask.safe_join(
            path(app.root_path), app.config['USER_FILES_PATH'])
        file_path = flask.safe_join(user_files_folder, file_id)
        path(file_path).remove_p()
        del indicators_row['file_id']

@lists.route('/indicators/new/', methods=['GET', 'POST'])
@lists.route('/indicators/<int:indicator_id>/edit', methods=['GET', 'POST'])
def indicator_edit(indicator_id=None):
    app = flask.current_app
    session = database.session

    if indicator_id is None:
        indicators_row = None
    else:
        indicators_row = database.get_or_404('indicators', indicator_id)
        indicator_schema = schema.IndicatorsSchema.from_flat(indicators_row)

    if flask.request.method == 'POST':
        form_data = dict(schema.IndicatorsSchema.from_defaults().flatten())
        form_data.update(flask.request.form.to_dict())


        uploaded_file = flask.request.files['file']
        file_error = None
        if uploaded_file.filename != u'':
            mb_limit = flask.current_app.config.get('FILE_SIZE_LIMIT_MB')
            limit = mb_limit * MByte
            try:
                _save_file(form_data, uploaded_file, limit)
                if indicators_row:
                    try:
                        _delete_file(indicators_row)
                    except IndicatorMissingFile:
                        pass
            except FileSizeLimitExceeded:
                file_error = 'File size limit exceeded (%d MB)' % mb_limit

        indicator_schema = schema.IndicatorsSchema.from_flat(form_data)
        if indicator_schema.validate() and not file_error:
            if indicators_row is None:
                indicators_row = session['indicators'].new()
            indicators_row.update(indicator_schema.flatten())

            session.save(indicators_row)
            session.commit()

            flask.flash('Indicator saved', 'success')
            location = flask.url_for('lists.indicator_view',
                                     indicator_id=indicators_row.id)
            return flask.redirect(location)

        else:
            flask.flash(u'Errors in indicators information', 'error')
            if file_error:
                indicator_schema['file_id'].valid = False
                indicator_schema['file_id'].errors.append(file_error)
    else:
        if indicator_id:
            indicator_schema = schema.IndicatorsSchema.from_flat(indicators_row)
        else:
            indicator_schema = schema.IndicatorsSchema()

    if indicators_row:
        indicator = schema.Indicator.from_flat(indicators_row)
    else:
        indicator = None
    return flask.render_template('indicator_edit.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_edit.html')),
        'indicator_schema': indicator_schema,
        'indicator': indicator,
        'indicator_id': indicator_id,
    })

@lists.route('/indicators/<int:indicator_id>/')
def indicator_view(indicator_id):
    app = flask.current_app
    indicators_row = database.get_or_404('indicators', indicator_id)
    indicator = schema.IndicatorsSchema.from_flat(indicators_row)
    return flask.render_template('indicator_view.html', **{
        'mk': MarkupGenerator(app.jinja_env.get_template('widgets_view.html')),
        'indicator': indicator,
        'indicator_id': indicator_id,
    })

@lists.route('/indicators/<int:indicator_id>/delete', methods=['POST'])
def indicator_delete(indicator_id):

    session = database.session
    indicators_row = database.get_or_404('indicators', indicator_id)
    _delete_file(indicators_row)
    session['indicators'].delete(indicator_id)
    session.commit()
    return flask.redirect(flask.url_for('lists.indicators_listing'))

@lists.route('/indicators/')
def indicators_listing():
    indicators_rows = database.get_all('indicators')
    indicators = []
    for indicators_row in indicators_rows:
        indicator = schema.Indicator.from_flat(indicators_row)
        indicator['id'] = indicators_row.id
        indicators.append(indicator)
    indicator_schema = schema.IndicatorsSchema()
    interlinks_rows = database.get_all('interlinks')
    interlinks = [schema.InterlinksSchema.from_flat(interlinks_row)
        for interlinks_row in interlinks_rows]
    trends = {}
    gmts = {}
    for indicator in indicators:
        trends[indicator['id']] = set()
        gmts[indicator['id']] = set()
        for interlink in interlinks:
            if indicator['id'] == interlink['indicator1'].value or \
               indicator['id'] == interlink['indicator2'].value or \
               indicator['id'] == interlink['indicator3'].value or \
               indicator['id'] == interlink['indicator4'].value:
                   trends[indicator['id']].add(
                       interlink['trend'].value_labels[interlink['trend'].value])
                   gmts[indicator['id']].add(
                       interlink['gmt'].value_labels[interlink['gmt'].value])
    return flask.render_template('indicators_listing.html', **{
        'indicators': indicators,
        'indicator_schema': indicator_schema,
        'trends': trends,
        'gmts': gmts,
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
