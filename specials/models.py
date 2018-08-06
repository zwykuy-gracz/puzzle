from django.db import models

class Hotm(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

class FablesOfGrimforest(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class TheSandEmpire(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class GuardiansOfTeltoc(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class EasterEvent(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class PiratesOfCorellia(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class KnightsOfAvalon(models.Model):
    name = models.CharField(max_length = 30)
    color = models.CharField(max_length = 20)
    stars = models.IntegerField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
