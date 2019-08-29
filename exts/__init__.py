from .exts import *
import rest

import inspect

loc = locals()
def init_exts(app):
    for ext in loc:
        if not inspect.isclass(loc[ext]):
            if hasattr(loc[ext],'init_app'):
                loc[ext].init_app(app)