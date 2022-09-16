from django.db import models

# Create your models here.

class InputTable(models.Model):
    id = models.AutoField(primary_key=True)
    Input_str1=models.CharField(max_length=300,null=True, blank=True)
    Input_str2=models.CharField(max_length=300,null=True, blank=True)
    def __str__(self):
        return str(self.id)
