"""
WSGI config for metaativa_projeto project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'metaativa_projeto.settings')

application = get_wsgi_application()
