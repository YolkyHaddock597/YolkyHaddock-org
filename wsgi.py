from web import app

if __name__ == '__main__':
    #app.config['SERVER_NAME'] = "localhost:5000"
    app.run()


#gunicorn --bind 0.0.0.0:5000 wsgi:app