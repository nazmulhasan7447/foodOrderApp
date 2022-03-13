from django.db import models

class Hotels(models.Model):
    name = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=255, default='')
    state = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    check_in = models.CharField(max_length=255, default='')
    check_out = models.CharField(max_length=255, default='')
    attraction_one_name = models.CharField(max_length=255, default='')
    attraction_one_distance = models.CharField(max_length=255, default='')
    attraction_two_name = models.CharField(max_length=255, default='')
    attraction_two_distance = models.CharField(max_length=255, default='')
    map_link = models.TextField(default='')
    ac = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    tv = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)

    def __str__(self):
        return self.name + " || " + str(self.pk)
