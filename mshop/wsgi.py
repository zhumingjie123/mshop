"""
WSGI config for mvote project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
import sys

path = '/home/letigang123/mshop'
if path not in sys.path:
    sys.path.append(path)

os.environ["DJANGO_SETTINGS_MODULE"] = 'mshop.settings'
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
