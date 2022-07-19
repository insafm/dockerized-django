from .base import *

DEBUG = True

INSTALLED_APPS += [
	# 'debug_toolbar',
]

# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DEBUG_TOOLBAR_CONFIG = {
# 	'JQUERY_URL': '',
# }