import boto3

session = boto3.session.Session()
ec2 = session.resource('ec2')

instances = ec2.create_instances(InstanceType='t1.micro',
                                 ImageId='ami-0d4c3eabb9e72650a',
                                 MinCount=1,
                                 MaxCount=2)

print(f'Created {len(instances)} EC2 instance(s).')
