from flask_script import Manager
from app import main, db
from flask_migrate import Migrate, MigrateCommand

migrate = Migrate(main.app, db)
manager = Manager(main.app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()