from application import app
from exts import init_exts

app.config.from_object('config.Developement')

init_exts(app)
app.run()