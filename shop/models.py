from django.db import models

class ClickButton(models.Model):
    btn_name = models.CharField(max_length=30)
    btn_image = models.ImageField()
    btn_price = models.IntegerField(unique=True)

    class Meta():
        verbose_name  = 'click button'
        verbose_name_plural = 'Buttons'

    def __str__(self):
        return self.btn_name

class Background(models.Model):
    bkg_name = models.CharField(max_length=30)
    bkg_image = models.ImageField()
    bkg_price = models.IntegerField(unique=True)

    def __str__(self):
        return self.bkg_name
