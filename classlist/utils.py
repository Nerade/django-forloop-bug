from django.apps import apps
from django.core.cache import cache
from django.conf import settings

from .models import FormDocument

_class_exclude_list = []

def exclude_class(model=None):
    def wrapper(model):
        if not model in _class_exclude_list:
            _class_exclude_list.append(model)
        return model

    if model is None:
        return wrapper
    else:
        return wrapper(model)

def get_custom_apps():
    app_list = reversed(apps.get_app_configs())
    while True:
        app = next(app_list)
        yield app
        if app.name == 'core':
            break
    
def get_class_list():
    class_list = cache.get('class_list')
    if not class_list:
        class_list = [f for app in get_custom_apps() for f in app.get_models() if issubclass(f,FormDocument) and f not in _class_exclude_list]
        cache.set('class_list',class_list,None)
    print("class_list:",class_list)
    return class_list

def class_for_name(module_name, class_name):
    # load the module, will raise ImportError if module cannot be loaded
    m = __import__(module_name, globals(), locals(), class_name)
    # get the class, will raise AttributeError if class cannot be found
    c = getattr(m, class_name)
    return c
