import time
import cloud_runner.instance_pool as instance_pool

start_time = time.time()

with instance_pool.InstancePool(5) as pool:
    all_up = False
    while not all_up:
        print(f'\nAfter {round(time.time() - start_time)} seconds:')
        pool.print_status()

        if pool.all_instances_up():
            break
        time.sleep(5)

    print('\nAll instances running.')

    print('\nTODO: Run tasks :-)')

print('\nDone.')
