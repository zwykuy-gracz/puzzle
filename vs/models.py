from django.db import models

class ThreeStars(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='images/3/')

    def __str__(self):
        return self.name

class FourStars(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='images/4/')

    def __str__(self):
        return self.name

class FiveStars(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    image = models.ImageField(upload_to='images/5/')

    def __str__(self):
        return self.name
