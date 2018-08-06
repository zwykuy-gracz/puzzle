from django.db import models

class Camp1(models.Model):
    name = models.CharField(max_length = 30)
    stars = models.IntegerField()
    color = models.CharField(max_length = 20)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class Camp2(models.Model):
    name = models.CharField(max_length = 30)
    stars = models.IntegerField()
    color = models.CharField(max_length = 20)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
