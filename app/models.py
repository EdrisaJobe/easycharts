from django.db import models

# Create your models here.
class UserInput(models.Model):
    
    category = models.CharField(max_length=20, blank=True, verbose_name="")
    num_of_items = models.IntegerField(verbose_name="", blank=True)
    
    def __str__(self):
        
        return f'{self.category} - {self.num_of_items}'

class FileInputModel(models.Model):

    files = models.FileField(upload_to='excel/', verbose_name="")