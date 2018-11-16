from .microservicio import db



@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    #db.create_all()
    print('Initialized the database.')