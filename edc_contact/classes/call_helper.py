from ..utils.update_household_work_list import update_household_work_list


class CallHelper(object):

    def __init__(self, call_log_entry):
        self._member_appointment = None
        self._work_list = None
        self.call_log_entry = call_log_entry
        self.label = call_log_entry.call_log.label

    @property
    def call_log_entry(self):
        return self._call_log_entry

    @call_log_entry.setter
    def call_log_entry(self, value):
        self._call_log_entry = value

    @property
    def work_list(self):
        return self._work_list
