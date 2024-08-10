from django.db import models
from .gamer import Gamer
from .game import Game

class Event(models.Model):
  id = models.AutoField(primary_key=True)
  game = models.ForeignKey(Game, on_delete=models.CASCADE)
  description = models.CharField(max_length=50)
  date = models.DateField()
  time = models.TimeField()
  organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)

  @property
  def joined(self):
     return self.__joined

  @joined.setter
  def joined(self, value):
    self.__joined = value