import environ
import os
from django.conf import settings

env = environ.Env()
environ.Env.read_env(os.path.join(settings.BASE_DIR, '.env'))