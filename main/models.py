from django.db import models 
# from account.models import Profile
# Create your models here.
class Ea(models.Model):
    name = models.CharField(max_length=50, unique=True)
 
    def __str__(self):
        return str(self.name)