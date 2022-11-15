from datetime import date
from django.db import models

class Duck(models.Model):
    duck_image = models.ImageField(upload_to = 'photos')
    duck_first_name = models.CharField(max_length = 30)
    duck_last_name = models.CharField(max_length = 30)
    duck_age = models.IntegerField(default = 0)
    duck_birthday = models.DateField(default = date.today)
    body_color = models.CharField(max_length = 30)
    beak_color = models.CharField(max_length = 30)
    owner_first_name = models.CharField(max_length = 30)
    owner_last_name = models.CharField(max_length = 30)

    @property
    def duck_full_name(self):
        return '%s %s' % (self.duck_first_name, self.duck_last_name)

    def __str__(self) -> str:
        return (self.duck_full_name)

    # Create your models here.
