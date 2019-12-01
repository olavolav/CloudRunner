import boto3
import cloud_runner.monitored_instance as mi


class InstancePool:
    """InstancePool is the list of monitored instances that we work with."""
    def __init__(self):
        self.session = boto3.session.Session()
        self.ec2 = self.session.resource('ec2')
        self.m_instances = []

    def start_instances(self, nr_instances: int):
        ec2_instances = self.ec2.create_instances(
            InstanceType='t2.small',
            ImageId='ami-0d4c3eabb9e72650a',
            MinCount=1,
            MaxCount=nr_instances)

        self.m_instances = [mi.MonitoredInstance(i) for i in ec2_instances]
        print(f'Created {len(self.m_instances)} EC2 instance(s).')

    def terminate_instances(self):
        l = len(self.m_instances)
        for i in self.m_instances:
            i.terminate()
        print(f'\nTerminated {l} EC2 instance(s).')

    def get_instance_ids(self):
        return [i.get_id() for i in self._m_instances]

    def print_status(self):
        for mi in self.m_instances:
            print(f'ID {mi.get_id()}: {mi.get_state()}')
