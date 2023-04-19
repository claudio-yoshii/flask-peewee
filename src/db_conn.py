from flask_mysqldb import MySQL

class mysql():
    def init(app):
        app.config['MYSQL_HOST'] = 'db001.cy9emovzqrlm.us-east-1.rds.amazonaws.com'
        app.config['MYSQL_USER'] = 'u_desafio_fullstack'
        app.config['MYSQL_PASSWORD'] = 'Svc6hxje,o$WPnM.'
        app.config['MYSQL_DB'] = 'base'
        return MySQL(app)