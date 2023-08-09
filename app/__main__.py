from . import create_app
from . import routes
from .config import Config

config = Config()
app = create_app()

routes.setup(app)

app.run(host=config.host, port=config.port, debug=config.debug, load_dotenv=False)
