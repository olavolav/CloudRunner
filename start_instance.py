import time
import cloud_runner.instance_pool

start_time = time.time()

pool = cloud_runner.instance_pool.InstancePool()
pool.start_instances(5)

try:
    for steps in range(1, 8):
        print(f'\nAfter {round(time.time() - start_time)} seconds:')
        pool.print_status()
        time.sleep(15)
finally:
    pool.terminate_instances()
