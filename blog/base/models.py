from datetime import datetime
from django.db import models

# Create your models here.
class Blogs(models.Model):
    idn = models.IntegerField()
    heading = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now=True)
    content = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.heading