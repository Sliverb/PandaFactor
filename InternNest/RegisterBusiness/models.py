from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __unicode__(self):
        return self.name
        
    class Meta:
      verbose_name = 'Business'
      verbose_name_plural = 'Businesses'

class Job(models.Model):
    business = models.ForeignKey(Business)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

