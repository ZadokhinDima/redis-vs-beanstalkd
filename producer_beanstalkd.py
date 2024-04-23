import random
import greenstalk
# Connect to Beanstalkd server

beanstalk = greenstalk.Client(('localhost', 11300))

print(beanstalk.stats())

# Define the name of the queue
queue_name = 'my_queue'

# Generate and send random messages to the queue
i = 0
while True:
    message = f"Message {i+1}: {random.randint(1, 100)}"
    beanstalk.use(queue_name)
    beanstalk.put(message.encode(), priority=0, delay=0, ttr=60)
    print(f"Sent message: {message}")
    i += 1