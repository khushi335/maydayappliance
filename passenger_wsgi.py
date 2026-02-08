import sys
import os

# Path to your project directory
PROJECT_DIR = "/home/hightech/project.columbiatransportation.com/air"

# Add project to Python path
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# Activate virtual environment
activate_env = "/home/hightech/virtualenv/project.columbiatransportation.com/air/3.10/bin/activate_this.py"
with open(activate_env) as f:
    exec(f.read(), {'__file__': activate_env})

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "air.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
