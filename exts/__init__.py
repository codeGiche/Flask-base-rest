from .exts import *
from private.exts import init_private_exts
import inspect

loc = locals()
def init_exts(app):
    init_private_exts(app)
    for ext in loc:
        if not inspect.isclass(loc[ext]):
            if hasattr(loc[ext],'init_app'):
                loc[ext].init_app(app)