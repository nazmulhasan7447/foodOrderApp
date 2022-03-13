from django.db import models
from django.contrib.auth.models import User


# class ChampionUserList(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(user_level_tag='champion')
#
#     def save(self, *args, **kwargs):
#         converted_accuracy = float(str(self.accuracy).split('%')[0])
#         converted_wpm = int(self.wpm)
#
#         if converted_accuracy >= 80 and converted_wpm >= 40 and converted_wpm < 45:
#             self.user_level_tag = 'champion'
#             super().save(*args, **kwargs)
#
#     objects = models.Manager() # built-in manager
#     championObjects = ChampionUserList()
