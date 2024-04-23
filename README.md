# redis-vs-beanstalkd

In scope of this task I measured how long it takes to produce and consume 100k messages for 3 queue options:
1. beanstalkd
2. Redis with default rdb config
3. Redis with every second rdb save
4. Redis with every second aof save
5. Redis with allways aof save

Problems: not possible to use beanstalkd binlog feature on Windows. Therefore comparison is not too fair.

Results:

| Queue Option                  | Time Taken for 100k reads |
|-------------------------------|---------------------------|
| beanstalkd                    | 53 seconds on average     |
| Redis default rdb config      | 28 seconds on average     |
| Redis every second rdb save   | 34 seconds on average     |
| Redis every second appendfile | 34 seconds on average     |
| Redis allways appendfile      | 1185 seconds on average     |


Even though beanstalkd didn't save data to disk it was slower then redis even with disc writes every second. `appendfsync always` is much slower as redis writes to disk with every produced and consumed message.