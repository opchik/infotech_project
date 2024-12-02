from django.db import models

class Data(models.Model):
    ne = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    gsm = models.BooleanField(default=False)
    umts = models.BooleanField(default=False)
    lte = models.BooleanField(default=False)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.ne
