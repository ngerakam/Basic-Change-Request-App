"""
ASGI config for requestApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from requestApp.settings.base import DEBUG

from django.core.asgi import get_asgi_application


if DEBUG:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "requestApp.settings.local")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "requestApp.settings.prod")    

application = get_asgi_application()
