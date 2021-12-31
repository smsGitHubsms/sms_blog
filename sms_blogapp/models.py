from django.conf import settings
from django.db import models
import datetime

# Create your models here.
class blog(models.Model):
    def __str__ (self):
        return self.heading
    heading=models.CharField(max_length=150)
    date = models.DateField(default=datetime.date.today)
    desc = models.CharField(max_length=700)
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='blogimg',null='true')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null='true')



