from django.db import models

class Hotels(models.Model):
    hotel_id = models.CharField(max_length=255, default='', blank=True, null=True)
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

class HotelImages(models.Model):
    hotel = models.OneToOneField(Hotels, on_delete=models.CASCADE)
    img1 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img2 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img3 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img4 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img5 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img6 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img7 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img8 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img9 = models.ImageField(upload_to='hotel_images', blank=True, null=True)
    img10 = models.ImageField(upload_to='hotel_images', blank=True, null=True)

    def __str__(self):
        return self.hotel.name

class Deals(models.Model):
    title = models.CharField(default='', max_length=255)
    promocode = models.CharField(default='', max_length=255)
    brand_name = models.CharField(default='', max_length=255)
    terms_condition = models.CharField(default='', max_length=255)
    logo = models.ImageField(upload_to='brand_logo')

    def __str__(self):
        return self.title

