from django.conf import settings
from django.db import models
from django.utils import timezone

class LectureList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lecture = models.CharField(db_column='LECTURE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prof = models.CharField(db_column='PROF', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    start = models.IntegerField(db_column='START', blank=True, null=True)  # Field name made lowercase.
    end = models.IntegerField(db_column='END', blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(db_column='DAY', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lecture_list'

class EnrollList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    memo = models.CharField(db_column='MEMO', max_length=500, blank=True, null=True)  # Field name made lowercase.
    lecture = models.CharField(db_column='LECTURE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    prof = models.CharField(db_column='PROF', max_length=200, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=200, blank=True, null=True)  # Field name made lowercase.
    start = models.CharField(db_column='START', max_length=20, blank=True, null=True)  # Field name made lowercase.
    end = models.CharField(db_column='END', max_length=20, blank=True, null=True)  # Field name made lowercase.
    day = models.CharField(db_column='DAY', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lecture_info = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(db_column='DESCRIPTION', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'enroll_list'

    def enroll_save(self) :
        self.save()

    class Meta:
        managed = False
        db_table = 'enroll_list'
