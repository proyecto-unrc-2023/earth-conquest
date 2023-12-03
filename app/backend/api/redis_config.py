import redis

# Configure Redis
r = redis.Redis(
    host='localhost',
    port=6379,
)


def check_redis_connection():
    try:
        r.ping()
        print('=== Connected to Redis')
    except redis.ConnectionError:
        print('=== Cannot connect to Redis')


check_redis_connection()
