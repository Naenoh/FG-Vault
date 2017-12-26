from flask_script import Manager
from app import main

manager = Manager(main.app)

if __name__ == '__main__':
    manager.run()