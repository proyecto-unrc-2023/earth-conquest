import os

from app import create_app, redis

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    redis.init_app(app)
    print(app.url_map)
    app.run(debug=True)
