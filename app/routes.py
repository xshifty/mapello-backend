def setup(app):
    @app.route('/')
    def index():
        return 'Mapello 1.0'
