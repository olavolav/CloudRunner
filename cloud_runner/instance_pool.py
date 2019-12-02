import boto3
import cloud_runner.monitored_instance as mi


class InstancePool:
    """InstancePool is the list of monitored instances that we work with."""
    def __init__(self, max_instances: int = 3):
        self.session = boto3.session.Session()
        self.ec2 = self.session.resource('ec2')
        self.key_pair = None
        self.max_instances = max_instances
        self.m_instances = []

    def __enter__(self):
        """Context manager __enter__ method."""
        # TODO Generate key pair
        self._start_instances()
        return self

    def __exit__(self, type, value, tb):
        """Context manager __exit__ method."""
        self._terminate_instances()

    def print_status(self):
        for mi in self.m_instances:
            print(f'- ID {mi.get_id()}: {mi.get_state()}')

    def all_instances_up(self):
        for mi in self.m_instances:
            if not mi.is_running():
                return False
        return True

    ###########
    # private #
    ###########

    def _start_instances(self):
        ec2_instances = self.ec2.create_instances(
            InstanceType='t2.small',
            ImageId='ami-0d4c3eabb9e72650a',
            MinCount=1,
            MaxCount=self.max_instances)

        self.m_instances = [mi.MonitoredInstance(i) for i in ec2_instances]
        print(f'Created {len(self.m_instances)} EC2 instance(s).')

    def _terminate_instances(self):
        l = len(self.m_instances)
        for i in self.m_instances:
            i.terminate()
        print(f'\nTerminated {l} EC2 instance(s).')

    def _get_instance_ids(self):
        return [i.get_id() for i in self._m_instances]
