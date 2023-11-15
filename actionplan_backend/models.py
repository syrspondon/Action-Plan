from django.db import models


class BRCA1Breast(models.Model):
    age = models.IntegerField(null=True, blank=True, unique=True)
    averageTen = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    averageLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    residualLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    

class BRCA1Ovarine(models.Model):
    age = models.IntegerField(null=True, blank=True, unique=True)
    averageTen = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    averageLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    residualLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    

class BRCA2Breast(models.Model):
    age = models.IntegerField(null=True, blank=True)
    averageTen = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    averageLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    residualLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    

class BRCA2Ovarine(models.Model):
    age = models.IntegerField(null=True, blank=True)
    averageTen = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    averageLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    residualLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    

class PALB2Breast(models.Model):
    age = models.IntegerField(null=True, blank=True)
    averageTen = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    averageLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    residualLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)
    

class PALB2Ovarine(models.Model):
    age = models.IntegerField(null=True, blank=True)
    averageTen = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentile = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    averageLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    lowerCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    upperCentileLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)
    residualLifetime = models.DecimalField(decimal_places=10, max_digits=20, null=True, blank=True)

    def __str__(self):
        return str(self.id)
