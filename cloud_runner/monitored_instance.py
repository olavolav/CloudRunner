import time


class MonitoredInstance:
    def __init__(self, instance):
        self.assigned_job_id = None
        self._instance = instance
        self._last_state_update = None

    def get_id(self):
        return self._instance.id

    def get_state(self):
        self._update_instance()
        return self._instance.state['Name']

    def is_running(self):
        return self.get_state() == 'running'

    def terminate(self):
        return self._instance.terminate()

    ###########
    # private #
    ###########

    def _update_instance(self):
        if self._info_is_outdated():
            self._instance.reload()

    def _info_is_outdated(self):
        if self._last_state_update is None:
            return True

        return self._last_state_update < time.time() - time.timedelta(
            seconds=1)
