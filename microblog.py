from app import app, db
from app.models import User, Post

@app.shell_context_processor # grinberg ch4, Shell Context
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}