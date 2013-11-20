from django_assets import Bundle, register


JS_ASSETS = (
    'bootstrap/js/bootstrap.js',
)


CSS_ASSETS = (
    'bootstrap/css/bootstrap.css',
    'bootstrap/css/bootstrap-responsive.css',
)


js = Bundle(*JS_ASSETS, filters='jsmin', output='static/packed.js')
css = Bundle(*CSS_ASSETS, filters='cssmin', output='static/packed.css')


register('js', js)
register('css', css)
