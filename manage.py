from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import create_app
from app.extensions import db

from scripts import commands


app = create_app(log_info=False)
migrate = Migrate(app, db)
manager = Manager(app)

for command in commands:
    manager.add_command(*command)

manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    manager.run()

