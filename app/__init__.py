from datetime import datetime
import os

from flask import Flask
from flask_wtf.csrf import CSRFProtect

csrf_protect = CSRFProtect()
def create_app(extra_config_settings={}):
    """Create a Flask applicaction.
    """
    # Instantiate Flask
    app = Flask(__name__)

    # Load App Config settings
    # Load common settings from 'app/settings.py' file
    app.config.from_object('app.settings')
    # Load local settings from 'app/local_settings.py'
    app.config.from_object('app.local_settings')
    # Load extra config settings from 'extra_config_settings' param
    app.config.update(extra_config_settings)

    # Setup WTForms CSRFProtect
    csrf_protect.init_app(app)

    # Register blueprints
    from app.views.misc_views import main_blueprint
    from app.views.apis import api_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(api_blueprint)
    csrf_protect.exempt(api_blueprint)
    
    # Register blueprints
    from app.views.misc_views import main_blueprint
    app.register_blueprint(main_blueprint)

    # Define bootstrap_is_hidden_field for flask-bootstrap's bootstrap_wtf.html
    from wtforms.fields import HiddenField

    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)

    app.jinja_env.globals['bootstrap_is_hidden_field'] = is_hidden_field_filter

    return app