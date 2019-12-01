import time
import cloud_runner.instance_pool

start_time = time.time()

pool = cloud_runner.instance_pool.InstancePool()

try:
    pool.start_instances(7)

    all_up = False
    while not all_up:
        print(f'\nAfter {round(time.time() - start_time)} seconds:')
        pool.print_status()

        if pool.all_instances_up():
            break
        time.sleep(5)

    print('\nAll instances running.')

    print('\nTODO: Run tasks :-)')

finally:
    pool.terminate_instances()

print('\nDone.')
