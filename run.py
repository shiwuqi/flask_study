import os
from dotenv import load_dotenv
from flask_migrate import Migrate, upgrade
from app.models import User
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# 绑定app和数据库，以便进行操作
migrade = Migrate(app, db)

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

@app.cli.command()
def deploy():
    """Run deployment tasks."""
    # migrate database to latest revision
    upgrade()

    db.create_all()