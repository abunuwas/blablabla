import os
from dotenv import load_dotenv

if not os.environ.get('TESTING'):
    if os.path.exists('.env'):
        load_dotenv('.env')

    if os.path.exists('local.env'):
        load_dotenv('local.env')

    if os.path.exists('settings/secure_settings.env'):
        load_dotenv('settings/secure_settings.env')


from .base import *  # noqa
