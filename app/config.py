import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        self.debug = os.getenv("DEBUG") or True
        self.host = os.getenv("MAPELLO_HOST") or "localhost"
        self.port = os.getenv("MAPELLO_PORT") or 9000
