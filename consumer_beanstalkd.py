import greenstalk
import time

def read_from_beanstalkd(tube_name):
    beanstalk = greenstalk.Client(('localhost', 11300))
    beanstalk.watch(tube_name)

    print(beanstalk.stats())

    start_time = time.time()
    i = 0
    while True:
        job = beanstalk.reserve()
        # Process the job here
        beanstalk.delete(job.id)

        if (i + 1) % 100000 == 0:
            elapsed_time = time.time() - start_time
            print(f"Time taken for {100000} reads: {elapsed_time} seconds")
            start_time = time.time()

        i += 1

read_from_beanstalkd("my_queue")