import os
import unittest

from flask_script import Manager

from app.main import create_app

app = create_app(os.getenv('APP_ENV') or 'dev')
app.app_context().push()
manager = Manager(app)

def run():
    manager.run()

def test():
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
