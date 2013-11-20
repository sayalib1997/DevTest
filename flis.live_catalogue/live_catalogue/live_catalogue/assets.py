from django_assets import Bundle, register


JS_ASSETS = (
    'bootstrap/js/bootstrap.js',
    'js/jquery-ui-1.8.18.custom.min.js',
    'js/select2.min.js',
    'js/main.js',
)


CSS_ASSETS = (
    'bootstrap/css/bootstrap.css',
    'bootstrap/css/bootstrap-responsive.css',
    'css/bootstrap-ui/jquery-ui-1.8.16.custom.css',
    'css/select2/select2.css',
)


js = Bundle(*JS_ASSETS, filters='jsmin', output='static/packed.js')
css = Bundle(*CSS_ASSETS, filters='cssmin', output='static/packed.css')


register('js', js)
register('css', css)
