from django.db import models
from django.contrib.auth.models import User
from shop.models import ClickButton, Background

class PlayerInventory(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, default=None, editable=False)
    name = models.ForeignKey(User, default=None)
    total_clicks = models.IntegerField(default=0)
    equipped_button = models.ForeignKey(ClickButton, default=None)
    equipped_background = models.ForeignKey(Background, default=None)


    class Meta():
        verbose_name = 'Player'
        verbose_name_plural = "Players' stats"

    def __str__(self):
        return self.name.username