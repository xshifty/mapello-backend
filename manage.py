import os

from flask_script import Manager

from app.main import create_app

app = create_app(os.getenv('APP_ENV') or 'dev')
app.app_context().push()
manager = Manager(app)

def run():
    manager.run()

if __name__ == '__main__':
    manager.run()
