import os

from app import create_app
from app.backend.api.redis_config import r

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)
