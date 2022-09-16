from django.db import models

# Create your models here.
class UserInformation(models.Model):
    id = models.AutoField(primary_key=True)
    utm_source=models.CharField(max_length=250,null=True, blank=True)
    utm_medium=models.CharField(max_length=250,null=True, blank=True)
    requestId=models.CharField(max_length=250,null=True, blank=True)
    visitorId=models.CharField(max_length=250,null=True, blank=True)
    def __str__(self):
        return str(self.id)

