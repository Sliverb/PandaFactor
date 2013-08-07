from django.db import models
from django.contrib.auth import get_user_model


class Job(models.Model):
    creator = models.ForeignKey(get_user_model())
    
    title = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    is_paid = models.BooleanField(default=True)
    description = models.CharField(max_length=800)
    is_public = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
