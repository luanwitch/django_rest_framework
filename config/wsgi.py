import os
import sys

path = '/home/luanvieira9/django_rest_framework'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings' 

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()