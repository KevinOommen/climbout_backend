from django.db import models

# Create your models here.
class events(models.Model):    
    location= models.TextField(blank=False)
    date = models.DateField()
    name = models.TextField(blank=False)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.name
    