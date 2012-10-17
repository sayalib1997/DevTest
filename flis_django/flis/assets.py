from django_assets import Bundle, register


JS_ASSETS = (
    'js/jquery-1.7.1.min.js',
    'js/jquery.uniform.js',
    'bootstrap/js/bootstrap.js',
)


CSS_ASSETS = (
    'bootstrap/css/bootstrap.css',
    'bootstrap/css/bootstrap-responsive.css',
    'css/uniform.default.css',
)


js = Bundle(*JS_ASSETS, filters='jsmin', output='gen/packed.js')
css = Bundle(*CSS_ASSETS, filters='cssmin', output='gen/packed.css')


register('js', js)
register('css', css)