"""
WSGI config for my_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import sys
sys.path.append('../')
#for p in sys.path: print(p)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_website.prod_settings")

application = get_wsgi_application()
