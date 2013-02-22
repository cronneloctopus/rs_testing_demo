from django.db import models


# Create your models here.
class Animals(models.Model):
    name = models.CharField(max_length=155)
    votes = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name
