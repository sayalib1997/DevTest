DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}


# for test only to get the user details. frame.requests.get is mocked
FRAME_URL = True


SKIP_EDIT_AUTHORIZATION = False


# disable frame.Loader in tests, don't need it
TEMPLATE_LOADERS = ('django.template.loaders.app_directories.Loader',)
