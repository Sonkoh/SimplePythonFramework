import engine.server
import dotenv
import os
import importlib

archivos = os.listdir("routes")
app = engine.server.WebServer({key: value for key, value in dotenv.dotenv_values().items()})

for archivo in archivos:
    if archivo.endswith('.py'):
        m = importlib.import_module(f'routes.{archivo[:-3]}')
        if hasattr(m, 'routes'):
            m.routes(app)

app.listen()