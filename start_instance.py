import boto3
import time

session = boto3.session.Session()
ec2 = session.resource('ec2')

start_time = time.time()
instances = ec2.create_instances(InstanceType='t2.small',
                                 ImageId='ami-0d4c3eabb9e72650a',
                                 MinCount=1,
                                 MaxCount=2)

print(f'Created {len(instances)} EC2 instance(s).')

for steps in range(1, 10):
    print(f'\nAfter {(time.time() - start_time)/1e3} seconds:')
    for instance in instances:
        instance.reload()
        id = instance.id
        state = instance.state['Name']
        print(f'- Instance ID {id} is in state {state}')
    time.sleep(15)
