from datetime import date
from django.db import models
from datetime import datetime, date


class Owner(models.Model):
    owner_first_name = models.CharField(max_length =30)
    owner_last_name = models.CharField(max_length=30)
    
    @property
    def owner_full_name(self):
        return '%s %s' % (self.owner_first_name, self.owner_last_name)

    def __str__(self) -> str:
        return (self.owner_full_name)
    
    class Meta:
        db_table = 'Owner'

class Color(models.Model):
    color_name = models.CharField(max_length=30)

    @property
    def color_display_name(self) :
        return '%s' % self.color_name
    def __str__(self) -> str:
        return(self.color_display_name)
    class Meta:
        db_table = 'Color'


class Duck(models.Model):
    duck_image = models.ImageField(upload_to = 'photos', blank = True)
    duck_first_name = models.CharField(max_length = 30)
    duck_last_name = models.CharField(max_length = 30)
    duck_age = models.IntegerField(default = 0)
    duck_birthday = models.DateField(default = date.today)
    body_color = models.ForeignKey(Color,related_name="a_body_color", null=True, blank=True, on_delete=models.SET_NULL)
    beak_color = models.ForeignKey(Color, related_name="a_beak_color", null=True, blank=True, on_delete=models.SET_NULL)
    Owner = models.ForeignKey(Owner, null=True, blank=True, on_delete=models.SET_NULL)
    
    @property
    def duck_age(self):
        today = datetime.now().date()

        return today.year - self.duck_birthday.year - ((today.month, today.day) < (self.duck_birthday.month, self.duck_birthday.day))
    @property
    def duck_full_name(self):
        return '%s %s' % (self.duck_first_name, self.duck_last_name)

    class Meta:
            db_table = 'Duck'

    # Create your models here.
