from importlib import import_module
import settings

def init_app(app):
    for module_name in settings.ENABLED_MODULES:
        module_path = ".{}".format(module_name)
        import_module(module_path, package=__name__).init_app(app)
