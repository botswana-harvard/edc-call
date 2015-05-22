

class CallHelper(object):

    def __init__(self, call_log_entry):
        self._appointment = None

    @property
    def appointment(self):
        """Returns an appointment after either updating or creating."""
        return self._appointment
