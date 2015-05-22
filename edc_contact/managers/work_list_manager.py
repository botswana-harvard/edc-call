from django.db import models


class WorkListManager(models.Manager):

    def get_by_natural_key(self, subject_identifier):
        return self.get(subject_identifier=subject_identifier,)


class FollowUpListManager(models.Manager):

    def get_by_natural_key(self, work_list, contact_datetime):
        return self.get(work_list=work_list, contact_datetime=contact_datetime)
