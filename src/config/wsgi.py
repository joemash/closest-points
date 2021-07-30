"""
WSGI config for closest_points project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
"""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings")

from django.core.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
