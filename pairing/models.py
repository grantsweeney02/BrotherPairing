from django.db import models

# Create your models here.
class Brother(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    new_members = models.ManyToManyField('Pledge', related_name='pledge')

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
class Pledge(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    brothers = models.ManyToManyField('Brother', related_name='brother')

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
class Pairing(models.Model):
    week_start = models.DateField()
    week_end = models.DateField()
    brother = models.ForeignKey('Brother', on_delete=models.CASCADE, related_name='pairings')
    pledge = models.ForeignKey('Pledge', on_delete=models.CASCADE)

    def __str__(self):
        return self.brother.first_name + " " + self.brother.last_name + " - " + self.pledge.first_name + " " + self.pledge.last_name