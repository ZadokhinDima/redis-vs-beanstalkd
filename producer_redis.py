import redis
import random

# Connect to Redis
redis_host = 'localhost'
redis_port = 6381
redis_db = 0
redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

queue_name = 'message_queue'

while True:
    message = random.randint(1, 100)
    # Push the message to a Redis list
    redis_client.lpush(queue_name, random.randint(1, 100))
    print(f"Sent message: {message}")