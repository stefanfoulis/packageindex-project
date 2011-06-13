try:
    # import magic deployment specific settings
    from magic import whatever
except ImportError:
    # import default local development deployment settings
    from .local_development import *

TEMPLATE_DIRS = (
    project_root('templates')
)