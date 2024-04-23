import redis
import time

# Connect to Redis
redis_host = 'localhost'
redis_port = 6381
redis_db = 0
redis_client = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

queue_name = 'message_queue'

start_time = time.time()
i = 0

# Continuously consume messages from the queue
while True:
    # Block until a message is available in the queue
    message = redis_client.blpop(queue_name)

    # Extract the message value
    message_value = message[1].decode('utf-8')
    
    if (i + 1) % 100000 == 0:
        elapsed_time = time.time() - start_time
        print(f"Time taken for {100000} reads: {elapsed_time} seconds")
        start_time = time.time()

    i += 1