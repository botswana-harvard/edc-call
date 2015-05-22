from django.db import models


class CallLogManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(subject_identifier)


class CallLogEntryManager(models.Manager):

    def get_by_natural_key(self, call_log, call_datetime):
        return self.get(call_log=call_log, call_datetime=call_datetime)
