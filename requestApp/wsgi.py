"""
WSGI config for requestApp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
from requestApp.settings.base import DEBUG

from django.core.wsgi import get_wsgi_application


if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "requestApp.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "requestApp.settings.prod")    

application = get_wsgi_application()
